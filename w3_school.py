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

# string

name = "Hello wolrd"

# for loop
# slicing
for x in name:
    print(x)
    print(x[: 5])
    print(x[2:6])
    print(x.upper())
# concatenation or combining 

a = 5
b= 10
c= a + b
print(c)

# f string, used for formatting strings

age = 600
text = f"my name is Moses and i am  {age} years old"
print(text)

# boolean representr one or two values

print(10 > 9)
print(9 < 4)

# another example will be 

a = 400
b = 50

if a > b:
    print("A is GREATER than B")
else:
    print("check again")
