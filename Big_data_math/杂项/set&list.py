
# python中list为列表，有如下方式定义
list1=[] #list可以定义空列表
list2=[1,'sss',3.3] #list中的元素可以不是同一个类型
list3=list('aaabbbccc') #可以通过list()方法来将一个字符串转化成一个列表
print(list1)
print(list2)
print(list3)
 
# list是一组有序的数组，由索引来访问
print(list2[1])
 
# set为一组无序的不重复的数组，由set()方法创建
s1=set([1,5,3,3,5,8,9])
s2=set(list3)
# 输出时可见没有重复的元素
print(s1)
print(s2)
 
# list通过append(),insert(),remove(),del()，pop()等方法来对列表进行操作
# set通过add()方法添加元素（重复元素不报错但不会加入），通过remove()删除元素
 
#set主要用于查看某个元素是否存在于此集合内
x = 1
if x in s1:
    print('YES')
else:
    print('NO')
    
    
    '''
    Answer:
    
[]
[1, 'sss', 3.3]
['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
 
sss
 
{1, 3, 5, 8, 9}
{'b', 'c', 'a'}
 
YES
'''
