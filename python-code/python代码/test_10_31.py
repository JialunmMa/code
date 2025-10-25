#第十五届蓝桥杯B组省赛试题
#试题A
# def trans_2(a):
#     c = 0
#     while a:
#         b = a % 2
#         a = a // 2
#         c = c + b
#     return c
#
# def trans_4(a):
#     c = 0
#     while a:
#         b = a % 4
#         a = a // 4
#         c = c + b
#     return c
#
# count = 0
# for i in range(1,2025):
#     trans_2(i)
#     trans_4(i)
#     if trans_2(i) == trans_4(i):
#         count += 1
# print(count)
from multiprocessing.forkserver import set_forkserver_preload

#试题B
# a = 10 ** 9 + 7
# b = pow(9,10000) - 2 * pow(8,10000) + pow(7,10000)
# print(b % a)

#试题C


# m,n = input().split(" ")
# print(m)
# print(n)

# m,n = map(int,input().split(" "))
# print(f'{m},{n}')
# print(type(m))

# def trans(n,x):
#     a = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     b = []
#     while n:
#         y = n % x
#         b = b + [y]
#         n = n / x
#
#     b.reserve()

#NP20
# my_list = input().split(" ")
# my_list.append('Alien')
# print(my_list)

#NP21
# mylist = input().split()
# mylist.insert(0,'Allen')
# print(mylist)

#NP22
# my_list = input().split()
# del my_list[0]
# print(my_list)

#NP23
# mylist = input().split()
# name = input()
# mylist.remove(name)
# print(mylist)

# #NP24
# my_list = input().split()
# my_list.pop()
# my_list.pop()
# my_list.pop()
# print(my_list)

#NP25
# letter = ['p','y','t','h','o','n']
# letter_1 = sorted(letter)
# print(letter_1)
# print(letter)
# letter.sort(reverse = True)
# print(letter)

#NP26
# num = [3, 5, 9, 0, 1, 9, 0, 3]
# num.reverse()
# print(num)

#NP27
# name = ['Niumei', 'YOLO', 'Niu Ke Le', 'Mona']
# friends = []
# friends.append(name)
# food =  ['pizza', 'fish', 'potato', 'beef']
# friends.append(food)
# number = [3, 6, 0, 3]
# friends.append(number)
# print(friends)

#NP28
# number = int(input())
# arr = [1,1,1,1]
# for i in range(0,4):
#     arr[i] = ((number % 10) + 3 ) %9
#     number = number // 10
# arr.reverse()
# print(arr[2],arr[3],arr[0],arr[1],sep ="")

