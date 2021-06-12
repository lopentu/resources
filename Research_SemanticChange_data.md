# /Research/SemanticChange/data


<a href='https://drive.google.com/drive/folders/11ln53rubBG1BT2GmvhFzDcb-FSSEIUVP' target='_blank' class='drive-location'><code>/Research/SemanticChange/data/ctext</code></a>

## **`meta/`**

</br>

1. `all_urns.json`: (32123 entries) all urns retrieved from [gettexttitles api](https://api.ctext.org/gettexttitles?if=zh)

    - `all_book_urns.json`: (139 entries) all book urns in urns_all.json
    - `all_wiki_urns.json`: (31984 entries) all wiki urns in urns_all.json

    ```python
    [
        {
            "title": "墨子",
            "urn": "ctp:mozi"
        },
          {
            "title": "論語",
            "urn": "ctp:analects"
        },
        ...
    ]
    ```

1. `wiki_select_urns.json`: (320 entries) wiki urns retrieved on [維基 > 原典精選](https://ctext.org/wiki.pl?if=gb)

    ```python
    [
        "ctp:wb153836",
        "ctp:wb143901",
        "ctp:wb563355",
        "ctp:wb847447",
        "ctp:wb957942",
        ...
    ]
    ```

1. `dynasties.json`: (26 dynasties) dynasties info retrieved from [getdynasties api](https://api.ctext.org/getdynasties)

    ```python
    {
        "dynasties": [
            {
                "id": "1",
                "title": "Western Zhou",
                "yearfrom": "-1046",
                "yearto": "-771"
            },
            {
                "id": "27",
                "title": "Zhou",
                "yearfrom": "-1046",
                "yearto": "-221"
            },
            ...
        ]
    }
    ```

---

## **`data/`**

</br>

1. Meta of folders under `data/`:

    folder | number of entries | retrieved via
    ---------|----------|---------
    **`book/`** | 139 (complete) | ctext
    **`book_R/`** | 94 | ctextclassics
    **`wiki/`** | 13984 (complete) | ctext
    **`wiki_select/`** | 320 | ctext

    <br/>

    > * [Official Python wrapper - ctext](https://pypi.org/project/ctext/)
    > * [R library - ctextclassics](https://www.r-bloggers.com/ctextclassics-my-first-package/)
    
1. Content of folders under `data/` include:

    folder/file | content
    ---------|----------
    **`text/`**`text_<index>_<ctp>_<title>.json` | individual text files
    **`textinfo/`**`textinfo_<index>_<ctp>_<title>.json` | individual textinfo files
    `textinfo_all.json` | - a file of all textinfo </br> - in a list of nested dictionaries
    `textinfo_all_flatten.csv` | - a file of all textinfo </br> - flatten into a table
    `textinfo_all_flatten_TEXTDB_removed.csv` | - a file of all textinfo </br> - flatten into a table </br> - The tag TEXTDB is **not** allowed for wiki entries and removed accordingly.

    with the following exceptions marked with _X_:

    folder/file | **`book/`** | **`book_R/`** | **`wiki/`** | **`wiki_select/`**
    ---------|----------|----------|----------|----------
    **`text/`**`text_<index>_<ctp>_<title>.json` |
    **`textinfo/`**`textinfo_<index>_<ctp>_<title>.json` ||_X_|_X_
    `textinfo_all.json` ||_X_
    `textinfo_all_flatten.csv` ||_X_||_X_
    `textinfo_all_flatten_TEXTDB_removed.csv` |_X_|_X_||_X_

    </br>

    ```python
    # textinfo_all.json
    [
        {
            "index": 0,
            "textinfo": ...
        },
        {
            "index": 1,
            "textinfo": ...
        },
        ...
    ]
    ```

    ```python
    # headers in textinfo_all_flatten.csv
        ,
        index,
        textinfo_dynasty_from_id,
        textinfo_dynasty_from_name,
        textinfo_dynasty_to_id,
        textinfo_dynasty_to_name,
        textinfo_lastmodified,
        textinfo_title,
        textinfo_toptitle,
        textinfo_topurn,
        textinfo_author,
        textinfo_edition_collectionid,
        textinfo_edition_description,
        textinfo_edition_title,textinfo_edition_url,
        textinfo_tags,
        textinfo_tags_string
    ```