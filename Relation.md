##### tag_relation 計算祖先、父子、孫子標籤 (相同深度放在同一個liist)


```python
# 1. 傳入list_深度+標籤
# 2. 依照傳入的list長度作為最後放結果指定的list長度
# 3. for迴圈跑當前深度+標籤
# 4. 當前深度與最大深度比較，相同當前的list增加該標籤，不相同則下一個的list位置增加標籤
# 5. 更新最大深度
# 6. return list 相同深度的會在同一個內

def tag_relation(list_dempth_tag): # 傳入list_深度+標籤
    list_length = len(list_dempth_tag) # 傳入的list長度
    int_dempth = 0 # 當前深度
    max_dempth = 0 # 最大深度
    list_tag = [[] for i in range(list_length)] # 標籤結果
    int_tag = -1 # 當前深度
    for i in list_dempth_tag:
        int_dempth = int(i[0]) # 當前深度
        string_tag = i[1] # 當前深度的標籤        
        if max_dempth == int_dempth: # 深度相同
            list_tag[int_tag].append(string_tag) #當前list增加標籤
        else: # 深度不同時
            int_tag += 1 # 下一個list位置
            list_tag[int_tag].append(string_tag) # 增加標籤
        max_dempth = int_dempth # 更新最大深度
    return list_tag # 回傳祖先、父子、孫子標籤(相同深度放在同一個list)
```

##### tag_relation_score 計算祖先、父子、孫子標籤關係分數


```python
# 1. 傳入b_基準 與 m_量測 的祖先、父子、孫子標籤(相同深度放在同一個list)
# 2. 取得相同的祖先、父子、孫子關係
# 3. 將相同的祖先、父子、孫子關係計算相同數量
# 4. 計算分數

def tag_relation_score(b_list_tag_all, m_list_tag_all): #傳入b_基準 與 m_量測 的標籤 (祖先、父子、孫子關係)
    b_list_length = int(len(b_list_tag_all)) # 基準文件list長度
    m_list_length = int(len(m_list_tag_all)) # 基準文件list長度
    list_result = [] # 存放結果
    # b_基準 與 m_量測 跑最小長度
    check_length = 0 
    if b_list_length > m_list_length:
        check_length = m_list_length
    else:
        check_length = b_list_length
    # 1. 取得相同的祖先、父子、孫子關係
    for i in range(check_length): # 跑list長度    
        set_tag_b = set(b_list_tag_all[i]) # 轉為set 
        set_tag_m = set(m_list_tag_all[i]) # 轉為set
        dict_same_tag_tag = set_tag_m.intersection(set_tag_b) # 取出當前list(set)相同的標籤
        list_result.append(list(dict_same_tag_tag)) # 轉換為list增加至list_result
    # print(list_result) # 相同的祖先、父子、孫子關係
    # 2. 計算相同祖先、父子、孫子關係
    int_number = -1 # list_result位置暫存
    int_number_result = 0 # 相同祖先、父子、孫子節點數量
    for j in range(check_length): # 跑b_基準list長度
        int_number += 1 # list_result 每次近來前先+1
        now_number = int(len(list_result[int_number])) # 取得當前list長度，若無祖先、父子、孫子相同關係，則為0
        if now_number != 0: # 判斷當前list是否有相同的祖先、父子、孫子關係
            int_number_result += now_number # 若成立，則將相同祖先、父子、孫子相同關係數量增加到int_number_result
    # print(int_number_result) # 相同的祖先、父子、孫子數量
    # 3. 計算b_基準與相同祖先、父子、孫子節點分數
    if b_list_length == int_number_result:
        score = 100
    else:
        score = int_number_result / b_list_length * 100
    return score # 回傳相同的祖先、父子、孫子相同關係數量
```


```python

```


```python
#m_xml_file_path = '/home/user/Jupyter/m_xml_file_zero/' # 0%雜訊
#m_xml_file_path = '/home/user/Jupyter/m_xml_file_ten/' # 10%雜訊
m_xml_file_path = '/home/user/Jupyter/m_xml_file_twenty/' #20%雜訊
```
