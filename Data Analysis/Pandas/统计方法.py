#pandas常用统计方法
import pandas as pd

file_path = ""
df = pd.read_csv(file_path)

print(df.info())

#获取平均评分
print(df["Rating"].mean())

#导演人数
print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))


#演员人数
temp_actors_list = df["Actors"].str.split(", ").tolist()
# actor_list = [i for j in temp_actors_list for i in j]

actors_num = len(set(actors_list))
print(actors_num)

#电影时长最大最小值
max_runtime = df["Runtime (Minute)"].max()
max_runtime_index = df["Runtime (Minute)"].argmax()
min_runtime = df["Runtime (Minute)"].min()
min_runtime_index = df["Runtime (Minute)"].argmin()
runtime_median = df["Runtime (Minute)"].median()

