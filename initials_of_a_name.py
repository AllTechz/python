raw_name = input("\nEnter Full Name : ") 
name = raw_name.strip()
bname  = name.split(' ')
lenofstr = len(bname)
fname = bname[0]
leofstrstr = str(lenofstr)
vlname = int(lenofstr) - 1
lname = bname[int(vlname)]
print("\nHi,"+bname[0])
print("\nHi,",end="")
for i in bname:
    if i == lname:
        break
    print(i[0].upper()+".",end="")
print(lname+"\n")

##This is the second method with more compact code
raw_name = input("\nEnter Full Name : ").strip().split(' ')
lname = raw_name[int(int(len(raw_name)) - 1)]
[print(i[0].upper()+".",end="") if i != lname else print(lname+"\n") for i in raw_name]
