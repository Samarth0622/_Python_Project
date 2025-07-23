# fruits = ["apple", "banana", "cherry"]
# print("apple" not in fruits)

# num1= float(input("enter a number:"))
# print(num1)
# print(type(num1))

# num = int(input("enter a number:"))

# if num < 10:
#     print("student is not adult ")

# elif num >= 18 and num <=100 :
#     print("student is adult")

# elif num >100:
#     print("student is not a human")


# num1 = float(input("enter a number:"))
# num2 = float(input("enter a number:"))

# print(f"result of addition is :{num1 + num2}")


# name = "samarth"
# # name = "kunal"
# # print(name[4])
# print(name)

# name = "samarth@123wrwerwe"


# for i in range(len(name)):
# if len(name) <= 11:
#     print("successfully login")
# else:
#     print("login failed, please try again")


# my_dic["college"] = "radhe college"
# del my_dic["college"]

# my_dic["age"] = 23
# print(my_dic)

# print(my_dic)
# data = my_dic.get("address","not fount data")
# print(data)
# key = my_dic.keys()
# print( list(key))


# square = {x : x*2 for x in range(1,6)}
# print(square)

# my_dic = {
#     "name" : "samarth",
#     "age": 22,
#     "pin":244712,
#     "address": "gurgaon"
# }

# for key in my_dic.get(["name"]):
#     print(key)


# def greet(name,city="delhi"):
#     print(f"hello world {name} and i living in {city}")

# greet(name="kunal",city="jaspur")

# def get_value(func):
#     def wrapper():
#         print("before fuction cll")
#         func()
#         print("after function call")
#         return wrapper
 
# @get_value
# def say_hello():
#     print("hello world")

#     say_hello()

# for i in range (1,11):
#     if i%2 == 0:
#         print(f"{i} ")
#     # else:
#     #     print(f"{i} odd number",)

# class student:
#     def set_detail(self , name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"student name is {self.name} and age is {self.age}")

# s1 =  student()
# s2 = student()

# s1.set_detail( "samarth", 22)
# s2.set_detail("kunal", 23)

# s1.display()
# s2.display()


# class company:
#     def __init__(self, emp_name, emp_id):
#         self.emp_name = emp_name
#         self.emp_id = emp_id

# c1=company("samarth",101)
# print(c1.emp_name , c1.emp_id)