student = {}

studentName = input("Enter your student's name please.")
student["name"] = studentName

studentAge = input("Enter your student's age please.")
student["age"] = studentAge

studentGrade = input("Enter your student's grade please.")
student["grade"] = studentGrade

#Loops until done is entered, input all hobbies.
hobby = input("Input your student's hobbies one by one, and when you're finished, enter done: ").lower()
hobbies = []
while not hobby == "done":
    hobbies.append(hobby)
    hobby = input("Input your student's hobbies one by one, and when you're finished, enter done: ").lower()
   

student["Hobbies"] = hobbies

print(student)
