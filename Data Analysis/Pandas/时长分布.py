#对一组电影数据 想统计rating runtime 分布情况 该如何呈现数据

import pandas as pd
from matplotlib import pyplot as plt

file_path = ""

df = pd.read_csv(file_path)
print(df.head(1))
print(df.info)

#rating runtime分布情况
#选择图形 直方图
#准备数据
runtime_data = df["Runtime (Minute)"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

#计算组数
num_bin = (max_runtime-min_runtime)//5

#设置图形的大小
plt.figure(figsize(20,8),dpi=80)
plt.hist(runtime_data,num_bin)

plt.xticks(range(min_runtime,max_runtime+5,5))
plt.show()



#评分分布   重新看
