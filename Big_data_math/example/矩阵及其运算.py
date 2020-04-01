# -*- coding: utf-8 -*-

# 代码4-14
import numpy as np
# 方法一
A1 = np.mat('1 2 3 4;3 4 5 6;5 6 7 8;7 8 9 0')
print('使用mat函数创建的矩阵为：\n', A1)


# 方法二
A2 = np.matrix([[1, 2, 3, 4],[3, 4, 5, 6],[5, 6, 7, 8],[7, 8, 9, 0]])
print('使用matrix函数创建的矩阵为：\n', A2)




# 代码4-15
O = np.zeros((3, 3))
print('零矩阵O为：\n', O)




# 代码4-16
# 使用identity函数创建3行3列的单位矩阵
E = np.identity(3)
print('单位矩阵E为：\n', E)
# 使用eye函数创建3行3列的单位矩阵
I = np.eye(3, k = 0)
print('单位矩阵I为：\n', E)




# 代码4-17
A = np.diag([1, 2, 3, 4], k = 0)
print('对角矩阵A为：\n', A)




# 代码4-18
B = np.matrix([[1, 2, 3, 4],[3, 4, 5, 6],[5, 6, 7, 8],[7, 8, 9, 0]])
A = np.triu(B, k = 0)
print('上三角矩阵A为：\n', A)




# 代码4-19
B = np.matrix([[1, 2, 3, 4],[3, 4, 5, 6],[5, 6, 7, 8],[7, 8, 9, 0]])
A = np.tril(B, k = 0)
print('下三角矩阵A为：\n', A)




# 代码4-20
A = np.matrix([[2, 1, 4],[0, 3, 3]])
B = np.matrix([[3, 3, 1],[4, 0, 3]])
print('矩阵A与矩阵B的和为：\n', A + B)




# 代码4-21
A = np.matrix([[2, 1, 4],[0, 3, 3]])
k = 3
print('矩阵A与数k的乘积为：\n', A * k)




# 代码4-22
A = np.matrix([[1, 2, 3],[1, 1, 2],[0, 1, 2]])
B = np.matrix([[16, 25],[20, 8],[15, 14]])
print('密文矩阵为：\n',  A * B)  # 方法一


print('密文矩阵为：\n', np.dot(A, B))  # 方法二




# 代码4-23
B = np.mat('16 25;20 8;30 14')
print('矩阵B的转置矩阵为：\n', B.T)




# 代码4-24
A = np.matrix([[1, 2, 3],[1, 1, 2],[0, 1, 2]])
C = np.matrix([[101, 83],[66, 61],[50, 36]])
print('密钥矩阵为：\n', (A.I) * C)  # 方法一
print('密钥矩阵为：\n', np.linalg.inv(A) * C)  # 方法二




# 代码4-25
A = np.matrix([[1, -1, 5, -1],[1, 1, -2, 3],[3, -1, 8, 1],[1, 3, -9, 7]])
print('矩阵A的秩为：', np.linalg.matrix_rank(A))




# 代码4-26
A = np.matrix([[1, -1, 0, 0],[0, 1, -1, 0],[0, 0, 1, -1],[-1, 0, 0, 1]])
B = np.matrix([[1, -1, 0, 0, 160],[0, 1, -1, 0, -40],[0, 0, 1, -1, 210],[-1, 0, 0, 1, -330]])
print('矩阵A的秩为：', np.linalg.matrix_rank(A))
print('矩阵B的秩为：', np.linalg.matrix_rank(B))




# 代码4-27
x = np.random.random(size=(2,5))  # 生成2行5列的数据
Vx = np.cov(x)
print('矩阵x的协方差矩阵为：\n', Vx)




# 代码4-28
x = np.random.random(size=(2,5))  #生成2行5列的矩阵
R = np.corrcoef(x)
print('矩阵x的相关矩阵为：\n', R)

