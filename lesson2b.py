#  TUPLE
# a tuple is an imutable
# to introduce a tuple, we use the paranthesis ()

counties = ("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")

print(counties)

# slicing of tuples
print(counties[3:])

# accessing items of a tuple by use of indexes
print(counties[5])

#NB : Below will generate an error
counties.append("Machakos")
print(counties)