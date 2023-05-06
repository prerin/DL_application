# filling mask
*で虫食いにした文章を入れると、それを推測するアプリ

## DEMO
![demo](https://github.com/prerin/dl_application/blob/master/filling_mask/img/ssPkRfsZ55JhcjXKb7q41683373740-1683373753.gif)

## Features
入力に指定の文章の一部を*にしたものを入れ、実行するとその部分に入るのにbertが妥当だと思った単語を出力します。

## Installation
'''bash<br>
pip install gradio<br>
pip install numpy<br>
brew install mecab-ipadic<br>
brew install mecab<br>
pip install mecab-python3<br>
pip install unidic-lite<br>
pip install transformers<br>
'''


## Usage
python exucute.pyを実行すると、gradioがurlを発行します。<br>
そのurl先で、入力を入れると使うことができます。<br>
入力がおかしい場合は、「*が含まれていません」が出力されます。

## Note
dataのJapanese_L-12_H-768_A-12_E-30_BPEフォルダは自分で用意する必要があります。<br>
data/preprocess.ipynbを順番に実行することで準備することができます。

