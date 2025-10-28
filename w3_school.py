# global variables are var declared outside a funct and call within a func
# e.g

myName = "Moses Ogunsemore"

def name():
    print("Your name is " + myName)

name()

# also you cna have a local var

def surName():
    x = "i am a technocrats"
    print(x)
surName()

# you can also however chnage the global var to a local var


y = "Italian course"
def courseName():
    global y
    y = "Jupiter nodes"
    print(y)
courseName()


# i can also check the tyoe of datatype using casting 

#  e,g

z = "Moses is a programmer"

print(type(z))

# list

fruits = ["Banana", "Apple"]

# tuple

fruits = ("banana", "manago")

# dict

fruits = {"age": 14, "name":"Moses"}

# set

fruits = {"age", "moses"}

# naming convention in python are in 3 forms
# camel case, pascal case and snake case

# camel case
myNameIs = 'Moses ogunsemore'

# pascal case

MyNameIs = 'Moses OgUNSEMORE'

# snakecase

my_name_is = 'Moses Ogunsemore'

# random function 


import random

print(random.randrange(1, 10))