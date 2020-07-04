# 詞彙資源

{docsify-updated}


## 詞表 :id=word-list


### 批踢踢詞彙

Retrieved: 2018-11-07  
鄉民百科爬下來的 PTT 詞彙  
[`/LOPERs/廖永賦/PTT/ptt_terms.csv`](https://raw.githubusercontent.com/liao961120/lang-resource/master/raw-data/ptt_lexical_items/ptt_terms.csv)  
[`/LOPERs/廖永賦/PTT/ptt_terms-has_chinese.txt`](https://github.com/liao961120/lang-resource/blob/master/lexical_items/ptt_terms-has_chinese.txt)  
[`/LOPERs/廖永賦/PTT/ptt_terms-all_chinese.txt`](https://github.com/liao961120/lang-resource/blob/master/lexical_items/ptt_terms-all_chinese.txt)

- **資料格式**
	- `ptt_terms.csv`: 2-column (_term_, _src_) csv
	- `ptt_terms-has_chinese.txt`: 一行一個詞條
	- `ptt_terms-all_chinese.txt`: 一行一個詞條
- **資料讀取**
	```python
	# ptt_terms.csv (Alternatively, https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial)
	import pandas as pd
	df = pd.read_csv('ptt_terms.csv')

	# ptt_terms-has_chinese.txt & ptt_terms-all_chinese.txt
	with open('ptt_terms-all_chinese.txt', encoding="utf-8") as f:
		words = [line.strip() for line in f]
	```
- **資料來源與處理簡述**  
	`ptt_terms.csv` 為鄉民百科爬下來的資料，詳見 [yongfu.name/PTT-scrapy](https://yongfu.name/PTT-scrapy)  
	`*-has_chinese.txt` 與 `*-all_chinese.txt` 為自 `ptt_terms.csv` 篩選過的資料 ([程式碼](https://github.com/liao961120/lang-resource/blob/master/raw-data/ptt_lexical_items/))：
	- `ptt_terms-has_chinese.txt`: **含有**中文字的詞條
	- `ptt_terms-all_chinese.txt`: **全為**中文字的詞條


### 中文維基標題

Retrieved: 2020-06-20  
中文維基百科所有頁面標題  
[`/LOPERs/廖永賦/wiki/zhwiki-20200620-titles-has_chinese.txt`](https://drive.google.com/file/d/1vtDRXJCcENj3acuXXcbFDjjDXBtFrp4p)(49MB)  
[`/LOPERs/廖永賦/wiki/zhwiki-20200620-titles-all_chinese.txt`](https://drive.google.com/file/d/1TTzRWuP6dF0EqjeMkJrr3TRDQcB1Jey_)(28MB)


- **資料格式**: 一行一個詞條
	```txt
	孫中台
	金屬磷屬氧化物
	龙泉市
	...
	```
- **資料讀取**
	```python
	with open('zhwiki-20200620-titles-has_chinese.txt', encoding="utf-8") as f:
		words = [line.strip() for line in f]
	```
- **資料來源與處理簡述**  
	由 [Wikipedia 提供](https://zh.wikipedia.org/wiki/Wikipedia:数据库下载)之所有[頁面標題資料](https://dumps.wikimedia.org/zhwiki/20200620/zhwiki-20200620-all-titles.gz)。經處理篩選出**含有** (`*-has_chinese.txt`) 或**皆為** (`*-all_chinese.txt`) 中文字的標題([程式碼](https://github.com/liao961120/lang-resource/tree/master/raw-data/wiki-pagetitle))


### 萌典詞條 

Retrieved: 2020-02-26  
教育部萌典詞條  
[`/LOPERs/廖永賦/moe_dict/moe_lexical_items.json`](https://drive.google.com/file/d/1T_WJcWcaYVPhFWqIdAfup30-bauzxXVa)(2MB)

- **資料格式**：JSON array
	```json
	["⺔", "⼁", "㑳", "㑳憋憋", "㑳擾", "㑿", "㒓", "㓦", "㓦劃", ...]
	```
- **資料讀取**
	```python
	import json
	with open("moe_lexical_items.json", encoding="utf-8") as f:
		words = json.load(f)
	```
- **資料來源與處理簡述**  
	由 [g0v/moedict-data](https://github.com/g0v/moedict-data/blob/master/dict-revised.json) 取得原始字典檔資料 (`dict-revised.json`)，抽取每個項目的詞條 (`title`)


## 字典

### 萌典

Retrieved: 2020-02-26  
教育部萌典 (含詞條、釋義、部首、筆劃、注音、拼音等)  
[`/LOPERs/廖永賦/moe_dict/moe.json`](https://drive.google.com/file/d/1H-wXEWC0Tgz8GE3kmc9vZV0WfuiqiGmV/view?usp=sharing)(72MB)

- **資料讀取**
	```python
	import json
	with open("moe.json", encoding="utf-8") as f:
		moe_dict = json.load(f)
	```
- **資料來源與處理簡述**  
	使用原始資料，未處理：[`g0v/moedict-data/dict-revised.json`](https://github.com/g0v/moedict-data/blob/master/dict-revised.json)

