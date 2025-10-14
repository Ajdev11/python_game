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
def greet(name):
    print(f"Hello, {name}!")

greet("Moses")
greet("John")
greet("Jane")