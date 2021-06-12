# /實驗室資源管理與工具/embeddings


<a href='https://drive.google.com/drive/folders/1wsGWJlqgI9dWv1_cpZFZaN0yvWpKFF3X' target='_blank' class='drive-location'><code>/實驗室資源管理與工具/embeddings/FastText_UsageOn121</code></a>

## FastText Pretrained Word Vectors

### Description

- 根據 Common Crawl 與 Wikipedia 訓練的中文詞向量 (同時包含簡、繁體)
- [Word vectors for 157 languages: Chinese binary model](https://fasttext.cc/docs/en/crawl-vectors.html) (6.8GB, uncompressed)


#### 資料使用

由於 FastText 的資料很大，**自己的電腦很可能無法處理** (而且下載模型要不少時間)，因此下方說明如何在 **LOPE 121 server** 上使用已下載好的 FastText word vector。

這邊使用 `gensim` 的 [FastText wrapper](https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#sphx-glr-auto-examples-tutorials-run-fasttext-py) (記得先在自己的 venv `pip install gensim`):

    
```python
from gensim.models.wrappers import FastText

# 載入模型 (大約要 1 分鐘)
model = FastText.load_fasttext_format('/home/yongfu/fasttext-cc.zh.300.bin')

# 測試訓練資料中是否有該詞彙
"語言所" in model.wv.vocab
#> True

# 測試能否取得某詞彙之詞向量 (i.e. 訓練資料含有該詞彙 或 可透過 subword info 計算出來)
"語言所" in model
#> True

# 取得詞向量
model.wv["語言所"]
#> array([ 1.50353173e-02, -6.50167018e-02,  1.50109693e-01, -4.27900888e-02,
#>        -9.06715021e-02, -8.23854804e-02,  1.25261307e-01,  5.17920628e-02,
#>         ...
#>        -3.61525565e-02,  7.66911805e-02,  6.42841533e-02, -5.33376262e-02,
#>         4.04697210e-02,  4.73028347e-02,  7.43498094e-03, -4.26138751e-02],
#>       dtype=float32)

# 計算兩詞彙之 cosine similarity
model.similarity("語言所", "語言")
#> 0.4139877

# 取得與某詞彙最相似的前 n 個詞彙, see https://bit.ly/2D1nIJQ
model.most_similar("語言所", topn=3)
#> [('文哲所', 0.7951180934), ('國文哲', 0.7393301129), ('博士論文', 0.7151889204)]
```


#### 資料來源與處理簡述

由 [FastText](https://fasttext.cc) 釋出的詞向量資料。這邊未進行處理，僅下載到 LOPE 121 server 方便大家使用。
<a href='https://drive.google.com/drive/folders/1TmtfHQJ7EcDI9vFrw-HX7J3LOJyD45od' target='_blank' class='drive-location'><code>/實驗室資源管理與工具/embeddings/fasttext</code></a>

## Title
### Description
<a href='https://drive.google.com/drive/folders/1l2CTLOOJeQivRvDTGwqdypWzqrvmdZ4I' target='_blank' class='drive-location'><code>/實驗室資源管理與工具/embeddings/ptt</code></a>

## Title
### Description