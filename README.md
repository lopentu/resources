[![Build Status](https://travis-ci.org/lopentu/resources.svg?branch=master)](https://travis-ci.org/lopentu/resources)

關於
==========================

此份說明文件記錄著 [LOPE Drive](https://drive.google.com/drive/folders/0AJ9ALSFcTcxMUk9PVA) 上的資源，方便實驗室成員使用。


## 撰寫說明文件

在 LOPE Drive 中，每筆資料 (每個專案) 皆存放於一個資料夾內。如欲上傳新資料，請為此資料新增一個專案資料夾，並於此資料夾內放入一個 `LOPE_INDEX.md` (請使用 **UTF-8** 編碼)，做為此資料的說明文件。

`LOPE_INDEX.md` 的格式要求如下 (標題請由**階層二**開始增加，除第一個標題為階層二，其餘至少需為階層三)：

```md
## <資料名稱>

### Description
```

此份文件每週自動更新一次，屆時新增於 LOPE Drive 上的 `LOPE_INDEX.md` 即會更新於此。



## docsify Tips

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


## Supported Code Chunk Highlighting

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
</details>



## Developer's Notes

See `liao961120/lope-drive-docs-generator` for token info.
