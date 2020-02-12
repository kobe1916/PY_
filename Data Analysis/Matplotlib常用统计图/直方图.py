'''
直方图  电影时长  统计电影时长分布状态
原始数据 未经过统计的数据才能绘制成直方图


应用场景：XXX分布状态

组数=极差/组距   组距：每个小组两个端点的距离
'''
from matplotlib import pyplot as plt
from matplotlib import font_manager

a=[]

#计算组距
d =5
num_bims= (max(a)-min(a))//d

#设置图形大小
plt.figure(figsize(20,8),dpi = 80)

plt.hist(a,num_bins)

#设置x轴刻度
plt.xticks(range(min(a),max(a)+d,d))

plt.grid()

plt.show()
