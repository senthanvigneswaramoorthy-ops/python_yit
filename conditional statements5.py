salary=float(input("Enter basic salary:"))
print("-----------------------")
if salary>0:
    if salary>=100000:
        tax=salary*5/100
        print("Tax percentage is 5%")
    elif salary>=80000:
        tax=salary*3/100
        print("Tax percentage is 3%")
    else:
        tax=00
        print("Tax percentage is 0%")
else:
    print("Enter valid Salary")

print("Basic salary is: ",salary)
print("Tax paid:",tax)
print('Net salary:',salary-tax)
print("------------------------")