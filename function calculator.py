n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
x=int(input("Enter number:"))
def add(n1,n2):
    return n1+n2
a=add(n1,n2)
def subract(n1,n2):
    return n1-n2
b=subract(n1,n2)
def multiply(n1,n2):
    return n1*n2
c=multiply(n1,n2)
def divide(n1,n2):
    return n1/n2
d=divide(n2,n2)
match x :
    case 1 :
        print(a)
    case 2:
        print(b)
    case 3 :
        print(c)
    case 4 :
        print(d)
    case _ :
        print("Enter a valid number")
        