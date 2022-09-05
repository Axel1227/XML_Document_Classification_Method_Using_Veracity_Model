##### max_depth (最大深度)


```python
def max_depth(dataguides_list): # 傳入dataguides處理後的深度+標籤
    list_depth = [] # dataguides_list的所有深度
    int_max_depth = 0 # 最大深度
    for depth in dataguides_list:
        list_depth.append(depth[0]) # 只取深度，並增加到list_depth
    int_max_depth = max(list_depth) # 取出list中最大的深度
    return int_max_depth # 回傳最大深度
```

##### xml_max_depth 計算最大深度分數


```python
def xml_max_depth(b_XML, m_XML): # 最大結構深度
    b_max_depth = b_XML
    m_max_depth = m_XML
    if b_max_depth == m_max_depth:
        score = 100
    elif b_max_depth > m_max_depth:
        score = m_max_depth / b_max_depth * 100
    else:
        score = b_max_depth / m_max_depth * 100 # _max_depth < m_max_depth
    return score
```
