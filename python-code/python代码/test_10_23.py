# language = 'python  '
# print(f"{language}1")
# print(f"{language.rstrip()}1")

# url = 'https://nostarch.com'
# print(url)
# print(url.removeprefix('https://'))

# # 练习2.3
# name = 'Eric'
# print(f"Hello {name},would you like to learn some python today?")

# # 练习2.4
# name = 'xiao ming'
# print(name.title())
# print(name.upper())
# print(name.lower())

# # 练习2.5
# print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')

# a = 1_000_000_000
# print(a)

# x,y,z = 1,2,3
# print(x,y,z)

# my_list = [1,2,3,4,5,6,7,8,9]
# for i in my_list:
#     print(i)

# for i in range(1,9,2):
#     print(i)

# my_list = list(range(1,9))
# print(my_list)

# my_list = []
# for i in range(1,11):
#     my_list.append(i ** 2)
# print(my_list)

# my_list = [i ** 2 for i in range(1,11)]
# print(my_list)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# for i in players[:3]:
#     print(i)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# players_1 = players[:]
# print(players_1)

# user_0 = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }
# for keys,values in user_0.items():
#     print(f"Keys = {keys}")
#     print(f"Values = {values}\n")

# user_0 = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }
# for keys in user_0:
#     print(f"keys:{keys}")

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'rust',
#  'phil': 'python',
#  }
# for name in sorted(favorite_languages.keys()):
#     print(f"{name}")

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'rust',
#  'phil': 'python',
#  }
# print(favorite_languages.values())

# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'rust',
#  'phil': 'python',
#  }
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#  print(language.title())

# dict_1 = {"name":'xiaoming','age':15}
# dict_2 = {"name":'xiaoguang','age':18}
# dict_3 = {'name':'xiaomei','age':19}
# my_list = [dict_1,dict_2,dict_3]
# for i in my_list:
#     print(i)

# # 存储顾客所点⽐萨的信息
# pizza = {
# 'crust': 'thick',
# 'toppings': ['mushrooms', 'extra cheese'],
# }
# # 概述顾客点的⽐萨
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#  print(f"\t{topping}")

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# prompt = '您给我们提供你的名字，我们可以录入系统'
# prompt += '\n您的名字：'
# name = input(prompt)
# print(f'您的名字是：{name}')


# while True:
#     name = input('请输入您的姓名：')
#     print(name)
#     if name == 'quit':
#         break

# unused = [1,2,3,4,5]
# used = []
# while unused:
#     using = unused.pop()
#     print(f'The using number is {using}')
#     used.append(using)
# for i in used:
#     print(i)

# my_list = [1,1,1,2,5,4,6,1,2]
# while 1 in my_list:
#     my_list.remove(1)
# print(my_list)

# responses = {}
# # 设置⼀个标志，指出调查是否继续
# polling_active = True
# while polling_active:
#     # 提⽰输⼊被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday?")
#     # 将回答存储在字典中
#     responses[name] = response
#     # 看看是否还有⼈要参与调查
#     repeat = input("Would you like to let another person respond?(yes/no) ")
#     if repeat == 'no':
#         polling_active = False
# # 调查结束，显⽰结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

# def function(name):
#     print(f'Hello,{name}!')
# function('xiaoming')

# def function(name,age):
#     print(f'My name is {name}')
#     print(f'age{age}\n')
# function('xiaoming',19)
# function('xiaoliang',20)

# def function(name,age):
#     print(f'My name is {name}')
#     print(f'age{age}\n')
# function(age = 18,name = 'xiaoming')

# def function(name,age = 18):
#     print(f'My name is {name}')
#     print(f'Age{age}\n')
# function(name = 'xiaoming')
# function('xiaoming')

# def function(name,age):
#     return name
#
# name = function('xiaoming',18)
# print(name.title())

# def function(name, age, sex = ''):
#     if age:
#         print(f"My name is {name},I am {age} years old.I am a {sex}")
#     else:
#         print(f"My name is {name},I am {age} years old.")
#
# name_1 = input('请输入您的姓名->')
# age_1 = input("您的年龄->")
# print('如果您不想输入性别，请不要输入。')
# sex_1 = input('您的性别->')
#
# function(name_1,age_1,sex_1)

