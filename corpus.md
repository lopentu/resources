語料
==============================

{docsify-updated}


未斷詞
------------------------------

### 膩結尾問句

- Retrieved: 2020-01-08
- PTT
- [`/yulin/ni_clean.csv`](https://docs.google.com/spreadsheets/d/1CNeF5teGTyzWW8nL-xvYYF4mPHNaAzKotByQNVWZg2I/edit?usp=sharing)

#### 資料格式

CSV file:

```csv
2019-11-01, Baseball, 打少棒膩？
2020-01-01, Gossiping, 你當我被騙大的膩？ 
...
```

#### 資料讀取

```R
sent <- read.csv("ni_clean.csv")
```

#### 資料來源與處理簡述

使用 PTT Corpus 的 API 取得 [PTT](https://www.ptt.cc/bbs/hotboards.html) 爬取前20大討論板中以膩為結尾的問句



已斷詞
------------------------------


### ASBC

- Version 5.0
- [No metadata](https://drive.google.com/file/d/1rPj_cLwAwnIMZvHSA9ejCgQHJPev6SRQ) (解壓後 213MB)
([Full corpus](https://drive.google.com/file/d/1yIdtvMu8vMpwhgTl9zRTL1Dj8feKEv-G)) 

#### 資料格式

[jsonlines](http://jsonlines.org): 每行是一篇文章，以 3 維的 nested JSON Array 表示：

- 第一層是文章：`[ <Sentence1>, <Sentence2>, <Sentence3>, ... ]`
- 第二層是句子：`[ <Token1>, <Token2>, <Token3>, ... ]`
- 第三層是詞彙 + PoS tag：`[ <word>, <tag> ]` 

	```json
	[
		[
			["眾院", "Nc"], ["軍事", "Na"], ["委員會", "Nc"], ["主席", "Na"], ["亞斯平", "Nb"], ["說", "VE"], ["，", "COMMACATEGORY"]
		], 
		[
			["在", "P"], ["這", "Nep"], ["場", "Nf"], ["大", "VH"], ["規模", "Na"], ["空中", "Nc"], ["攻擊", "Nv"], ["行動", "Na"], ["中", "Ng"], ["，", "COMMACATEGORY"]
		], 
		...
	]
	```
	
#### 資料讀取

將 zip 檔解壓後：
```python
import json
with open("asbc_lite.jsonl", encoding="utf-8") as f:
	corpus = [json.loads(line) for line in f]
```


### PTT 語料 (小規模)

- Retrieved: 2020-04-09
- 自 12 個板 (見下) 隨機抽取的 36000 篇 PTT 文章
- [`/LOPERs/廖永賦/PTT/sampled_PTTposts.zip`](https://drive.google.com/file/d/1iCkEOdIL02yAiY1DVOHj5fLHqaOoODzI)(97MB)


#### 資料格式

每篇文章為 `.vrt` 檔 (斷詞後之 PTT 語料格式)。`.vrt` 檔基本上是 XML 格式，可使用 `BeautifulSoup` 或其它處理 XML 的套件處理。


#### 資料讀取

```python
from bs4 import BeautifulSoup

with open('./Gossiping/M.1127637958.A.E2E.vrt') as f:
	vrt = f.read()

# Parse XML
soup = BeautifulSoup(vrt, 'lxml')

# Get elements
post = soup.find('post')
title = post.find(type='title')
content = post.find(type='body')
comments = post.find_all(type="comment")
```


#### 資料來源與處理簡述

原始資料為 Don 於 2020-04-09 爬取的 12 板 (`BabyMother`, `Boy-Girl`, `gay`, `Gossiping`, `Hate`, `HatePolitics`, `Horror`, `JapanMovie`, `joke`,`LGBT_SEX`, `NTU`, `sex`) 資料，經 PTT 語料庫的處理管線斷詞與 PoS tag。由於資料不小，先將各版的 `.vrt` (原本只有 12 個 `.vrt` 檔，一板一個) 分割成一篇文章一個 `.vrt` 檔。分割之後，再由各板隨機抽取 3000 篇文章，形成 36000 篇文章的小語料。




### Dcard

- Retrieved: 2020-02-04
- Dcard 貼文語料
- [liao961120/dcard-corpus/data/dcard.jsonl](https://github.com/liao961120/dcard-corpus/tree/master/data/dcard.jsonl) (94MB)


#### 資料格式

[jsonlines](http://jsonlines.org): 每行是一篇文章，以 JSON Object 表示。文章內文儲存在 `text` 之內 (格式為 3 維的 nested JSON Array)：

- 第一層是文章：`[ <Sentence1>, <Sentence2>, <Sentence3>, ... ]`
- 第二層是句子：`[ <Token1>, <Token2>, <Token3>, ... ]`
- 第三層是詞彙 + PoS tag：`[ <word>, <tag> ]` 

	```json
	{
		"title": "#問 Dr. Martens 1460 鞋墊", 
		"commentCount": 14, 
		"likeCount": 3, 
		"forumName": "穿搭", 
		"gender": 0, 
		"date": "2020-01-13",
		"text": [
			[
				["雖然", "Cbb"], ["知道", "VK"], ["可能", "D"], ["會", "D"], ["被", "P"], ...
			],
			[
				["我", "Nh"], ["做", "VC"], ["了", "Di"], ["很多", "Neqa"], ["功課", "Na"], ...
			],
			...
		],
	}
	```

#### 資料讀取

```python
import json
with open("dcard.jsonl", encoding="utf-8") as f:
	corpus = [json.loads(line) for line in f]
```


#### 資料來源與處理簡述

由 Dcard API 爬下之貼文 (19,224 篇)，經 [ckiplab/ckiptagger](https://github.com/ckiplab/ckiptagger) 斷詞及 PoS tag，詳見 [`liao961120/dcard-corpus`](https://github.com/liao961120/dcard-corpus)


原始資料
-------------------
### Me <資料名稱>

- Retrieved: 2017-11-29
-The corpus adopted here is collected by Brett Turner from November 29th to December 25th, 2017.
- (https://drive.google.com/drive/folders/1UIbpE21VPqREHnyjM05W5j1mRUtZ80Mz?usp=sharing)(117MB)

#### 資料格式

CSV:

```CSV
|   | text                                                                                                                                            | favorited | favoriteCount | replyToSN     | created        | truncated | replyToSID | id       | replyToUID | statusSource                                                                           | screenName     | retweetCount | isRetweet | retweeted | longitude | latitude |   |
|---|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------|---------------|----------------|-----------|------------|----------|------------|----------------------------------------------------------------------------------------|----------------|--------------|-----------|-----------|-----------|----------|---|
| 1 | American Harem.. #MeToo https://t.co/HjExLJdGuF                                                                                                 | FALSE     | 0             | NA            | 11/29/17 23:59 | FALSE     | NA         | 9.36E+17 | NA         | <a href="http://instagram.com"   rel="nofollow">Instagram</a>                          | ahmediaTV      | 0            | FALSE     | FALSE     | NA        | NA       |   |
| 2 | @johnconyersjr  @alfranken  why have you guys not resigned yet? Liberal   hypocrisy! #MeToo                                                     | FALSE     | 0             | johnconyersjr | 11/29/17 23:59 | FALSE     | NA         | 9.36E+17 | 2.66E+08   | <a href="http://twitter.com"   rel="nofollow">Twitter Web Client</a>                   | JesusPrepper74 | 0            | FALSE     | FALSE     | NA        | NA       |   |
| 3 | Watched Megan Kelly ask Joe Keery this A.M. if she can "rub my   fingers through your hair", and refer to his body be   https://t.co/Q86wfW7DeJ | FALSE     | 0             | NA            | 11/29/17 23:59 | TRUE      | NA         | 9.36E+17 | NA         | <a href="http://twitter.com/download/android"   rel="nofollow">Twitter for Android</a> | DemerisePotvin | 0            | FALSE     | FALSE     | NA        | NA       |   |
```

#### 資料讀取

```python
import pandas as pd  
import numpy as np

!pip install matplotlib
cols = ['number','text','favorited','favoriteCount','replyToSN','created','truncated','replyToSID','id','replyToUID','statusSource','screenName','retweetCount','isRetweet','retweeted','longitude','latitude']
df = pd.read_csv("metoo_tweets_dec2017.csv",header=None, names=cols,encoding = 'unicode_escape')

```

#### 資料來源與處理簡述

Metoo movement tweets collected by Brett Turner from November 29th to December 25th, 2017.
