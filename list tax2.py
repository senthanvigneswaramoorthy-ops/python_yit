months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sal=[60000,55000,45000,70000,120000,350000,34000,67000,78000,55000,66000,100000]
salary=0
tax=0
netsalary=0
totalsalary=0
totaltax=0
totalnetsalary=0
i=0
while i<len(sal):
    if sal[i]<50000:
        tax=sal[i]*3/100
    elif 50000<=sal[i]<100000:
        tax=sal[i]*5/100
    elif 100000<=sal[i]<30000:
        tax=sal[i]*8/100
    elif 300000<=sal[i]:
        tax=sal[i]*10/100
    netsalary=sal[i]-tax
    print(f"{months[i]},\t,  {sal[i]},\t,   {tax},\t,  {netsalary}")
    totalsalary+=sal[i]
    totaltax+=tax
    totalnetsalary+=netsalary
    i+=1
print("-----------------------------------------------")
print("totalsalary:",totalsalary,"totaltax:",totaltax,"totalnetsalary:",totalnetsalary)

        
