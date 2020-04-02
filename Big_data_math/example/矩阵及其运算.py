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



# -*- coding: utf-8 -*-

# 代码4-29
import numpy as np
A = np.matrix([[3, -1],[-1, 3]])
# 方法一
print('矩阵A的特征值为：', np.linalg.eigvals(A))

# 方法二
A1,A2 = np.linalg.eig(A)
print('矩阵A的特征值为：', A1)
print('矩阵A的特征向量为：\n', A2)




# 代码4-30
A = np.mat([[3,1],[2,2]])
A1,A2 = np.linalg.eig(A)
print('矩阵A的特征值为：\n', A1)
print('矩阵A的特征向量为：\n', A2)




# 代码4-31
A = np.mat([[1,3,3],[-3,-5,-3],[3,3,1]])
A1,A2 = np.linalg.eig(A)
print('矩阵A的特征值为：', A1)
print('矩阵A的特征向量为：\n', A2)
# 构建矩阵P
P = np.mat(A2)
print('矩阵P为：\n', P)
# 构建矩阵D
D = np.diag(A1)
print('矩阵D为：\n', D)



# 代码4-32
import math
sq2 = math.sqrt(2)/2
A = np.mat([[sq2,sq2],[-sq2,sq2]])
print('矩阵A.T*A的结果为：\n', A.T*A)




# 代码4-33
v = np.array([1,-2,2,0])
vv = math.sqrt(np.sum(v.T*v))
u = (1/vv)*(v.T)
print('向量v的长度为：', vv)
print('单位向量u为：', u)




# 代码4-34
a = np.array([5,6,-1])
b = np.array([4/3,-1,2/3])
print('向量a*b的结果为：', np.sum(a*b))




# 代码4-35
A = np.mat([[3,-2,4],[-2,6,2],[4,2,3]])
A1,A2 = np.linalg.eig(A)
print('矩阵A的特征值为：', A1)
print('矩阵A的特征向量为：\n', A2)
# 特征向量正交化
B3 = A2[:,2]-np.float(np.vdot(A2[:,2],A2[:,0]))/np.float(np.vdot(A2[:,0],A2[:,0]))*A2[:,0]
# 特征向量单位化
P1 = math.sqrt(np.linalg.norm(A2[:,0])) * A2[:,0]
P2 = math.sqrt(np.linalg.norm(A2[:,1])) * A2[:,1]
P3 = math.sqrt(np.linalg.norm(B3)) * B3
# 构建矩阵D
D = np.diag(A1)
print('矩阵D为：\n', D)




# 代码4-36
L = np.mat([[1,1/2,0],[0,1/2,1],[0,0,0]])
L1,L2 = np.linalg.eig(L)
print('矩阵A的特征值为：', L1)
print('矩阵A的特征向量为：\n', L2)
# 构造矩阵
D = np.diag(L1)
print('矩阵D为：\n', D)
# 构建矩阵C
C = np.mat(L2)
print('矩阵C为：\n', C)




# 代码4-37
# 求特征值
A = np.mat([[4,11,14],[8,7,-2]])
B = np.linalg.eigvals(A.T*A)
print('特征值为：', B)
# 计算奇异值
import math
print('奇异值1为：', math.sqrt(B[0]))
print('奇异值3为：', math.sqrt(B[2]))




# 代码4-38
A = np.mat([[4,11,14],[8,7,-2]])
U,X,V = np.linalg.svd(A)
print('矩阵A的左奇异向量为：\n', U)
print('矩阵A的奇异值为：', X)
print('矩阵A的右奇异向量为：\n', V)




# 代码4-39
A = np.mat([[1,1,1,1,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],
            [1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
U,X,V = np.linalg.svd(A)
print('矩阵A的左奇异向量为：\n', U)
print('矩阵A的奇异值为：\n', X)
print('矩阵A的右奇异向量为：\n', V)





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

