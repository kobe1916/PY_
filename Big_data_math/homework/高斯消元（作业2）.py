# 矩阵格式输出函数
def print_matrix(info, m):
    print(info)
    for i in range(0, l):
        for j in range(0, k):
            if (j == k - 1):
                print('|', end=' ')  # 将系数矩阵和向量b用“|”隔开
            print(m[i][j], end=' ')  # 输出矩阵元素m[i][j]
        print('\n')

def solve(ma):
    global m
    m = ma
    global l
    global k
    l = len(matrix)
    k = len(matrix[0])
    row_pos = 0
    col_pos = 0
    # row_pos 变量标记行循环, col_pos 变量标记列循环
    while ((row_pos<l) and (col_pos<l)):
        if(abs(m[row_pos][col_pos]) == 0.0 and row_pos==l-1):
             return 0
        if(abs(m[row_pos][col_pos]) == 0.0):
            for h in range(row_pos+1,l):
                if(m[h][col_pos]!=0):
                    for j in range(0,k):   #将主元位置为0的行和下面该列不为0的行交换
                        t = m[h][j]
                        m[h][j] = m[row_pos][j]
                        m[row_pos][j] = t
                    print_matrix("交换两行", m)
                    break
                else:
                    continue       #如果下面的行全为0就不交换
        if (m[row_pos][col_pos] == 0):
            return 0
        if(m[row_pos][col_pos]!=1):
            for n in range(k-1,col_pos-1,-1):   #将该行主元化为1，该行所有数除以主元
                m[row_pos][n]  = m[row_pos][n] / m[row_pos][col_pos]
            print("主元位置：(%d,%d)" % (row_pos, col_pos))
            print_matrix("主元化1",m)
        # 开始消元
        for i in range(0, l):   #遍历所有行
            if (i == row_pos):
                continue
            for j in range(k - 1, col_pos - 1, -1):   #遍历列从最后一列到主元所在列
                m[i][j] = m[i][j] - m[row_pos][j] * m[i][col_pos] #每个元素减去主元所在行对应的这一列元素乘该行主元所在列对应的元素
        print_matrix("消元", m)
        # 消元结束
        # 主元移到下一个位置
        row_pos += 1
        col_pos += 1
    return 1
# test
if __name__ == '__main__':
    matrix = [[1.0,1.0,1.0,1.0,1.0,1.0],
              [3.0,2.0,1.0,1.0,-3.0,25.0],
              [0,1.0,2.0,2.0,6.0,-22.0],
              [5.0,4.0,3.0,3.0,-1.0,27],
              [2.0,-1.0,0,3.0,2.0,2.0]]
    l = len(matrix)
    k = len(matrix[0])
    print_matrix("一开始的矩阵", matrix)
    ret = solve(matrix)    # 求解方程组, 并输出方程组的可解信息
    if (ret != 0):
        print("方程组有解\n")
        print_matrix("方程组及其解", m)
        for i in range(0, len(m)):
            print("x[%d] = %6.4f" % (i+1, m[i][len(m[i]) - 1]))
    else:
        if(m[l-1][k-1]!=0):
           print('方程无解\n')
        else:
            print("方程组无唯一解\n")
            print("方程组的一组解\n")
            for i in range(0,l):
                if (m[i][i] != 0):
                    x = m[i][k - 1]
                    for j in range(k-2,i,-1):    #从倒数第二列开始遍历，用最后一列减去前面的，计算出值
                        x-=m[i][j]
                    print('x[%d]=%6.4f'% (i+1, x))
                else:
                    print('x[%d]=1.0'%(i+1))



'''
一开始的矩阵
1.0 1.0 1.0 1.0 1.0 | 1.0 

3.0 2.0 1.0 1.0 -3.0 | 25.0 

0 1.0 2.0 2.0 6.0 | -22.0 

5.0 4.0 3.0 3.0 -1.0 | 27 

2.0 -1.0 0 3.0 2.0 | 2.0 

消元
1.0 1.0 1.0 1.0 1.0 | 1.0 

0.0 -1.0 -2.0 -2.0 -6.0 | 22.0 

0.0 1.0 2.0 2.0 6.0 | -22.0 

0.0 -1.0 -2.0 -2.0 -6.0 | 22.0 

0.0 -3.0 -2.0 1.0 0.0 | 0.0 

主元位置：(1,1)
主元化1
1.0 1.0 1.0 1.0 1.0 | 1.0 

0.0 1.0 2.0 2.0 6.0 | -22.0 

0.0 1.0 2.0 2.0 6.0 | -22.0 

0.0 -1.0 -2.0 -2.0 -6.0 | 22.0 

0.0 -3.0 -2.0 1.0 0.0 | 0.0 

消元
1.0 0.0 -1.0 -1.0 -5.0 | 23.0 

0.0 1.0 2.0 2.0 6.0 | -22.0 

0.0 0.0 0.0 0.0 0.0 | 0.0 

0.0 0.0 0.0 0.0 0.0 | 0.0 

0.0 0.0 4.0 7.0 18.0 | -66.0 

交换两行
1.0 0.0 -1.0 -1.0 -5.0 | 23.0 

0.0 1.0 2.0 2.0 6.0 | -22.0 

0.0 0.0 4.0 7.0 18.0 | -66.0 

0.0 0.0 0.0 0.0 0.0 | 0.0 

0.0 0.0 0.0 0.0 0.0 | 0.0 

主元位置：(2,2)
主元化1
1.0 0.0 -1.0 -1.0 -5.0 | 23.0 

0.0 1.0 2.0 2.0 6.0 | -22.0 

0.0 0.0 1.0 1.75 4.5 | -16.5 

0.0 0.0 0.0 0.0 0.0 | 0.0 

0.0 0.0 0.0 0.0 0.0 | 0.0 

消元
1.0 0.0 0.0 0.75 -0.5 | 6.5 

0.0 1.0 0.0 -1.5 -3.0 | 11.0 

0.0 0.0 1.0 1.75 4.5 | -16.5 

0.0 0.0 0.0 0.0 0.0 | 0.0 

0.0 0.0 0.0 0.0 0.0 | 0.0 

方程组无唯一解

方程组的一组解

x[1]=6.2500
x[2]=15.5000
x[3]=-22.7500
x[4]=1.0
x[5]=1.0
'''
