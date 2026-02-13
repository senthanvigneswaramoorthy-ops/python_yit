num_1=int(input("Enter a number:"))
num_2=int(input("Enter a number:"))
x=int(input("Enter a valid function number:"))
match x:
    case 1:
        print("num_1+num_2=",num_1+num_2)
    case 2:
        print("num_1-num_2=",num_1-num_2)
    case 3:
        print("num_1*num_2=",num_1*num_2)
    case 4:
        print("num_1/num_2=",num_1/num_2)
    case _:
        print("Enter a valid function number")
