# # 存储顾客所点⽐萨的信息
# pizza = {
# 'crust': 'thick',
# 'toppings': ['mushrooms', 'extra cheese'],
# }
# # 概述顾客点的⽐萨
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#  print(f"\t{topping}")

# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
# hello()
# def id(name,age = 18):
#     print(f"这个人的姓名是{name}")
#     print(f"这个人的年龄是{age}")
# na = input("请输入您的姓名->")
# ag = int(input("请输入您的年龄->"))
# id(name = na)

# def add(a,b):
#     """写一个加法计算器。"""
#     return a + b
# title = "请输入两个数，中间用空格隔开->"
# m,n = map(int,input(title).split(" "))
# sum_1 = add(m,n)
# print(f"这两个是相加的值是：{sum_1}")

# def score(sco):
#     """求总成绩"""
#     return sum(sco)
# i = input("请输入该名学生的学号->")
# ti = "请输入该学生的三科成绩，用空格隔开->"
# a,b,c = map(int, input(ti).split(" "))
# score_list = [a,b,c]
# score_sum = score(score_list)
# print(f"学号为{i}的学生的总成绩为{score_sum}")

# def sum_score(sco):
#     sco.remove(max(sco))
#     sco.remove(min(sco))
#     return sum(sco)
# name = input("请输入该名选手的姓名->")
# ti = "请输入该为选手的五个成绩->"
# a,b,c,d,e = map(int,input(ti).split(" "))
# score_list = [a,b,c,d,e]
# score_sum = sum_score(score_list)
# ave = score_sum / 3
# print(f"{name}选手的最终成绩为{ave:.2f}")

# def sum_score(sco):
#     sco.remove(max(sco))
#     sco.remove(min(sco))
# name = input("请输入该名选手的姓名->")
# ti = "请输入该为选手的五个成绩->"
# a,b,c,d,e = map(int,input(ti).split(" "))
# score_list = [a,b,c,d,e]
# sum_score(score_list)
# print(score_list)

# def sum_score(sco):
#     sco.remove(max(sco))
#     sco.remove(min(sco))
# name = input("请输入该名选手的姓名->")
# ti = "请输入该为选手的五个成绩->"
# a,b,c,d,e = map(int,input(ti).split(" "))
# score_list = [a,b,c,d,e]
# sum_score(score_list[:])
# print(score_list)

# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     """创建⼀个字典，其中包含我们知道的有关⽤户的⼀切"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
# print(user_profile)

# import score
# name = input("请输入该名选手的姓名->")
# ti = "请输入该为选手的五个成绩->"
# a,b,c,d,e = map(int,input(ti).split(" "))
# score_list = [a,b,c,d,e]
# score_sum = score.sum_score(score_list)
# ave = score_sum / 3
# print(f"{name}选手的最终成绩为{ave:.2f}")

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hello,my name is {self.name}, and I am {self.age} years old.")
#
# person_1 = Person("xiaoming",18)
# person_2 = Person("xiaoliang",20)
#
# person_1.greet()
# person_2.greet()

# class Car:
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化描述汽车的属性"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 50
#
#     def odometer_update(self,miles):
#         if miles >= self.odometer_reading:
#             self.odometer_reading = miles
#             print(f"This car has {self.odometer_reading} miles on it.")
#         else:
#             print("You can't roll back an odometer!")
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
# mile = int(input("请输入里程数->"))
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_update(mile)

# class Car:
#     def __init__(self,make,model,year,odometer_reading = 0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = odometer_reading
#
#     def odometer_add(self,miles):
#         if miles >= 0:
#             self.odometer_reading += miles
#             print(f"The{self.make}{self.model} made in {self.year} has run {self.odometer_reading} already.")
#         else:
#             print("You can't roll back an odometer!")
#
# mile = int(input("请输入初始里程数->"))
# my_new_car = Car('Audi', 'A4', 2016,mile)
# mile_add = int(input("请输入增加的里程数->"))
# my_new_car.odometer_add(mile_add)

# class Score:
#     def __init__(self,subject:list[str],score:list[int]):
#         self.subject = subject
#         self.score = score
#     def score_print(self):
#         for i in range(0,6):
#             print(f"The average score of {self.subject[i]} is {self.score[i]}")
#
# all_subject = ["Chinese","Maths","English","Physics","Chemistry","Biology"]
# all_score = [122,130,137,86,92,95]
# the_full_score = Score(all_subject,all_score)
# the_full_score.score_print()

# class Score:
#     def __init__(self,subject,score):
#         self.subject = subject
#         self.score = score
#     def score_print(self):
#         for i in range(0,6):
#             print(f"The average score of {self.subject[i]} is {self.score[i]}")
#
# class GradeOneScore(Score):
#     def __init__(self,subject,score):
#         super().__init__(subject,score)
#     def print_1(self):
#         print("-------------------------------------")
#         print("Scores of the grade one:")
#
# all_subject = ["Chinese","Maths","English","Physics","Chemistry","Biology"]
# all_score = [122,130,137,86,92,95]
# all_score_1 = [130,140,135,90,95,97]
# the_full_score = Score(all_subject,all_score)
# the_full_score.score_print()
# the_full_score_1 = GradeOneScore(all_subject,all_score_1)
# the_full_score_1.print_1()
# the_full_score_1.score_print()

