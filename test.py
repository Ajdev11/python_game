animals = ["dog", "cat", "bird"]
animals[2] = "fish"
animals.append("horse")
animals.extend(["cow", "sheep"])
animals += ["pig", "goat"]
animals.remove("dog")
animals.insert(0, "ragnar")
animals.pop()
# print(animals)




# tuples, sets, dictionaries and list

# list
animals =  ["dog", "cat", "mouse", "bird", "snake", "turtle", "fish", "lizard", "frog", "toad"]
# print(animals)

# tuple
animals_tuple = ("dog", "cat", "mouse", "bird", "snake", "turtle", "fish", "lizard", "frog", "toad")
# print(animals_tuple)

# set
animals_set = {"dog", "cat", "mouse", "bird", "snake", "turtle", "fish", "lizard", "frog", "toad"}
animals_set2 = {"dog", "cat"}
mod = animals_set < animals_set2
# print(mod)

# dictionary
names = {"first_name": "John", "last_name": "Doe", "age": 30, "city": "New York"}
# print(names)


# functions
# def greet(name):
#     print(f"Hello, {name}!")
#     return name

# names_of_people = greet("Moses is a good boy")
# names_of_people = greet("John is a good boy")
# names_of_people = greet("Jane is a good girl")


def name_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    # return name, age

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


def userAge():
   choice = int(input("Enter your age: "))
   return choice
age = userAge()
if age >= 18:
   print(f"Your age is {age}, you are an adult")
elif age <= 18:
    print(f"Your age is {age}. you are a minor")
else:
   print("enter a valid age")








# the main purpose of a function is to avoid code duplication and the difference between a paramter
#  and an argument is that a parameter is the variable in the function definition and an argument
#  is the value passed to the function when it is called
# return statement is used to return a value from a functio1n. if no return statement is used, the function will return None
# return statement is used to exit a function
