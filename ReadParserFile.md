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

##### 讀取xml文件目錄(量測文件M)


```python
import os
# 量測文件讀取
#m_path="m_xml_file_zero/" # 0%雜訓
#m_path = 'm_xml_file_ten/' # 10%雜訊
m_path = 'm_xml_file_twenty/' #20%雜訊

m_file_list = [n for n in os.listdir(m_path) if os.path.isfile(os.path.join(m_path, n))]
m_file_list.sort()
m_file_list
```




    ['101_m_envi_twenty.xml',
     '102_m_envi_twenty.xml',
     '103_m_envi_twenty.xml',
     '104_m_envi_twenty.xml',
     '105_m_envi_twenty.xml',
     '106_m_envi_twenty.xml',
     '107_m_envi_twenty.xml',
     '108_m_envi_twenty.xml',
     '109_m_envi_twenty.xml',
     '110_m_envi_twenty.xml',
     '111_m_envi_twenty.xml',
     '112_m_envi_twenty.xml',
     '113_m_envi_twenty.xml',
     '114_m_envi_twenty.xml',
     '115_m_envi_twenty.xml',
     '116_m_envi_twenty.xml',
     '117_m_envi_twenty.xml',
     '118_m_envi_twenty.xml',
     '119_m_envi_twenty.xml',
     '120_m_envi_twenty.xml',
     '121_m_envi_twenty.xml',
     '122_m_envi_twenty.xml',
     '123_m_envi_twenty.xml',
     '124_m_envi_twenty.xml',
     '125_m_envi_twenty.xml',
     '126_m_envi_twenty.xml',
     '127_m_envi_twenty.xml',
     '128_m_envi_twenty.xml',
     '129_m_envi_twenty.xml',
     '130_m_envi_twenty.xml',
     '131_m_envi_twenty.xml',
     '132_m_envi_twenty.xml',
     '133_m_envi_twenty.xml',
     '134_m_envi_twenty.xml',
     '135_m_envi_twenty.xml',
     '136_m_envi_twenty.xml',
     '137_m_envi_twenty.xml',
     '138_m_envi_twenty.xml',
     '139_m_envi_twenty.xml',
     '140_m_envi_twenty.xml',
     '141_m_envi_twenty.xml',
     '142_m_envi_twenty.xml',
     '143_m_envi_twenty.xml',
     '144_m_envi_twenty.xml',
     '145_m_envi_twenty.xml',
     '146_m_envi_twenty.xml',
     '147_m_envi_twenty.xml',
     '148_m_envi_twenty.xml',
     '149_m_envi_twenty.xml',
     '150_m_envi_twenty.xml',
     '251_m_meteorological_twenty.xml',
     '252_m_meteorological_twenty.xml',
     '253_m_meteorological_twenty.xml',
     '254_m_meteorological_twenty.xml',
     '255_m_meteorological_twenty.xml',
     '256_m_meteorological_twenty.xml',
     '257_m_meteorological_twenty.xml',
     '258_m_meteorological_twenty.xml',
     '259_m_meteorological_twenty.xml',
     '260_m_meteorological_twenty.xml',
     '261_m_meteorological_twenty.xml',
     '262_m_meteorological_twenty.xml',
     '263_m_meteorological_twenty.xml',
     '264_m_meteorological_twenty.xml',
     '265_m_meteorological_twenty.xml',
     '266_m_meteorological_twenty.xml',
     '267_m_meteorological_twenty.xml',
     '268_m_meteorological_twenty.xml',
     '269_m_meteorological_twenty.xml',
     '270_m_meteorological_twenty.xml',
     '271_m_meteorological_twenty.xml',
     '272_m_meteorological_twenty.xml',
     '273_m_meteorological_twenty.xml',
     '274_m_meteorological_twenty.xml',
     '275_m_meteorological_twenty.xml',
     '276_m_meteorological_twenty.xml',
     '277_m_meteorological_twenty.xml',
     '278_m_meteorological_twenty.xml',
     '279_m_meteorological_twenty.xml',
     '280_m_meteorological_twenty.xml',
     '281_m_meteorological_twenty.xml',
     '282_m_meteorological_twenty.xml',
     '283_m_meteorological_twenty.xml',
     '284_m_meteorological_twenty.xml',
     '285_m_meteorological_twenty.xml',
     '286_m_meteorological_twenty.xml',
     '287_m_meteorological_twenty.xml',
     '288_m_meteorological_twenty.xml',
     '289_m_meteorological_twenty.xml',
     '290_m_meteorological_twenty.xml',
     '291_m_meteorological_twenty.xml',
     '292_m_meteorological_twenty.xml',
     '293_m_meteorological_twenty.xml',
     '294_m_meteorological_twenty.xml',
     '295_m_meteorological_twenty.xml',
     '296_m_meteorological_twenty.xml',
     '297_m_meteorological_twenty.xml',
     '298_m_meteorological_twenty.xml',
     '299_m_meteorological_twenty.xml',
     '300_m_meteorological_twenty.xml',
     '401_m_traffic_live_twenty.xml',
     '402_m_traffic_live_twenty.xml',
     '403_m_traffic_live_twenty.xml',
     '404_m_traffic_live_twenty.xml',
     '405_m_traffic_live_twenty.xml',
     '406_m_traffic_live_twenty.xml',
     '407_m_traffic_live_twenty.xml',
     '408_m_traffic_live_twenty.xml',
     '409_m_traffic_live_twenty.xml',
     '410_m_traffic_live_twenty.xml',
     '411_m_traffic_live_twenty.xml',
     '412_m_traffic_live_twenty.xml',
     '413_m_traffic_live_twenty.xml',
     '414_m_traffic_live_twenty.xml',
     '415_m_traffic_live_twenty.xml',
     '416_m_traffic_live_twenty.xml',
     '417_m_traffic_live_twenty.xml',
     '418_m_traffic_live_twenty.xml',
     '419_m_traffic_live_twenty.xml',
     '420_m_traffic_live_twenty.xml',
     '421_m_traffic_live_twenty.xml',
     '422_m_traffic_live_twenty.xml',
     '423_m_traffic_live_twenty.xml',
     '424_m_traffic_live_twenty.xml',
     '425_m_traffic_live_twenty.xml',
     '426_m_traffic_live_twenty.xml',
     '427_m_traffic_live_twenty.xml',
     '428_m_traffic_live_twenty.xml',
     '429_m_traffic_live_twenty.xml',
     '430_m_traffic_live_twenty.xml',
     '431_m_traffic_live_twenty.xml',
     '432_m_traffic_live_twenty.xml',
     '433_m_traffic_live_twenty.xml',
     '434_m_traffic_live_twenty.xml',
     '435_m_traffic_live_twenty.xml',
     '436_m_traffic_live_twenty.xml',
     '437_m_traffic_live_twenty.xml',
     '438_m_traffic_live_twenty.xml',
     '439_m_traffic_live_twenty.xml',
     '440_m_traffic_live_twenty.xml',
     '441_m_traffic_live_twenty.xml',
     '442_m_traffic_live_twenty.xml',
     '443_m_traffic_live_twenty.xml',
     '444_m_traffic_live_twenty.xml',
     '445_m_traffic_live_twenty.xml',
     '446_m_traffic_live_twenty.xml',
     '447_m_traffic_live_twenty.xml',
     '448_m_traffic_live_twenty.xml',
     '449_m_traffic_live_twenty.xml',
     '450_m_traffic_live_twenty.xml',
     '551_m_finance_twenty.xml',
     '552_m_finance_twenty.xml',
     '553_m_finance_twenty.xml',
     '554_m_finance_twenty.xml',
     '555_m_finance_twenty.xml',
     '556_m_finance_twenty.xml',
     '557_m_finance_twenty.xml',
     '558_m_finance_twenty.xml',
     '559_m_finance_twenty.xml',
     '560_m_finance_twenty.xml',
     '561_m_finance_twenty.xml',
     '562_m_finance_twenty.xml',
     '563_m_finance_twenty.xml',
     '564_m_finance_twenty.xml',
     '565_m_finance_twenty.xml',
     '566_m_finance_twenty.xml',
     '567_m_finance_twenty.xml',
     '568_m_finance_twenty.xml',
     '569_m_finance_twenty.xml',
     '570_m_finance_twenty.xml',
     '571_m_finance_twenty.xml',
     '572_m_finance_twenty.xml',
     '573_m_finance_twenty.xml',
     '574_m_finance_twenty.xml',
     '575_m_finance_twenty.xml',
     '576_m_finance_twenty.xml',
     '577_m_finance_twenty.xml',
     '578_m_finance_twenty.xml',
     '579_m_finance_twenty.xml',
     '580_m_finance_twenty.xml',
     '581_m_finance_twenty.xml',
     '582_m_finance_twenty.xml',
     '583_m_finance_twenty.xml',
     '584_m_finance_twenty.xml',
     '585_m_finance_twenty.xml',
     '586_m_finance_twenty.xml',
     '587_m_finance_twenty.xml',
     '588_m_finance_twenty.xml',
     '589_m_finance_twenty.xml',
     '590_m_finance_twenty.xml',
     '591_m_finance_twenty.xml',
     '592_m_finance_twenty.xml',
     '593_m_finance_twenty.xml',
     '594_m_finance_twenty.xml',
     '595_m_finance_twenty.xml',
     '596_m_finance_twenty.xml',
     '597_m_finance_twenty.xml',
     '598_m_finance_twenty.xml',
     '599_m_finance_twenty.xml',
     '600_m_finance_twenty.xml',
     '701_m_medical_treatment_twenty.xml',
     '702_m_medical_treatment_twenty.xml',
     '703_m_medical_treatment_twenty.xml',
     '704_m_medical_treatment_twenty.xml',
     '705_m_medical_treatment_twenty.xml',
     '706_m_medical_treatment_twenty.xml',
     '707_m_medical_treatment_twenty.xml',
     '708_m_medical_treatment_twenty.xml',
     '709_m_medical_treatment_twenty.xml',
     '710_m_medical_treatment_twenty.xml',
     '711_m_medical_treatment_twenty.xml',
     '712_m_medical_treatment_twenty.xml',
     '713_m_medical_treatment_twenty.xml',
     '714_m_medical_treatment_twenty.xml',
     '715_m_medical_treatment_twenty.xml',
     '716_m_medical_treatment_twenty.xml',
     '717_m_medical_treatment_twenty.xml',
     '718_m_medical_treatment_twenty.xml',
     '719_m_medical_treatment_twenty.xml',
     '720_m_medical_treatment_twenty.xml',
     '721_m_medical_treatment_twenty.xml',
     '722_m_medical_treatment_twenty.xml',
     '723_m_medical_treatment_twenty.xml',
     '724_m_medical_treatment_twenty.xml',
     '725_m_medical_treatment_twenty.xml',
     '726_m_medical_treatment_twenty.xml',
     '727_m_medical_treatment_twenty.xml',
     '728_m_medical_treatment_twenty.xml',
     '729_m_medical_treatment_twenty.xml',
     '730_m_medical_treatment_twenty.xml',
     '731_m_medical_treatment_twenty.xml',
     '732_m_medical_treatment_twenty.xml',
     '733_m_medical_treatment_twenty.xml',
     '734_m_medical_treatment_twenty.xml',
     '735_m_medical_treatment_twenty.xml',
     '736_m_medical_treatment_twenty.xml',
     '737_m_medical_treatment_twenty.xml',
     '738_m_medical_treatment_twenty.xml',
     '739_m_medical_treatment_twenty.xml',
     '740_m_medical_treatment_twenty.xml',
     '741_m_medical_treatment_twenty.xml',
     '742_m_medical_treatment_twenty.xml',
     '743_m_medical_treatment_twenty.xml',
     '744_m_medical_treatment_twenty.xml',
     '745_m_medical_treatment_twenty.xml',
     '746_m_medical_treatment_twenty.xml',
     '747_m_medical_treatment_twenty.xml',
     '748_m_medical_treatment_twenty.xml',
     '749_m_medical_treatment_twenty.xml',
     '750_m_medical_treatment_twenty.xml']



##### 解析xml文件取得標籤


```python
import re
from xml.etree.ElementTree import XMLParser
list_all_xml = [] # xml所有文件list
list_xml = []# xml文件list
file_count = 0 # 文件數量
class XML2List:
  maxDepth = 0 # 定義變數maxDepth
  depth = 0  # 定義變數depth
  # 走訪每一個元素的起始處理方式
  def start(self, tag, attrib): 
    self.depth += 1
    if self.depth > self.maxDepth:
        self.maxDepth = self.depth
    list_xml.append([self.depth, tag, attrib])
  # 走訪每一個葉節點元素處理方式
  def end(self, tag):
     self.depth -= 1
  # 呼叫處理後資料所回傳資訊
  def close(self):
    print ('最大深度:{},'.format(self.maxDepth))
```
