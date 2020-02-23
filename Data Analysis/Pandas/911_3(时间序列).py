#不同月份不同类型
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#def plot_img(df,label):



#把时间字符串转化为时间类型设置为索引
df = pd.read_csv("./911.csv")
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
#df.set_index("timeStamp",inplace=True)

#添加列，表示分类
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

df.set_index("timeStamp",inplace=True)

plt.figure(figsize=(20,8),dpi = 80)

#分组
for group_name,group_data in df.groupby(by="cate"):
    #对不同类型的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]

    # 画图
    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _y, rotation=45)
plt.legend(loc="best")
plt.show()

