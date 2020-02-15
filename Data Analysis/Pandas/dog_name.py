#统计dog_name
import pandas as pod

df = pd.read_csv()
#DataFrame中排序方法
df= pd.sort_values(by="Count_AnimalName",ascending=False)
print(df.head(5))


#问题：取第1，3，8列排序？

#pandas取行或者列的注意点
#- 方括号写数组，表示取行 对行进行操作
#- 写字符串 表示取列索引 对列进行索引
print(df[:20])
print(df["Row_Labels"])
print(type(df["Row_Labels"]))



#pandas之loc
''' df.loc 通过标签索引行数据
    df.iloc通过位置获取行数据
    '''
t3 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
t3.loc["a","Z"]
type(t3.loc["a","Z"])
t3.loc["a"]  #t3.loc["a",:]
t3.loc[:,"Y"]


#多行多列
t3.loc[["a","c"]]
t3.loc[["a":"c"]]  #a--c  包含c
