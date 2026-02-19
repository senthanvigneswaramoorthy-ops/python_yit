def studentdetails(name,age,grade):
    print(f"student is {name} {age} {grade}")
n=int(input("Enter the number of students:"))
for x in range(n):
    name1=input("Enter the name of student:")
    age1=int(input("Enter the age of student:"))
    grade1=int(input("Enter the grade of student:"))
    studentdetails(name1,age1,grade1)
    