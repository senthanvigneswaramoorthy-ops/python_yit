m=[
    [55,65,75]
    [75,85,95]
    [95,65,35]
    ]
student=["Joseph","Peter","Philips"]
maths=0
science=0
english=0
total=0
average=0
print("Student","\t","Maths","\t","Science","\t","English","\t","Total","\t","Average")
print("-----------------------------------------------")
for x in range(3):
    for y in range(3):
        print(f"{student[x]},\t,{m[x][y]},\t,{scie