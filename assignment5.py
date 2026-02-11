#Function Without Parameters
#Create a function that
#• Takes no parameters
#• Uses arithmetic operators to calculate the area of a rectangle
#• Prints the result

def greet_the_world():
     "Hello, world! I are you enjoying coding or it's enjoying you?"

print(greet_the_world())


def calculate_rectangle_area():
    # Define the dimensions within the function
    length = 10
    width = 5
    
    # Use the multiplication arithmetic operator
    area = length * width
    
    # Print the result
    print(f"The area of the rectangle is: {area}")

calculate_rectangle_area()


#Qn 2: Function With Parameters
#Create a function that:
#• Accepts two numbers as parameters
#• Returns their sum, difference, product, and division

def calculate_all(num1, num2):
    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    
    return addition, subtraction, multiplication, division

add, sub, mult, div = calculate_all(20, 5)

print(f"Sum: {add}")
print(f"Difference: {sub}")
print(f"Product: {mult}")
print(f"Division: {div}")

#Qn 3: Control Statement (if...elif...else)
#Write a function that:
#• Accepts a number (use input function)
#• Checks whether the number is:
#• Positive
#• Negative
#• Zero

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

#Qn 4: Loop with Arithmetic
#Write a function that:
#• Accepts a number n
#• Uses a for loop
#• Calculates the sum of numbers from 1 to n

def sum_with_formula_check():
    """
    Calculates sum using for loop and verifies with mathematical formula.
    Formula: sum = n * (n + 1) / 2
    """
    n = int(input("Enter a number: "))
    
    # For loop method
    loop_sum = 0
    for i in range(1, n + 1):
        loop_sum += i
    
    # Formula method
    formula_sum = n * (n + 1) // 2
    
    print(f"Sum using for loop: {loop_sum}")
    print(f"Sum using formula: {formula_sum}")
    print(f"Both methods match: {loop_sum == formula_sum}")
    
    return loop_sum

sum_with_formula_check()

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

