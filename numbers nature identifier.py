user = int(input("enter your desired number: "))
no=[ ]
no.append(user)
choose_user = input("enter \"y\" to continue or \"any key\" to stop")
while choose_user == "y":
    user = int(input("enter your desired number: "))
    no.append(user)
    choose_user = input("enter \"y\" to continue or \"n\" to stop")
dic={"positive":0,"negative":0,"zero":0}
for g in no:
    f=2**g
    if f<1 or g==-1:
        dic["negative"]+=1
    if f>1 or g==1:
        dic["positive"]=dic["positive"]+1
    elif f==1:
        dic["zero"]+=1
print(dic)