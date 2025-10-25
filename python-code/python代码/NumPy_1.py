import numpy as np
# np.random.seed(0)
# arr_1 = np.random.randint(1,10,size = 5)
# print(arr_1)
# def compute_re(values):
#     output = np.empty(len(values))
#     for i in range(len(values)):
#         output[i] = 1.0 / values[i]
#     return output
# print(compute_re(arr_1))  #16.6 µs ± 4.1 µs per loop
# print(1.0 / arr_1) #1.8 µs ± 104 ns per loop

# print(arr_1 + 2)
# print(arr_1 - 2)
# print(-arr_1)
# print(arr_1 * 2)
# print(arr_1 / 2)
# print(arr_1 ** 2)
# print(arr_1 % 2)
# print(arr_1 // 2)
# arr_1 = arr_1 - 3
# print(arr_1)
# print(np.absolute(arr_1))

# arr_angle = np.linspace(0,np.pi,3)
# print(arr_angle)
# print(np.sin(arr_angle))
# print(np.cos(arr_angle))
# print(np.tan(arr_angle))

# arr = np.array([-1,0,1])
# print(np.arcsin(arr))
# print(np.arccos(arr))
# print(np.arctan(arr))

# arr = np.array([1,2,3])
# print(np.exp(arr))  #计算e的n次方
# print(np.exp2(arr)) #计算2的n次方
# print(np.power(3,arr)) #计算3的n次方
# print(np.log(arr))  #计算以e为底数的对数
# print(np.log2(arr)) #计算以2为底数的对数
# print(np.log10(arr)) #计算以10为底数的对数

arr_1 = np.arange(5)
arr_2 = np.empty(5)
print(arr_1)
np.multiply(arr_1,10,out = arr_2)
print(arr_2)
arr_2[0] = 1
print(arr_2)
print(arr_1)
a = 10
print(a)

