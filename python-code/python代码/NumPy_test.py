import numpy as np
#创建一个简单的数组
# a = np.array([1,2,3,4,5],ndmin = 2)
# print(a)
# print(type(a))

# #创建一个二维数组
# a = np.array([range(i,i+3) for i in [1,2,3]])
# print(a)

# """创建一个全0的数组"""
# a = np.zeros((3,4))
# print(a)

# """创建一个全1的数组"""
# a = np.ones((3,4),dtype = int)
# print(a)

# """创建一个形状相同的数组"""
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# b = np.zeros_like(a)
# print(b)

# """创建一个线性序列数组"""
# a = np.arange(10,20,2)
# print(a)

# """创建一个均匀分配长度的数组"""
# a = np.linspace(0,1,5)
# print(a)

# """创建随机数组"""
# a = np.random.random((3,4))
# print(a)

# """创建一个正态分布的数组"""
# a = np.random.normal(0,1,(3,4))
# print(a)

# """创建一个随机整数数组"""
# a = np.random.randint(0,10,(3,4))
# print(a)

"""创建一个单位矩阵"""
a = np.eye(3)
print(a)