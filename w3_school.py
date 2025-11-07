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



# List is a collection which is ordered and changeable. Allows duplicate members.
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

# loop list
# for loop is used to loop tyhrough items in a list and the list are dosplayed one after the other 

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


# while loop is more condtional, the statement has to be TRUE for the block of code to RUN 

thislist = ["apple", "banana", "cherry"]
i = 0

while i < len(thislist):
    print(thislist[i])
    i += 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
#  short hand form of using or loops, in this we add the [] to cover the print the statement and the ew variable in ()
thislist = ["apple", "banana", "cherry", "Watermelon"]
[print(x) for x in thislist]


# to print a newlist that contains certain elements
fruits = ["apple", "banana", "cherry", "Watermelon"]
newList = []

for x in fruits:
    if "a" in x:
        newList.append(x)

print(newList)


# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# or we can use the extend method

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# to print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))   

# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# add tuple to a tuple 

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Tuples are unchangeable, so you cannot remove 
# items from it, but you can use the same workaround as we used for changing and adding tuple items:


# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# The del keyword can delete the tuple completely:

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple) 
#this will raise an error because the tuple no longer exists

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i += 1

# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Once a set is created, you cannot change its items, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# Check if "banana" is NOT present in the set:

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# Use | to join two sets:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# The values in dictionary items can be of any data type:

# String, int, boolean, and list data types:

thisdict_2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict_2)


# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# there is also another method call get()
y = thisdict.get("model")
z = thisdict.keys()
print(x)
print(y)
print(z)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the chang
print(car)


# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Add a color item to the dictionary by using the update() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# The clear() method empties the dictionary:

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# also you can loop in a dict

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "orange"
for x in thisdict:
  print(x)

# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# or 

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

# Print the name of child 2:

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])


# Python Conditions and If statements
# Python can evaluate many types of values as True or False in an if statement.

# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
#
# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string)

a = 33
b = 200
if b > a:
  print("b is greater than a")


# elif statement 

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Testing multiple conditions:

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

# Day of the week checker:

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

# The Else Keyword
# The else keyword catches anything which isn't caught by the preceding conditions.

# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Checking if the number  even or odd numbers:

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

# Logical operators are used to combine conditional statements. Python has three logical operators:

# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


# Combining and, or, and not:

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
      print("Discount applies!")


# nested if statements 

# Checking multiple conditions with nesting:

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")



# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass


# Match

# Instead of writing many if..else statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.

# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block



day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:


day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


# or we can also have somethinmg like this 

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")


# You can add if statements in the case evaluation as an extra condition-check:

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")


# Python Loops
# Python has two primitive loop commands:

# while loops
# for loops
# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.


i = 1

while i < 10:
    print(i)
    i += 1


# exact the loops when it gets to 3

i = 1
while i < 6:
    print(f"the value are {i}")
    if i == 3:
        break
    i += 1
