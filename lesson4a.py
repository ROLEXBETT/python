# Nested if Statements
# a nested if statement is an if statetement that is contained within another if statement

age = 20
weight = 60

if age > 15:
    if weight > 50:
        print("you can donate blood")
    else:
        print("you cannot donate blood becouse of your weight")
else:
    print("you cannot donate blood because of your age")