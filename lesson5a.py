# Python Function
# They are a block of code/ statements that performs a given task/action. They can be reused through out the program to perfom 
# Functions are definned using the def keyword
# we have two main types   i.e
# 1. In-built functions -> they come preinstalled with the interpreter i.e print(), pop, range, append
# 2. user-defined function  they are created by a programmer to solve a given task
# To define a funcyion you need to give it a name followed by parethesis.
# for the funtion body it is usiualy imntened and to invoke a fuction we use the function name.

def greetings():
    print("Hello, how are you?")


#below we call the function by use of its name
greetings()

print("==============")
# Addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ",sum)
addition()



print("==============")
# create a function that  is able to multiply three values
# multiplication function
def multiplication():
    num1 = 2
    num2 = 7
    num3 = 5
    product = num1 * num2 * num3
    print("The multiple of the numbers is: ",product)
multiplication()

print("==============")
# Below is a division function
def divide():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    quotient = number1 / number2
    print("The answer is: ",quotient)
    print("-------")

    for function in range(3):
        divide()