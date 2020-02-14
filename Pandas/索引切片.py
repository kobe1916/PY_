import pandas as pd

t2 = pd.Series([1,2,3,4,5],index=list("abcde"))  #index添加索引
print(t2)

#还可以通过字典创建
temp_dict={"name":"xiaohong","age":30,"tel":10086}
t3 = pd.Series(temp_dict)


#Series 切片和索引
'''
切片：直接传入start end 或者步长即可
索引：一个的时候直接传入序号或者index,多个的时候传入序号或者index 的列表

Series 对象本质上由两个数组构成，
一个数组构成对象的键（index，索引），一个数组构成对象的值（values）  键->值
'''
t3.index
t3.values


#pandas 读取外部数据

import pandas as pd

#读取csv数据
df = pd.read_csv("./dogNames2.csv")
