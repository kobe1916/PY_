'''
数组合并
join:默认情况下 把行索引相同的数据合并到一起

merge:按照指定的列把数据按照一定的方式合并到一起
默认 inner 交集
merge outer 并集 NAN补全
merge left 左边为准 NAN补全
merge right 右边为准NAN补全

'''
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=["abc"])
df2 = pd.DataFrame(np.zeros((3,3)),index=["A","B","C"],columns=list("xyz"))
df1.join(df2)
df2.join(df1)

df3= pd.DataFrame(np.zeros((3,3)),columns=list("fax"))
df1.merge(df3,on="a")
df1.merge(df3,on="a",how="left")
