#统计不同类型的紧急情况次数
#统计不同月份不同类型紧急电话次数变化情况

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.read_csv("./911.csv")

print(df.head())
print(df.info())

#获取分类
#print()df["title"].str.split(": ")
temp_list = df["title"].str.split(": ").tolist()
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)

#构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

#赋值
for cate in cate_list:
    zeros_df[cate][df["title"].str.contains(cate)] = 1

print(zeros_df)
'''
for i in range(df.shape[0]):
    zeros_df.loc[i,tem_list[i][0] = 1
print(zeros_df)
'''
sum_ret = zeros_df.sum(axis=0)
print(sum_ret)


#不同月份不同类型
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./911.csv")

#获取分类
#print()df["title"].str.split(": ")
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)),columns=["cate"])
print(cate_df)

#df["cate"] = cate_df
print(df.groupby(by ="cate").count()["title"])




#时间序列
pd.data_range(start=None,end=None,periods=None,freq='D')
'''  periods  时期 每段时间
D--day
M--month  每月最后一天  MS 每月第一天  BMS 每月第一个工作日
B工作日
H每小时
T/min 每分    S 每秒    L 每毫秒   BM 每月最后一个工作日
start和end以及freq配合能够生成start和end范围内以频率freq的一组时间索引
start和periods以及freq配合能够生成以start开始的频率为freq的periods个时间索引


df = pd.DataFrame(np.random.rand(10),index=index)
df["timeStamp"] = pd.to_datetime(df["timeStamp"],format="")
format参数大部分情况可以不用写，对于pandas无法格式化的时间字符串可以用该参数，不i如包含中文
百度  python时间格式化
'''

#pandas重采样
#重采样：指将时间序列从一个频率转化为另一个频率进行处理的过程
#将高频率转化为低频率数据为降采样，低频率转化为高频率为升采样

#pandas提供了一个resample的方法来帮助我们实现频率转化
