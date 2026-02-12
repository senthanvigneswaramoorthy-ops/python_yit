num_1=int(input("Enter a number:"))
num_2=int(input("Enter a number:"))
x=int(input("Enter function number :"))
if 7>=x>0:
    if x==1:
        a= num_1+num_2
        print("num_1+num_2=",a)
    if x==2:
        a=num_1-num_2
        print("num_1-num_2=",a)
    if x==3:
        a=num_1*num_2
        print("num_1*num_2=",a)
    if x==4:
        a=num_1/num_2
        print("num_1/num_2=",a)
    if x==5:
        a=num_1//num_2
        print("num_1//num_2=",a)
    if x==6:
        a=num_1%num_2
        print("num_1%num_2=",a)
    if x==7:
        a=num_1**num_2
        print("num_1**num_2=",a)    
else:
    print("Enter a valid function number")    
