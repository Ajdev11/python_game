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
import this

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


numbers = [1, 2, 3, 4, 5]

count = len(numbers)
if count > 3:
    print(f"The number of list is {count}")

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist[0] = ['Grapes']
thislist.insert(1, "Mango")
if 'apple' in thislist:
    print("YES i am Present in this list")
else:
    print('I have been replaced by something else')
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[2:4])
print(thislist[:4])

# append is use to add an item to the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# to extend the items from another list 
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)