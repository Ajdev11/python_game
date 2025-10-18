# animals = ["dog", "cat", "bird"]
# animals[2] = "fish"
# animals.append("horse")
# animals.extend(["cow", "sheep"])
# animals += ["pig", "goat"]
# animals.remove("dog")
# animals.insert(0, "ragnar")
# animals.pop()
# print(animals)




# tuples, sets, dictionaries and list

# list
# animals =  ["dog", "cat", "mouse", "bird", "snake", "turtle", "fish", "lizard", "frog", "toad"]
# # print(animals)

# # tuple
# animals_tuple = ("dog", "cat", "mouse", "bird", "snake", "turtle", "fish", "lizard", "frog", "toad")
# # print(animals_tuple)

# # set
# animals_set = {"dog", "cat", "mouse", "bird", "snake", "turtle", "fish", "lizard", "frog", "toad"}
# animals_set2 = {"dog", "cat"}
# mod = animals_set < animals_set2
# # print(mod)

# # dictionary
# names = {"first_name": "John", "last_name": "Doe", "age": 30, "city": "New York"}
# print(names)


# functions
# def greet(name):
#     print(f"Hello, {name}!")
#     return name

# names_of_people = greet("Moses is a good boy")
# names_of_people = greet("John is a good boy")
# names_of_people = greet("Jane is a good girl")


# def name_age(name, age):
#     print(f"Hello, {name}! You are {age} years old.")
#     # return name, age

# name_age("Moses", 20)
# name_age("John", 21)
# name_age("Jane", 22)

# def change(value):
#     value["name"] = "olaseni"

# val = {"name":"dumdum"}
# change(val)
# print(val)



# def age(years):
#     if years >= 30:
#         return "Moses is getting old"
#     else:
#         return "he is still young"

# result = age(100)
# print(f"i think {result} ")


# def userAge():
#    choice = int(input("Enter your age: "))
#    return choice
# age = userAge()
# if age >= 18:
#    print(f"Your age is {age}, you are an adult")
# elif age <= 18:
#     print(f"Your age is {age}. you are a minor")
# else:
#    print("enter a valid age")


# nested function 
# def count():
#    count = 0
#    def increment():
#       nonlocal count
#       count = count + 10000
#       print(count)
#    return increment()

# global variable

# age = 9
# def ageCount():

#     print(age)
   
# result = ageCount()

# objects

# items = [1,2]
# items.append(3)
# print(items)


# loops

# while loops

# Condition = True
# while Condition == True:
#    print("condition is true")
#    Condition = False

# count = 0
# while count < 20:
#    print("Condition is true")
#    count = count + 1
#    # count += 1
# print("It is done iterating")


# for loops (commonlybused to iterate an item in a list)

# wildAnimals = ["lion", "monkey", "tiger", "bear", "snakes", "humans"]
# for index, animals in enumerate(wildAnimals):
   
#    print(index, animals)

# for num in range(40):
#    print(num)


# items = [1,2,3,4,5]

# for item in items:
#    print(item)

# to get the indec of this items we can also say


# items = [1,2,3,4,5]

# for index, item in enumerate(items):
#    print(index, item)

# items = [1,2,3,4,5]
# for item in items:
#    if item == 3:
#       break
#    print(item)

# items = [1,2,3,4,5]
# for item in items:
#    if item == 3:
#       continue
#    print(item)


# classes

# one important thing about class is the ability to inherit
# examole


# class Animals:
#    def walk(self):
#       print("walking.....")


# class Dog(Animals):
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def barking(self):
#       print("wooof")
#       return


# ragnar = Dog("German Shepherd", 100)
# print(ragnar.name)
# print(ragnar.age)
# ragnar.barking()
# ragnar.walk()


# modules
# every pythin file is a module

# lambda function
# import numbers
# from tokenize import Double


# lambda num: num * 2
# multiply = lambda a, b: a * b
# print(multiply(2, 4))

# map, filter and reduce
# numbers = [4, 6, 9]
# # double = lambda g: g * 5
# result = map(lambda g: g * 5, numbers)
# print(list(result))

# filter 
# numbers = [2, 4, 6, 8, 10]
# result = filter(lambda n: n % 2==0, numbers)
# print(list(result))

# reduce
# reduce is used tocalculate a value out of a sequence 
from functools import reduce

expenses = [("dinner", 90), ("breakfast", 120)]

sum = reduce(lambda a,b: a[1] + b[1], expenses)
print(sum)





















# the main purpose of a function is to avoid code duplication and the difference between a paramter
#  and an argument is that a parameter is the variable in the function definition and an argument
#  is the value passed to the function when it is called
# return statement is used to return a value from a functio1n. if no return statement is used, the function will return None
# return statement is used to exit a function
