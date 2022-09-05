##### 讀取xml文件目錄(基準文件B)


```python
os.chdir('/home/user/Jupyter/') #切回最原始的執行路徑

import os
b_path="b_xml_file/"
b_file_list = [n for n in os.listdir(b_path) if os.path.isfile(os.path.join(b_path, n))]
b_file_list.sort()
b_file_list 
```




    ['001_b_envi.xml',
     '002_b_meteorological.xml',
     '003_b_traffic_live.xml',
     '004_b_finance.xml',
     '005_b_medical_treatment.xml']
