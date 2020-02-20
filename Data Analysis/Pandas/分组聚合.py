'''
星巴克店铺统计   美国和中国那个多   中国每个省份星巴克数量

思路：遍历一遍  每次加1？？？
pandas分组   grouped = df.groupby(by="columns_name")
grouped 是一个DataFrameGroupBy对象  是可迭代的
grouped 中每一个元素是一个元组
元组里面是 （索引（分组的值），分组之后的DataFrame)

'''
import pandas as pd
import numpy as nnp

file_path = " "

df = pd.read_csv(file_path)

#print(df.head(1)
#print(df.info())

grouped = df.grouped(by="Country")
print(grouped)

#DataFrameBy
'''
for i,j in grouped:
    print(i)
    print("-"*100)
    print(j,type(j))
    print("*"*100)
    df[df["Country"]="US"]
'''
    #调用聚合方法
country_count=grouped["Brand"].count()
print(country_count["US"])
print(country_count["CN"])


#统计中国每个省份数量
china_data = df[df["Country"]=="CN"]

grouped = china_data.groupedby(by="State/Province").count()["Brand"]
print(grouped)
