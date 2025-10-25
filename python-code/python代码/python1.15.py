# import numpy as np

# my_array = np.array([[1,2,3.0],[4,5,6]])
# print(my_array)
# print(my_array.dtype)
# print(type(my_array))
# summary = my_array.sum()
# print(summary)

# my_array = np.array([1,2,3,4,5],dtype='float32')
# print(my_array)

# my_array = np.array([range(i,i+3) for i in [2,4,6]])
# print(my_array)

"""从头创建数组的几种方式"""

# #创建一个数组值都为0的数组
# my_array_0 = np.zeros((2,3),dtype=int)
# print(my_array_0)

# my_array = np.ones((3,5),dtype='float32')
# print(my_array)

# my_array = np.full((3,5),3,dtype=float)
# print(my_array)

# #创建一个从0到18的偶数数组
# my_array = np.arange(0,20,2)
# print(my_array)

# #创建一个5个元素的数组，这五个数均匀的分配0~1
# my_array = np.linspace(0,1,5)
# print(my_array)

# # 创建一个3*3的，在0~1之间均匀分布的随机数组成的数组
# my_array = np.random.random((3,3))
# print(my_array)

# # 创建一个3×3的、均值为0、方差为1的正态分布的随机数数组
# my_array = np.random.normal(0, 1, (3, 3))
# print(my_array)

# # 创建一个3×3的、[0, 10)区间的随机整型数组
# my_array = np.random.randint(0, 10, (3, 3))
# print(my_array)

# # 创建一个3×3的单位矩阵
# my_array = np.eye(3)
# print(my_array)

# array_1 = np.array([1,2,3])
# array_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# ndim_1 = np.ndim(array_1)
# ndim_2 = np.ndim(array_2)
# shape_1 = np.shape(array_1)
# shape_2 = np.shape(array_2)
# size_1 = np.size(array_1)
# size_2 = np.size(array_2)
# itemsize_1 = array_1.itemsize
# itemsize_2 = array_2.itemsize
# nbytes_1 = array_1.nbytes
# nbytes_2 = array_2.nbytes
# print(ndim_1,end = " ")
# print(ndim_2,end = " ")
# print(shape_1,end = " ")
# print(shape_2,end = " ")
# print(size_1,end = " ")
# print(size_2,end = " ")
# print(itemsize_1,end = " ")
# print(itemsize_2,end = " ")
# print(nbytes_1,end = " ")
# print(nbytes_2,end = " ")

# np.random.seed(0)
# #一维数组
# array_1 = np.random.randint(0,10,5)
# print(array_1)
# print(array_1[1:5])
# print(array_1[::-1])
#
# #二维数组
#array_2 = np.random.randint(0,10,(3,5))
# print(array_2)
# print(array_2[:2,:3]) #前两行，前三列
# print(array_2[:3,::2]) #每一行，每隔一列
# print(array_2[:,0]) #数组的第一列
# print(array_2[0,:]) #数组的第一行

# x = np.array([1, 2, 3])
# #通过变形获得的行向量
# print(x.reshape((1, 3)))
# # 通过newaxis获得的行向量
# print(x[np.newaxis, :])
# # 通过变形获得的列向量
# print(x.reshape((3, 1)))
# # 通过newaxis获得的列向量
# print(x[:, np.newaxis])

# arr_1 = np.array([[1,2,3],[10,11,12]])
# arr_2 = np.array([[4,5,6],[13,14,15]])
# arr_3 = np.array([[7,8,9],[16,17,18]])
# arr = np.concatenate([arr_1,arr_2,arr_3],axis=1)
# print(arr)

# x = [1, 2, 3, 99, 99, 3, 2, 1]
# x1, x2, x3 = np.split(x, [3, 5])
# # print(x1, x2, x3)
# grid = np.arange(16).reshape((4, 4))
# print(grid)
# upper, lower = np.vsplit(grid, [2])
# print(upper)
# print(lower)
# left, right = np.hsplit(grid, [2])
# print(left)
# print(right)

# a = input()
# if a == "pizza":
#     print(10)
# elif a == "rice":
#     print(2)
# elif a == "yogurt":
#     print(5)
# else:
#     print(8)

# d = {'A':4.0,'B':3.0,'C':2.0,'D':1.0,'F':0.0}
# s = input()
# num1 = 0
# num2 = 0
# while s != 'False':
#     s1 = int(input())
#     num1 += d[s] * s1
#     num2 += s1
#     s = input()
# num2 = num1 / num2
# print(f"{num2:.2f}")

# name = input('输入用户名：')
# password = int(input('设置密码：'))
# print(type(name))
# print(type(password))
# print(password)

# a = input()
# b = input()
# if a == "admis" and b == "Nowcoder666":
#     print("Welcome!")
# else:
#     print("user id or password is not correct!")

# my_list = ['P','y','t','h','o','n']
# print("Here is the original list")
# print(my_list)
# print('\n',end = "")
# print("The number that my_list has is:")
# print(len(my_list))