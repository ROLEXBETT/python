#create a python program that is able to determine whether a number entered is an odd or even number

number = int(input("Enter number: "))

if number % 2 == 0:
    print("Number is an even number")
else:
    print("Number is an odd number")
    
# create a python program that determines whether a person can donate blood based on blood and weight of a person.. if the weight is > 50 kgs and age is above 18 ,then the person can donate , else not possible

    age = int(input("Enter age: "))
    weight =float(input("Enter weight: "))

if age >=18 and weight > 50:
   print("Can donate")
else:
   print("Not possible")