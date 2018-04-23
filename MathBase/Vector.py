import numpy as np

'''
NumPy的主要对象是同种元素的多维数组。这是一个所有的元素都是一种类型、
通过一个正整数元组索引的元素表格(通常是元素是数字)。
在NumPy中维度(dimensions)叫做轴(axes)，轴的个数叫做秩(rank)。

'''
a = np.array([-1, 2])
b = np.array([3, 1])
print(a + b)
print(a - b)  # 从几何角度讲，向量减相当于加上一个反向的向量。

v_volumn = np.array([1, 2])  # 列向量(单个[]),numpy中shape为(m,)的数组在矩阵运算的过程中看作行向量处理．
v_row = np.array([[1, 2]])  # 行向量
v_matrix = np.array([[1, 3], [1, 2]])  # 是一个2x2的矩阵,可以看出，行向量就是普通矩阵的特殊情况
v_matrix3 = np.array([[1, 3], [1, 2], [2, 4]])  # 是一个2x2的矩阵,可以看出，行向量就是普通矩阵的特殊情况

print("v_volumn = ", v_volumn)
print("v_row = ", v_row)
print("v_matrix = ", v_matrix)
print("v_matrix3 = ", v_matrix3)

print(v_volumn.shape)
print(v_row.shape)
print(v_matrix.shape)
print(v_matrix3.shape)
print(v_matrix3.ndim)
print(v_matrix3.size)

print(v_matrix3.T)  # 向量的转置
