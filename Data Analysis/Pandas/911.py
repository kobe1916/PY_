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
