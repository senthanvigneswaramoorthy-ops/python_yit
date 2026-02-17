n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
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
match  :
    case +:
        print(a)
    case -:
        print(b)
    case *:
        print(c)
    case /:
        print(d)
    case _:
        print("Enter a valid function number")
