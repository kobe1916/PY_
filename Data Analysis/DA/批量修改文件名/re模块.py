#使用
import re
result = re.findall("正则表示匹配规则",
                   "利用(正则表示匹配规则)到这个字符串查找符合规则的数据")
print(f'根据正则匹配结果:{result}')

#findall(规则，箱子)


import re 
result = re.findall("正则表示匹配规则",
                   "利用(正则表示匹配规则)到这个字符串查找符合规则的数据正则表示匹配规则")
print(f'根据正则匹配结果:{result}')

#匹配电话号
str1 = '我的电话号： 13888888888，他的电话号：13666666666'
#result = re.findall('\d\d\d\d\d\d\d\d\d\d\d',str1)
result = re.findall('\d{11}',str1)
print(result)
