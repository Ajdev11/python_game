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

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists