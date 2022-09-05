##### list_attrib 得到文件的所有的屬性


```python
# 1. 傳入該份文件所有內容
# 2. 將list內容轉為字串
# 3. 透過3.4只取得屬性內容
# 4. 取出字串中的{的下一個index(+1)
# 5. 取出字串中的}
# 6. 透過2.3.取得的index找到1.中的屬性內容
# 7. 將屬性內容放入list
# 8. 得到該份文件的所有屬性
# 註 該方法都一定會傳{}，所以不用判斷是否存在
def list_attrib(list_attrib):
    string_attrib_result = ""
    for attrib in list_attrib:
        string_attrib = str(attrib)
        attrib_a = string_attrib.index("{")
        attrib_a += 1
        attrib_b = string_attrib.index("}")
        string_attrib_result += string_attrib[attrib_a:attrib_b] + ","
    list_attrib_result =list(string_attrib_result.split(","))
    return list_attrib_result
```

##### set_attrib 得到文件的不重複的屬性


```python
# 1. 傳入該份文件所有內容
# 2. 將list內容轉為字串
# 3. 透過3.4只取得屬性內容
# 4. 取出字串中的{的下一個index(+1)
# 5. 取出字串中的}
# 6. 透過2.3.取得的index找到1.中的屬性內容
# 7. 將屬性內容放入list
# 8. 得到該份文件的所有屬性
# 9. 轉為set去除重複屬性
# 註 該方法都一定會傳{}，所以不用判斷是否存在
def set_attrib(list_attrib):
    string_attrib_result = ""
    for attrib in list_attrib:
        string_attrib = str(attrib)
        attrib_a = string_attrib.index("{")
        attrib_a += 1
        attrib_b = string_attrib.index("}")
        string_attrib_result += string_attrib[attrib_a:attrib_b] + ","
    set_attrib_result = set(list(string_attrib_result.split(",")))
    return set_attrib_result
```

##### same_attrib 計算相同屬性


```python
def same_attrib(b_set_attrib, m_set_attrib):
    set_attrib_b = set(b_set_attrib)
    set_attrib_m = set(m_set_attrib)
    dict_same_attrib = set_attrib_m.intersection(set_attrib_b)
    return dict_same_attrib
```

##### attrib_number 計算dict key的屬性數量


```python
def attrib_number(dict_attrib): # 傳入 dict 的所有key attrib
    number = 0
    for i in dict_attrib:
        number += 1
    return number # # 回傳屬性(key)數量
```

##### smae_attrib_score 計算相同屬性數量分數


```python
def smae_attrib_score(int_same_attrib, b_int_attrib): # 傳入相同屬性數量, 基準文件屬性總數量
    if int_same_attrib == b_int_attrib:
        score = 100
    else:
        score = int_same_attrib / b_int_attrib * 100 # _max_depth < m_max_depth
    return score # 回傳相同屬性分數
```
