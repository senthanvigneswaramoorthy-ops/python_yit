username="KKR"
password=1234
role_1="admin"
role_2="user"
x=input("Enter the username:")
y=int(input("Enter the password:"))
z=input("Enter your role:")
if x==username and y==password:
    print("Login successfull")
    if z==role_1:
        print("Welcome admin")
    else:
        print("Welcome user")
else:
    print("login unsuccessfull")