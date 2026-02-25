m=[
    [55,65,75],
    [75,85,95],
    [95,65,35]
    ]
student=["Joseph","Peter","Philips"]
total=[]
average=[]
results=[]
for x in range(3):
    tot=0
    ave=0
    for y in range(3):
        tot+=m[x][y]
    total.append(tot)
    ave=tot/3
    average.append(ave)
    if ave>80:
        res="Supermerit"
    elif ave>65:
        res="Optimi"
    else:
        res="None"
    results.append(res)
print(f"{"studentname"<15} {"Maths"<9} {"Science"<11} {"English"<11} {"Total"<9} {"Average"<11} {"Result"<10})
print("-----------------------------------------------------------------------------------------------------")
for x in range(3):
    print(f"{student[x]<15},{m[x][0]<9},
    {m[x][1]},\t,{m[x][2]}")
    
    
    