import numpy as np

# my_array = np.array([1,2,3,4,5])
# print(type(my_array))
# print(my_array)

# my_array = np.array([range(i,i+3) for i in [2,4,6]])
# print(my_array)

#创建一个数组值都是0的数组
# my_array = np.zeros((2,3),dtype = int)
# print(my_array)

#创建一个数组值都是1的数组
# my_array = np.ones((2,3),dtype=float)
# print(my_array)

#创建一个数组值都为3的浮点型数组
# my_array = np.full((2,3),3.14 )
# print(my_array)

#0-18之间所有的偶数组成的一个数组
# my_array = np.arange(0,19,2)
# print(my_array)

#创建一个有5个元素的数组，均匀的分配0~1之间的数。
# my_array = np.linspace(0,1,5)
# print(my_array)

#创建一个随机数数组
#纯随机数
# my_array = np.random.random((3,3))
#正态分布
# my_array = np.random.normal(0,1,(3,3))
#区间随机整数
# my_array = np.random.randint(0,10,(3,3))
# print(my_array)

#创建一个单位矩阵数组
# my_array = np.eye(4)
# print(my_array)

#数组的维度(ndim)，数组每个维度的大小(shape)，数组的总大小(size)，数组的数据类型(dtype)，数组元素的字节(itemsize)，数组的总字节(nbytes)
# np.random.seed(0)
# arr_1 = np.random.randint(0,10,5)
# print(arr_1)
# print(arr_1.nbytes)
# arr_2 = np.random.randint(0,10,(3,5))
# print(arr_2)
# print(arr_2.nbytes)

# arr_2[2,2] = 3.14
# print(arr_2)
# print(arr_1[::-1])
# arr = arr_2[0,:].copy()
# arr[2] = 10
# print(arr)
# print(arr_2)

# arr_1 = np.arange(1,10)
# print(arr_1)
# arr = arr_1.reshape((3,3))
# print(arr)
# arr_1 = np.array([1,2,3])
# print(arr_1[:,np.newaxis])
# print(arr_1[np.newaxis,:])

# arr_1 = np.array([[1,2,3],[10,11,12]])
# arr_2 = np.array([[4,5,6],[13,14,15]])
# arr_3 = np.array([[7,8,9],[16,17,18]])
# # arr = np.concatenate([arr_1,arr_2,arr_3],axis = 1)
# # print(arr)
# arr = np.dstack([arr_1,arr_2,arr_3])
# print(arr)

