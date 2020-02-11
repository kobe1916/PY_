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



'''题目2    你和同桌各自的'''
rom matplotlib import pyplot as plt
form matplotlib import font_manager

my_font = font_manger.FontProperties()

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,3,1,1,2,4,3,3,3,5,4,5,6,5,2,3,2,3,4,0]

x = range(11,31)

#设置图形大小
plt.figure(figsize(20,8),dpi=80)

plt.plot(x,y_1,label = "ziji",dolor = "orange",linestyle = ':')
plt.plot(x,y_2,label = "tongzhuo",color = "green",linestyle='--')


#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xticks_labels,fontproperties = my_font)

#绘制网格
plt.grid(alpha = 0.4,linestyle =':')  #alpha设置透明度

#添加图例
plt.legend(prop = my_font,loc = "upper lesft")

#展示
plt.show()
