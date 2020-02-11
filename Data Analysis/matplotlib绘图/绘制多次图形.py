'''
题目：统计从11岁到30岁每年交的男女朋友数量如列表a，绘制该数据的折线图，分析每年交友数量走势
a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
要求：y轴表示个数
    x轴表示岁数，如11岁
'''

from matplotlib import pyplot as plt
form matplotlib import font_manager
y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

#设置图形大小
plt.figure(figsize(20,8),dpi=80)

plt.plot(x,y)

#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xticks_labels,fontproperties = my_font)

#绘制网格
plt.grid(alpha = 0.4)  #alpha设置透明度
plt.show()



