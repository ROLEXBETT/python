# Python list
# a list in python, iks a collection of items that ae ordered in a certain way
# a list is introduced by the use of square brackets []
# the items of a list are stored inside of indexes NB . in programing we start counting from index zero (0) . bmw, benze, hiance, ...
# a list is mutable i.e the content of a list can be changed.

cars = ["BMW", "Benze", "Hiance", "Prado", "Probox", "Mclarel", "Range"]

print(cars)
print(type(cars))

# accesing items of a list
print(cars[2])
print("the car on index four is;",cars[4])

# List slicing - This is creating a list from a give bigger list
print(cars[4:])

# printing from index zero to index three
print(cars[:4])

# printing from hiance to probox
print(cars[2:5])

# List - Mutability
# we use the functio append to add an item at the end of a list
cars.append("Mercedes")
print(cars)

cars.append("subaru")
print(cars)

# we use the pop function to remove an item at the end of the list
cars.pop()
print(cars)

# we can use an index to add item to a list
cars[5] = "Pajero"
print(cars)

# we can use the sort function to sort out items in alphabetical order
cars.sort()
print(cars)

