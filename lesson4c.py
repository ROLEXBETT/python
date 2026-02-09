#a a for loop can also be used to iterate through a list, tuple, string or even a dictionary..

name = "Rolex"

for letter in name:
    if letter == "l":
       print("the letter l")
    else:\
        print(letter)

print("==================")
# Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Embu", "Meru"]

print(counties)

for county in counties:
    print(county)
    
print("==================")
if "Nakuru" in counties:
 for county in counties:
    print("Nakuru is in the list of counties")
else:
    print("Nakuru is not in the list of counties")


print("==================")
# the for loop can also be used to iterate through a dictionsnry

player = {
   "name": "Mmbappe",
   "age": 25,
   "teams": ["PSG", "Monaco", "France"],
   "nationality": "French"
}

for key in player:
   print(key)

print("==================")
for values in player:
   print(player[values])

   print(player[name])

   print("==================")
   #loop through the teams the player has played for
   print(player["teams"])

   