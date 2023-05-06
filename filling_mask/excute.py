import torch
from transformers import BertTokenizer, BertForMaskedLM, BertConfig
import numpy as np
import MeCab
import gradio as gr

config = BertConfig.from_json_file('./Japanese_L-12_H-768_A-12_E-30_BPE/bert_config.json')

model = BertForMaskedLM.from_pretrained('./Japanese_L-12_H-768_A-12_E-30_BPE/pytorch_model.bin', config=config)
bert_tokenizer = BertTokenizer('./Japanese_L-12_H-768_A-12_E-30_BPE/vocab.txt',
                                do_lower_case=False, do_basic_tokenize=False)

def preprocessing(pre_text):
  wakati = MeCab.Tagger("-Owakati")
  tokenized_text = wakati.parse(pre_text).split()
  tokenized_text.insert(0, '[CLS]')
  tokenized_text.append('[SLP]')
  if '*' not in tokenized_text:
    return "*が含まれていません", 0
  masked_index = tokenized_text.index('*')
  tokenized_text[masked_index] = '[MASK]'
  tokens = bert_tokenizer.convert_tokens_to_ids(tokenized_text)
  tokens_tensor = torch.tensor([tokens])  
  return tokens_tensor, masked_index

def predict(tonsor, masked_index):
  model.eval()
  with torch.no_grad():
    outputs = model(tonsor)
    predictions = outputs[0]
  _,predicted_indexes = torch.topk(predictions[0, masked_index], k=10)
  predicted_tokens = bert_tokenizer.convert_ids_to_tokens(predicted_indexes.tolist())
  return predicted_tokens

def predict_asterisk(pre_text):
  sentence = str(pre_text)
  tokens_tensor, index = preprocessing(sentence)
  if type(tokens_tensor) is str:
    return tokens_tensor
  predicted_tokens = predict(tokens_tensor, index)
  return predicted_tokens[0]

demo = gr.Interface(fn=predict_asterisk,
                    inputs=[gr.Textbox(label="sentence containing an asterisk")],
                    outputs="text"
                    )
demo.launch()