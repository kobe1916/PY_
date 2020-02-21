import pandas as pd
file_path = " "
df = pd.read_csv(file_path)

#使用matplotlib呈现店铺排名前10的国家

#准备数据
data1 = df.groupby(by="Country").count()["Brand"].soort_values(ascending=False)[:10]

_x = data1.index
_y = data1.values

#画图
plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x)

plt.show()




#使用matplotlib呈现出每个中国城市的店铺数量
import pandas as pd
from matplotlib impport pyplot as plt

file_path = " "
df = pd.read_csv(file_path)

df = df[df["Country"]=="CN"]


#准备数据
data1 = df.groupby(by="City").count()["Brand"].soort_values(ascending=False)[:50]

_x = data1.index
_y = data1.values

#画图
plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(_x)),_y,width=0.3,color="orange")

plt.xticks(range(len(_x)),_x)

plt.show()



'''
动手： 全球排名靠前1w本书统计
1  不同年份书的数量
2  不同年份书的评分情况


https://www.kaggle.com/zygmunt/goodbooks-10k
'''

import pandas as pd
from matplotlib impport pyplot as plt

file_path = " "
df = pd.read_csv(file_path)

#取出有效信息
data1= df[pd.notnull(df["original_publication_year"])]

data1.groupby(by="original_publicationn_year").count()["title"]

#不同年份书的平均评分情况


