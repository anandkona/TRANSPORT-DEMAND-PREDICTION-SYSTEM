key="the lazy brown fox jump on the wall"
dict1={}
temp=97
for i in key:
    if i not in dict1 and i!=" ":
        dict1[i]=chr(temp)
        temp+=1
message=input()
ans=" "
for i  in message:
    if i ==" ":
        ans+=" "
    else:
        ans+=dict1[i]
print(ans)        
         