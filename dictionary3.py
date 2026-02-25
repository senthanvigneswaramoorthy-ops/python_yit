d={"name":"Senthan","age":19,"gender":"Male"}
for key in d.keys():
    print(key,d[key])
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,value)
d1=d.copy()
d1["NIC"]=200625400988
print(d)
print(d1)