##### data_guides (去除重複路徑)


```python
def data_guides(list_xml): # 傳入list_xml(未處理的所有標籤(深度+標籤))
    list_data_guides = []
    for x in list_xml:
        if x not in list_data_guides :
            list_data_guides.append(x)
    return list_data_guides # 回傳不重複的深度+標籤
```
