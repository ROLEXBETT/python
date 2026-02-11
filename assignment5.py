#Function Without Parameters
#Create a function that
#• Takes no parameters
#• Uses arithmetic operators to calculate the area of a rectangle
#• Prints the result

def area():
    length=5
    width=10
    area=length*width
    print(area)

area()

print("==============")

#Qn 2: Function With Parameters
#Create a function that:
#• Accepts two numbers as parameters
#• Returns their sum, difference, product, and division

def calculate_operation(num1, num2):
    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division

add, sub, mult, div = calculate_operation(20, 5)

print(f"The Sum is: {add}")
print(f"The Difference is: {sub}")
print(f"The Product is: {mult}")
print(f"The Division is: {div}")

print("==========")

print("==============")

#Qn 3: Control Statement (if...elif...else)
#Write a function that:
#• Accepts a number (use input function)
#• Checks whether the number is:
#• Positive
#• Negative
#• Zero

def check_number():
   def check_number():
    # Capture user input
    val = input("Please enter a number: ")
    num = float(val)

    if num > 0:
        print(f"{num} is a Positive number.")
    elif num < 0:
        print(f"{num} is a Negative number.")
    else:
        print("The number is Zero.")

check_number()

print("==============")

#Qn 4: Loop with Arithmetic
#Write a function that:
#• Accepts a number n
#• Uses a for loop
#• Calculates the sum of numbers from 1 to n

def sum_of_numbers():
  def sum_of_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("The sum of numbers from 1 to", n, "is:", sum)

n = int(input("Enter a number: "))
sum_of_numbers(n)

print("====================")


#Qn 5: While Loop
#Write a function that:
#• Accepts a number (Use input() function)
#• Calculates the square of numbers from 1 up to that number

def calculate_squares():
    number = int(input("Enter a number: "))
    
    i = 1
    while i <= number:
        print(f"The square of {i} is {i ** 2}")
        i += 1

calculate_squares()

