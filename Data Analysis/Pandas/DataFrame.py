import pandas as pd
import numpy as np

pd.DataFrame(np.arange(12),reshape(3,4))
pd.DataFrame(np.arange(12),reshape(3,4),index=list("abc"),column=list("WXYZ"))
t1=pd.DataFrame(np.arange(12),reshape(3,4),index=list("abc"),column=list("WXYZ"))
print(t1)

#传入字典
d1={"name":["xiaoming","xiaohong"],"age":[20,21],"tel":[10086,10087]}
pd.DataFrame(d1)
t1 = pd.DataFrame(d1)



'''  基础属性
df.shape  #行数 列数
df.dtype  #列数据类型
df.ndim  #数据维度
df.index   #行索引
df.columns   #列索引
df.values   #对象值 二维ndarry数组

整体情况查询
df.head(3)  #显示头部几行  默认5行
df.tail(3)   #显示末尾几行，默认5行
df.info()  #相关信息概览：行数、列数、列索引、列非空值个数、列类型、列类型、内存占用
df.describe()  #快速综合统计结果：计数、均值、标准差 最大值、四分位数、最小值 （只能统计数字类型的）

'''

