##### tag_count (計算標籤出現次數)


```python
def tag_count(list_xml): # 傳入list_xml(未處理的所有標籤(深度+標籤))
    string_tag = ""
    dict_tag_count = {}
    dict_tag = {}
    for i in list_xml:
        string_tag += i[1] + "," # 只取標籤，並用逗號區隔(string) (ex:A,B,C...)
    dict_tag = string_tag.split(",")  # 將標籤用逗號區隔轉為dict (ex:A:0,B:0,C:0...)
    for j in dict_tag: # 跑dict
        dict_tag_count[j] = dict_tag.count(j)  # 得到該詞出現次數
    return dict_tag_count # # 回傳不重複的標籤+數量
```

##### tag_sum (計算標籤總數量)


```python
def tag_sum(dict_tag_count):  # 傳入tag_count (計算標籤出現次數)
    int_tag_sum = 0
    for i in dict_tag_count: 
        int_tag_sum += dict_tag_count[i] # 計算所有dict的value總和
    return int_tag_sum # 回傳標籤總數量
```
##### xml_total_tags 計算標籤總數量分數


```python
def xml_total_tags(b_XML, m_XML):
    b_total_tags = b_XML
    m_total_tags = m_XML
    if b_total_tags == m_total_tags:
        score = 100
    elif b_total_tags > m_total_tags:
        score = m_total_tags / b_total_tags * 100
    else:
        score = b_total_tags / m_total_tags * 100 #  b_total_tags < m_total_tags
    return score
```
