'''
问题  来自英国和美国各一千多视频  的点击 喜欢  不喜欢  评论数量

'''

'''
import numpy as np

us_file_path ="...."
uk_file_path="..."

t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

print(t1)
print("*"*10)
print(t2)
'''


import numpy as np

#us_file_path ="...."
uk_file_path="..."

#t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(uk_file_path,delimiter=",",dtype="int")

#print(t1)
print(t2)
print("*"*10)

#取行
print(t2[2])

#取连续行
print(t2)[2:])

#取不连续行
print(t2[[2,8,10]])

'''
print(t2[1,:])
print(t2[2:,:])
print(t2[:,0])
'''
#取列
print(t2[:,0])

#取连续多列
print(t2[:,[0,2]])

#取多行多列    第三行 第四列值
 a = t2[2,3]
print(a)
print(type(a))

#取多行和多列  取第三行到第五行 第二列到第四列的结果
b = t2[2:5,1:4]
print(b)

#取多个不相邻的点     选出结果是 （0，0）  （2，1）   （2，3）
c = t2[[0,2,2],[0,1,3]]
print(c)




#布尔索引
t2<10   #t2中小于10的为True 大于是为False
t2[t2<10]=3   #把t2中小于10的元素全部赋值为3 

#把t中小于10的替换为0  大于20的替换为20
np,where(t<10,0,10)  #numpy的三元运算符   小于10的全部替换为0其余替换为10


#numpy中的clip裁剪
t.clip(10,18)   #小于10的替换为10   大于18的替换为18    nan是浮点类型
