語料衍生資料
==============================

{docsify-updated}


Frequency Data
------------------------------


### PTT 2007-12 Unigram/Bigram  :id=ptt-bigram-freq

- Retrieved: 2020-06-04
- PTT 語料庫 2007-2012 各年之 Unigram/Bigram 頻率資料
- [`/LOPERs/廖永賦/PTT/PTT2007-2012_unigram_bigram_freq.zip`](https://drive.google.com/file/d/1sbrwwla7V9VjZXG-qTX_zcqxp5xehU-j)


#### 資料格式 :id=ptt-bigram-freq-format

##### *_unigrams.json

```json
{
    "昨天": 1506,
    "老公": 1154,
    "晚上": 3277, 
    ...
}
```

##### *_bigrams_trie.jsonl`

每行是一個 2-element JSON Array `[ <Word1>, <Word2> ]`，`<Word1>` 是 `str`，`<Word2>` 是 `dict`：

```json
[ "昨天", { "老公": 2, "是": 32, "晚上": 122, "三讀通過": 1, ... } ]
```

上方的資料表達的資訊為： `昨天老公`出現 2 次、`昨天是`出現 32 次、`昨天晚上` 出現 122 次、`昨天三讀通過` 出現 1 次、...



#### 資料讀取  :id=ptt-bigram-freq-read


##### *_unigrams.json

```python
import json
with open('2007_unigrams.json', encoding='utf-8') as f:
    unigram_freq = json.load(f)
```

##### *_bigrams_trie.jsonl

```python
import json

bigrams = {}
with open('2007_bigrams_trie.jsonl', encoding='utf-8') as f:
    for line in f:
        w1, w2_dict = json.loads(line)
        bigrams[w1] = w2_dict
```

```python
>>> bigrams['昨天']['晚上']
122
```


#### 資料來源與處理簡述

由 LOPE 125 Server `/hdd/ptt_data/ptt_json_rawdata/{BOARD}/{YEAR}*.vrt` 取得斷詞後之語料，計算 unigram 以及 bigram 頻率

<details>
<summary>(資料處理程式碼)</summary>

```python
# vrt2Bigrams.py
import os
import pathlib
import json
from functools import reduce
from bs4 import BeautifulSoup
from nltk import bigrams

def main():
    YEARS =  [2007, 2008, 2009, 2010, 2011, 2012]
    cwd = pathlib.Path(".")
    ptt = pathlib.Path("/hdd/ptt_data/ptt_json_rawdata")
    
    # Convert to bigrams
    for YEAR in YEARS:
        Bigrams = {}

        for fp in ptt.rglob(f"*/{YEAR}/*.vrt"):

            post = vrt2tokens(fp)
            for sent in post:
                
                # Count bigram
                for w1, w2 in bigrams(sent):
                    if w1 not in Bigrams:
                        Bigrams[w1] = {}
                    
                    if w2 not in Bigrams[w1]:
                        Bigrams[w1][w2] = {
                            'freq': 1,
                            'disp': {fp.stem}
                        }
                    else:
                        Bigrams[w1][w2]['freq'] += 1
                        Bigrams[w1][w2]['disp'].add(fp.stem)

            # Write file source log
            with open(f"post_src_{YEARS[0]}-{YEARS[-1]}.log", "a") as f:
                f.write(str(fp))
                f.write('\n')
    
        # Convert docnames to dispersion
        for w1 in Bigrams:
            for w2 in Bigrams[w1]:
                Bigrams[w1][w2]['disp'] = len(Bigrams[w1][w2]['disp'])

        # Save yearly data
        with open(f"{YEAR}_bigrams_trie.json", "w") as f:
            json.dump(Bigrams, f, ensure_ascii=False)

def vrt2tokens(fp):
    with open(fp) as f:
        data = f.read()

    # Extract body & comments
    soup = BeautifulSoup(data, 'lxml')
    body = soup.find(type="body").text.split('\n')
    comments = [tag.text.split('\n') for tag in soup.find_all(type="comment")]
    comments = reduce(lambda x, y: x + ['NEWLINE\tNEWLINE'] +  y, comments, [])

    # Convert to tokens
    post = []
    sent = []
    for tk_tag in body +  ['NEWLINE\tNEWLINE'] + comments:
        if tk_tag != 'NEWLINE\tNEWLINE':
            tk = tk_tag.split('\t')[0]
            if tk != '':
                sent.append(tk)
        else:
            if len(sent) != 0:
                post.append(sent)
                sent = []
    
    return post

if __name__ == "__main__":
    main()
```

</details>


### ASBC Unigram/Bigram  :id=asbc-bigram-freq

Version 5.0  
ASBC 之 Unigram/Bigram 頻率資料  
[`/LOPERs/G1.Language.Resources/ASBC.5.0/ASBC_unigram_bigram_freq.zip`](https://drive.google.com/file/d/1A_mpBlahG_m3REXpIOwG0aUHqVReuoQj)  


#### 資料格式

同 [PTT Unigram/Bigram](#ptt-bigram-freq-format)


#### 資料讀取

同 [PTT Unigram/Bigram](#ptt-bigram-freq-read)



Collocation
------------------------------


### ASBC & PTT 2007-12

ASBC 與 PTT 之_特定單字詞_ (CLD 與 DeepLex 交集) bigram association measures  
[`/LOPERs/廖永賦/PTT/ASBC_PTT2007-2012_seed_collocates.zip`](https://drive.google.com/file/d/1MfKrbY3Qw6mgTsiUfUu-mW2mBRt7RUHe)  


#### 資料格式

- `.tsv`

| w1 | w2 | MI | MI3 | MI_logf | t | Dice | logDice | deltaP21 | deltaP12 | src | seg_error |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 我 | 十六 | -0.1900 | 3.8100 | -0.3058 | -0.2636 | 0.0000 | -0.7011 | 0.0000 | 0.0188 | PTT2010 | FALSE |
| 但見 | 了 | 3.4262 | 7.4262 | 5.5142 | 5.9472 | 0.0000 | -1.1876 | 0.1344 | -0.0140 | PTT2012 | FALSE |
| 並 | 參加 | 0.9444 | 8.1143 | 2.4222 | 2.3082 | 0.0010 | 4.0637 | 0.0003 | 0.0037 | ASBC | FALSE |
| 我 | 知 | -1.4650 | 9.1058 | -5.4044 | -6.6178 | 0.0002 | 1.4788 | -0.0002 | 0.0073 | PTT2012 | TRUE |
| 郁凱 | 也 | 2.1309 | 10.4707 | 6.2742 | 6.8517 | 0.0004 | 2.6542 | 0.0261 | -0.0076 | PTT2011 | FALSE |

- Association Measures:
    - Symmetric measures: `MI`, `MI3`, `MI_logf`, `t`, `Dice`, `logDice` (based on [Statistics used in Sketch Engine](https://www.sketchengine.eu/wp-content/uploads/ske-statistics.pdf))
    - Asymmetric measures ([Gries, 2013](http://www.stgries.info/research/2013_STG_DeltaP&H_IJCL.pdf)): 
        * $$\Delta P_{2|1} = P(word_2|word_1) - P(word_2|not~word_1)$$
        * $$\Delta P_{1|2} = P(word_1|word_2) - P(word_1|not~word_2)$$


#### 資料讀取

```python
# Alternatively, see https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial
import pandas as pd
df = pd.read_csv('ASBC_PTT2007-2012_seed_collocates.tsv', sep="\t")
```


#### 資料來源與處理簡述

Association measures 由 [ASBC](#asbc-bigram-freq)/[PTT2007-12](#ptt-bigram-freq) Bigram 頻率計算而得。`seg_error` 是根據 `w1` + `w2` 是否出現在[萌典詞條](/lexical-items#萌典詞條)或[中文維基頁面標題](/lexical-items#中文維基標題)。

- 連結: [資料處理程式碼](https://github.com/lopentu/PTT_collocates)、[Model Report](https://lopentu.github.io/PTT_collocates/20200703)



$$$\Delta P_{1|2}$$$