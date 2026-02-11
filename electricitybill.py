u=int(input("Enter units used:"))
if 90>=u>0:
    a=u*7
elif 150>=u>90:
    a=90*7+(u-90)*10
elif 300>=u>150:
    a=90*7+60*10+(u-150)*15
elif u>300:
    b=90*7+60*10+150*15
    a=b+b*3/100
    #type casting
print("Electricity bill: Rs"+str(a))