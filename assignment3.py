# Below is a program that calculates the monthly contribution an employee should make to the National Health Insuarance as per the grossincome
grosssalary = int(input("Enter your salary here: "))
if grosssalary > 0 and grosssalary <= 5999:
    print("Your monthly contribution is Ksh 150.00")
elif grosssalary > 5999 and grosssalary <= 7999:
    print("Your monthly contribution is Ksh 300.00")
elif grosssalary > 7999 and grosssalary <= 11999:
    print("Your monthly contribution is Ksh 400.00")
elif grosssalary > 11999 and grosssalary <= 14999:
    print("Your monthly contribution is Ksh 500.00")
elif grosssalary > 14999 and grosssalary <= 19999:
    print("Your monthly contribution is Ksh 600.00")
elif grosssalary > 19999 and grosssalary <= 24999:
    print("Your monthly contribution is Ksh 750.00")
elif grosssalary > 24999 and grosssalary <= 29999:
    print("Your monthly contribution is Ksh 850.00")
elif grosssalary > 29999 and grosssalary <= 49999:
    print("Your monthly contribution is Ksh 1000.00")
elif grosssalary > 49999 and grosssalary <= 99999:
    print("Your monthly contribution is Ksh 1500.00")
else:
    print("Your monthly contribution is Ksh 2000.00")
