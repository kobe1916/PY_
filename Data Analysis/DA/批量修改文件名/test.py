##  OS模块

import os
print(os.getcwd())
#当前文件路径
print(os.name)
#当前系统   posix  Linux/unix系统   nt  Windows系统
os.mkdir('./文件夹')
#相对路径
#新建文件夹  .当前目录
'''
C:\Users\lhy\Desktop\Data analysis
nt
'''

import os
#返回绝对路径
result = os.path.abspath('文件夹')
#print(result)

#判断是否时文件夹   isdir
result = os.path.isdir('文件夹')
#print(result)

#判断是否是文件   isfile
result = os.path.isfile('./批量修改文件名.ipynb')
#print(result)

#
result = os.path.splitext('./批量修改文件名.ipynb')
#print(result)

#判断文件是否存在
result = os.path.exists('C:/Users/lhy/Desktop/Data analysis/批量修改文件名.ipynb')
#print(result)

#创建时间   ctime时间戳
result = os.path.getctime('C:/Users/lhy/Desktop/Data analysis/批量修改文件名.ipynb')
print(result)

import time
time_now = time.localtime(result)
mytime = time.strftime('%Y-%m-%d %H:%H:%S',time_now)
print(mytime)
'''
1603782432.2329137
2020-10-27 15:15:12
'''
