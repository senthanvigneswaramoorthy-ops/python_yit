marks=int(input("Enter the marks:"))
if 100>=marks>=0:
   if marks>=75:
      print("A")
   elif marks>=65:
       print("B")
   elif marks>=55:
       print('C')
   elif marks>=45:
       print("S")
   else:
      print("F")
else:
    print("Enter Valid Marks")