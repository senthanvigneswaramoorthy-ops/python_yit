subjects=["mathematics","science","tamil","ict",]
print(subjects)
print(type(subjects))
print(subjects[0])
print(subjects[-1])
print(len(subjects))
subjects[0]="history"
print(subjects)
subjects.append("physics")
print(subjects)
for x in subjects:
    print(x)
i=0
while i<len(subjects):
    print(subjects[i])
    i+=1