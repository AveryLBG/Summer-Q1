numberGrade = int(input("What is your number grade? 1-100."))
letterGrade = ""
if (numberGrade >= 90):
    letterGrade = "A"
elif (89 >= numberGrade >= 80):
    letterGrade = "B"
elif (79 >= numberGrade >= 70):
    letterGrade = "C"
elif (69 >= numberGrade >= 60):
    letterGrade = "D"
else:
    letterGrade = "F"

if letterGrade == "A":
    print("You got an " + letterGrade)
elif letterGrade == "F":
    print("You got an " + letterGrade)
else:
    print("You got a " + letterGrade)