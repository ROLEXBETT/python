# Dictionary is adata type that stores data in terms of key-value pair
# it is introduced by the use of curly braces{}
# The values stored inside of dictionary can be of any data type.
# to access the values in a dictionary we use the keys

phonebook = {
"Benson" : "25463739303",
"Mary" : "2537798309889",
"Stephen" : "23453638889"
}
# showing the entire dictionary
print(phonebook)
print(type(phonebook))

#print out Benson's number
print(phonebook["Benson"])

print("=====================")

player = {
    "name" : "Messi",
    "age" : 40,
    "teams" : ["psg", "Barcelona", "Argentina"]
}

#print barcelona - the second team he played for
print(player["teams"][1])

