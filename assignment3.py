
# Store gross salary in a variable
gross_salary = float(input("Enter your gross salary (Ksh): "))

# Determine monthly contribution using if-else statements
if gross_salary < 6000:
    contribution = 150
elif gross_salary <= 7999:
    contribution = 300
elif gross_salary <= 11999:
    contribution = 400
elif gross_salary <= 14999:
    contribution = 500
elif gross_salary <= 19999:
    contribution = 600
elif gross_salary <= 24999:
    contribution = 750
elif gross_salary <= 29999:
    contribution = 850
elif gross_salary <= 49999:
    contribution = 1000
elif gross_salary <= 99999:
    contribution = 1500
else:
    contribution = 2000

# Output the result
print(f"Your NHIF monthly contribution is: Ksh {contribution}")

