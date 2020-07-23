
# 關於

LOPE Drive 有相當多的語言資源，但由於資料累積多年，時常不易找到自己需要的東西。從過去處理資料的經驗中，發現許多資源是會重複使用的。但即使將這些資源放上 LOPE Drive，在缺乏**完整的使用說明**下，自己也會忘記這些資源的存在，更別說將這些資源分享給其他人使用。

我將一些大家 (包含我自己) 可能會常常使用到的資源 (資料&程式) 整理在這裡，記錄的資訊包含：
- 存放位置
- 資料格式、使用說明 (e.g. 程式讀取說明)
- 資料來源與處理簡述
- 相關連結 (repo, 論文等)


歡迎大家將常用的程式與資料的說明放上這裡。**更新這份文件**最簡單的方式就是點選最上方的 ![Edit Document](https://github.githubassets.com/images/icons/emoji/memo.png ':class=emoji') 至 [GitHub](https://github.com) 編輯文件 (提出 Pull Request)。


---

## 文件編輯


### Style Guide

為使說明文件的格式一致，建議可以依照下方的範例作為撰寫的模板 (複製貼上再修改資訊)。說明文件上的章節編號為**自動產生**，撰寫標題時**無需加入編號**。

<details>
<summary>撰寫模板 (以一份資料為例)</summary>

````md
### 萌典詞條 <資料名稱>

- Retrieved: 2020-02-26
- 教育部萌典詞條
- [`/LOPERs/廖永賦/moe_dict/moe_lexical_items.json`](https://drive.google.com/file/d/1T_WJcWcaYVPhFWqIdAfup30-bauzxXVa)(2MB)

#### 資料格式

JSON array:

```json
["⺔", "⼁", "㑳", "㑳憋憋", "㑳擾", "㑿", "㒓", "㓦", "㓦劃", ...]
```

#### 資料讀取

```python
import json
with open("moe_lexical_items.json", encoding="utf-8") as f:
	words = json.load(f)
```

#### 資料來源與處理簡述

由 [g0v/moedict-data](https://github.com/g0v/moedict-data/blob/master/dict-revised.json) 取得原始字典檔資料 (`dict-revised.json`)，抽取每個項目的詞條 (`title`)
````

</details>


### 建立新文件

若想新增的內容無法被歸類於當前 sidebar 內的分類，可以在此 repo 的**根目錄**自行建立一份新的章節 (見下_Repo 檔案結構_)，並將此檔案連結新增至 `_sidebar.md`。

<details>
<summary>Repo 檔案結構</summary>

```bash
lopentu/resources
  ├── README.md           # 首頁 (url: /#/)
  ├── lexical-items.md    # 詞彙 (url: /#/lexical-items)
  ├── corpus.md           # 語料 (url: /#/corpus)
  ├── corpus-stats.md     # 語料衍生資料 (url: /#/corpus-stats)
  ├── scripts.md          # 常用程式 (url: /#/scripts)
  ├── _sidebar.md         # 頁面連結設定
  |                       # ==== 此線以下的檔案無需理會 ==== #
  ├── _navbar.md
  ├── index.html
  ├── js/
  └── _media/
```
</details>


例如，可以在根目錄新增 `server.md`，再至 `_sidebar.md` 新增 `* [伺服器資源](server.md)`：

```md
<!-- docs/_sidebar.md -->

- [詞彙](lexical-items.md)
- [語料](corpus.md)
- [語料衍生資料](corpus-stats.md)
- [常用程式](scripts.md)
- [伺服器資源](server.md)
```


### docsify Tips

此份說明文件使用 [docsify](https://docsify.js.org) 製作，內文是由 Markdown 寫成。**docsify** 另有提供一些擴充語法，詳見其[說明文件](https://docsify.js.org/#/helpers)。下方羅列幾個常用到的語法：

1.  <details>
    <summary>自訂 ID</summary>
    
    ```md
    ## 某標題  :id=custom-title-id

    Any text [](# ':id=custom-id-anchor')

    前往[某標題](#custom-title-id)、[Any text](#custom-id-anchor)
    ```

    ## 某標題  :id=custom-title-id

    Any text [](# ':id=custom-id-anchor')

    前往[某標題](#custom-title-id)、[Any text](#custom-id-anchor)

    </details>
1.  <details>
    <summary>Cross Reference</summary>
    
    - `corpus-stats.md`  
    ```md
    ## PTT 2007-12 Unigram/Bigram  :id=ptt-bigram-freq
    ```

    - `<Any-other-file>.md`  
    ```md
    前往[PTT 2007-12 Unigram/Bigram](/corpus-stats#ptt-bigram-freq)
    ```

        前往 [PTT 2007-12 Unigram/Bigram](/corpus-stats#ptt-bigram-freq)
    </details>
1.  <details>
    <summary>Ignore Section Title on Sidebar</summary>

    ```md
    ## This title is shown on the sidebar

    ### This one is not {docsify-ignore}
    ```
    </details>


### Supported Code Chunk Highlighting

此文件的 code chunk 支援以下語法的 syntax highlight：

|      Language      |       Alias      |
|:------------------:|:----------------:|
|     JavaScript     | `javascript` `js`|
|       Python       |     `python`     |
|        Shell       |      `bash`      |
|          R         |        `r`       |
|      Markdown      | `markdown` `md`  |
| Regular Expression |      `regex`     |



<details>
<summary>Code chunk syntax highlight example</summary>

````md
##### A chunk of Python code

This is **Markdown** content.

```python
# This is python code
name = "Liao"
print(f"Hello, {name}!")
```
````

##### A chunk of Python code

This is **Markdown** content.

```python
# This is python code
name = "Liao"
print(f"Hello, {name}!")
```

---
</details>





---

## Developer's Notes

Preview the site locally:

```bash
# cd to root
python3 -m http.server
```


<!-- 
<style>
/* Close Auto-numbering */
h2:before, h3:before {
	content: "";
	padding-right: 0;
}
</style>
-->