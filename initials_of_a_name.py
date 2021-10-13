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
