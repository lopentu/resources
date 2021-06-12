# /LOPERs/廖永賦


<a href='https://drive.google.com/drive/folders/18xNeYO8IVJWn2NJUPdGQ6XimrGDAiAiA' target='_blank' class='drive-location'><code>/LOPERs/廖永賦/Dcard_data</code></a>

## Dcard

### Description

- Retrieved: 2020-02-04
- Dcard 貼文語料
- [GitHub: liao961120/dcard-corpus/data/dcard.jsonl](https://github.com/liao961120/dcard-corpus/tree/master/data/dcard.jsonl) (94MB)



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
