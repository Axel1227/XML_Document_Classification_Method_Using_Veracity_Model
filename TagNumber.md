##### tag_all (取得所有標籤)


```python
def tag_all(list_xml): # 傳入list_xml(未處理的所有標籤(深度+標籤))
    string_tag_all = ""
    dict_tag_count = {}
    for i in list_xml:
        string_tag_all += i[1] + "," # 只取標籤，並用逗號區隔(string) (ex:A,B,C...)
    return string_tag_all # # 回傳不重複的標籤
```
##### same_tag (計算相同標籤)    


```python
def same_tag(b_list_tag_all, m_list_tag_all): #傳入
    set_tag_b = set(b_list_tag_all)   
    set_tag_m = set(m_list_tag_all)
    dict_same_tag_tag = set_tag_m.intersection(set_tag_b)
    return dict_same_tag_tag
```



##### tag_number 計算dict key的標籤數量


```python
def tag_number(dict_tag): # 傳入 dict 的所有key tag
    number = 0
    for i in dict_tag:
        number += 1
    return number # # 回傳標籤(key)數量
```



##### smae_tag_score 計算相同標籤數量分數


```python
def smae_tag_score(dict_same_tag, b_list_tag_all): # 傳入相同標籤數量, 基準文件標籤總數量
    if dict_same_tag == b_list_tag_all:
        score = 100
    else:
        score = dict_same_tag / b_list_tag_all * 100 
    return score # 回傳相同標籤分數
```
