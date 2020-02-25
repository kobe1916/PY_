import pandas as pd
from matplotlib import pyplot as plt
file_path = "./"
df = pd.read_csv(file_path)

print(df.head())
print(df.info())

'''
DataFrameindex可以理解为时间戳
PeriodsIndex可以理解为时间段
periods = pd.Periodindex(year=data["year"],
month=data["month"],day=data["day"],hour=data["hour"],freq="H")'''

#把分开的时间字符串通过Periodsindex的方法转为pandas的时间类型
periods = pd.Periodindex(year=data["year"],month=data["month"],day=data["day"],hour=data["hour"],freq="H")
df["datetime"] = periods
#print(df.head(10))

#把datetime设置为索引
df.set_index("datetime",inplace=True)

#进行降采样
df = df.resample("7D").mean()

#处理缺失数据  删除缺失数据
print(df["PM_US Post"])
data = df["PM_US Post"].dropna()
data_china = df["PM_Dongsi"].dropna()

#画图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_china = [i.strftime("%Y%m%d") for i in data_china.index]
_y = data.values
_y_china = data_china.values

plt.figure(figsize==(20,8),dpi = 80)

plt.plot(range(len(_x)),_y,label="US")
plt.plot(range(len(_x_china)),_y_china,label="CN")

plt.xticks(range(0,len(_x),20),list(_x)[::20])
plt.legend("best")
plt.show()
