##### tf (計算單詞TF值)


```python
def tf(dict_tag_count, int_tag_sum): # 傳入tag_count (計算標籤出現次數) 與 tag_sum (計算標籤總數量)
    import math
    dict_tag_tf = {} # TF值
    for dict_tag_key, dict_tag_value in dict_tag_count.items(): # 跑該dict的key與value
        dict_tag_tf[dict_tag_key] = math.floor((dict_tag_value/float(int_tag_sum))*100)/100.0 # 該詞出現次數/總單詞數量(無條件捨去)
    dict_tag_tf_value = {i:j for i, j in dict_tag_tf.items() if j>=0.01} 
    return dict_tag_tf_value # 回傳標籤+TF值 (值越大表示該詞出現次數多(越重要))
```

##### idf (計算單詞idf值)


```python
def idf(dict_tag_sum): # 傳入dict_tag_sum取得文件的所有標籤與標籤數量(累加)
    import math
    dict_tag_idf_value = {}
    Q = m_file_count # 量測文件數量
    dict_tag_idf_value = dict.fromkeys(dict_tag_sum[0].keys(), 0) # 所有文件dict[key、val]，預設val為0    (文件標籤出現數量，val直接給予0)
    for doc in dict_tag_sum: # 迴圈次數為總文件數量
        for dict_tag_key, dict_tag_value in doc.items(): # 迴圈跑該總文件的key、val
            if dict_tag_value > 0: # 當該詞沒在該文件出現時則跳過
                dict_tag_idf_value[dict_tag_key] += 1 # 當該詞在文件中出現時+1(文件數量)
    for dict_tag_key, dict_tag_value in dict_tag_idf_value.items(): # key(詞)與val(文件數量)
        #dict_tag_idf_value[dict_tag_key] = math.log10(Q / float(dict_tag_value)) # 總文件數量/該詞在多少文件出現數量
        #dict_tag_idf_value[dict_tag_key] = math.floor(math.log10(Q / float(dict_tag_value))*100)/100.0 # 總文件數量/該詞在多少文件出現數量(無條件捨去) 
        dict_tag_idf_value[dict_tag_key] = math.floor(math.log10(Q+1 / (float(dict_tag_value)+1))*100)/100.0 # 總文件數量/該詞在多少文件出現數量(無條件捨去) 
        #print(dict_tag_value)
    return dict_tag_idf_value # 回傳標籤+idf值(值越小表示該詞出現篇數越少(表示該詞具代表意義))
```

##### tf_idf(計算tf_idf值)


```python
def tf_idf(dict_tag_tf_value, dict_tag_idf_value): # 傳入tf(計算單詞TF值) 與 idf (計算單詞idf值)
    import math
    dict_tf_idf_value = {}
    for dict_tag_key, dict_tag_value in dict_tag_tf_value.items():
        dict_tf_idf_value[dict_tag_key] = math.floor(float(dict_tag_value*dict_tag_idf_value[dict_tag_key])*100)/100.0
    return dict_tf_idf_value # 回傳標籤+tf-idf值
```

##### tfidf_score 計算tfidf分數


```python
def tfidf_score(compare_tfidf_result, b_list_tag_all): 
    compare_tfidf_result_number = len(compare_tfidf_result)
    b_list_tag_all_number = len(b_list_tag_all)
    if compare_tfidf_result_number == b_list_tag_all_number:
        score = 100
    else:
        score = compare_tfidf_result_number / b_list_tag_all_number * 100
    return score
```
