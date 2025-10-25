# users_list = [ 'Niuniu','Niumei','Niu Ke Le' ]
# for i in users_list:
#     print(f"Hi, {i}! Welcome to Nowcoder!")
# print("Happy Programmers' Day to everyone!")

# number_list = [i for i in range(10,51)]
# print(number_list)
# print(number_list[0],end = " ")
# print(number_list[-1])

# my_values = input()
# my_list = [int(i) for i in my_values.split()]
# for i in my_list:
#     print(i,end = " ")
# print("\n",end = "")
# print(sum(my_list),end = " ")
# average = sum(my_list)/len(my_list)
# print(f"{average:.1f}")

# my_list = [i for i in range(0,19,2)]
# for i in my_list:
#     print(i)

# my_list = [i  for i in range(5,51,5)]
# for i in my_list:
#     print(i)

# my_list = []
# for i in range(1,11):
#     my_list.append(2**i)
# for i in my_list:
#     print(i)

# food_list = ['apple', 'ice cream', 'watermelon', 'chips', 'hotdogs', 'hotpot']
# while food_list:
#     del food_list[-1]
#     print(food_list)

# users_list = ['Niuniu','Niumei','HR','Niu Ke Le','GURR','LOLO']
# for i in users_list:
#     if i == 'HR':
#         print(f"Hi, {i}! Would you like to hire someone?")
#     else:
#         print(f"Hi, {i}! Welcome to Nowcoder!")

# my_list = [3, 45, 9, 8, 12, 89, 103, 42, 54, 79]
# guess_num = int(input())
# for i in my_list:
#     if i == guess_num:
#         break
#     else:
#         print(i)

# my_list = list(range(1,16))
# for i in my_list:
#     if i == 13:
#         continue
#     else:
#         print(i,end = " ")

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# m = int(input())
# for i in range(3):
#     for j in range(3):
#         matrix[i][j] = matrix[i][j] * m
# print(matrix)

# m = input()
# n = input()
# name = (m,n)
# print(name)

# entry_form = ('Niuniu','Niumei')
# print(entry_form)
# try:
#     entry_form[1] = 'Niukele'
# except TypeError:
#     print('The entry form cannot be modified!')

# list_values = input()
# my_tuple = tuple(list_values.split(" "))
# print(my_tuple[:3])

# name = ('Tom', 'Tony', 'Allen', 'Cydin', 'Lucy', 'Anna')
# print(name)
# n = input()
# if n in name:
#     print('Congratulations!')
# else:
#     print('What a pity!')

# tuple_1 = (1,2,3,4,5)
# print(tuple_1)
# print(len(tuple_1))
# tuple_2 = (6,7,8,9,10)
# print(tuple_1 + tuple_2)
# print(len(tuple_1 + tuple_2))

# nums = set([1,2,2,3,3,3,4])
# print(nums)