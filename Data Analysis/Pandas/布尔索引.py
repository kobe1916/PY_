#布尔索引
#找狗名字使用超过800次以上的     多条件查找  &且  |或  不同条件需要用括号括起来

import pandas as pd

#读取数据
df = pd.read_csv()

print(df[(800<df["Count_AnimalName"])&(df["Count_AnimalName"]<1000)])


#缺失数据处理
'''
缺失数据：1. nan  2. 为0

判断数据是否为NaN :pd.isnull(df)   pd,notnull(df)
处理方式1：删除NaN所在的行列dropnaa(axis=0,how='any',inplace=False)
    any：只要有nan就删除
    all：全部是nan才删除

处理方式2：填充数据  t.fillna(t.mean())   t.fiallna(t.madian())  t.fillna(0)
  
处理为0的数据  t[t==0]=np.nan
并不是每次为0的数据都需要处理
计算平均值等情况 nan是不参与计算的  但是0会
