# Below is a grading system based on what a student will have gotten
marks = int(input("enter student marks: "))
# print("the entered marks is ", marks)
if marks < 30:
    print("below average")
elif marks >=30 and marks < 40:
    print("Average")
elif marks >40 and marks <70:
    print("Above average")
else:
    print("excellent")