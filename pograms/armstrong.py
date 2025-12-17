'armstrong'
def arm(n):
    l=list(map(int,str(n)))
    s=0
    for i in l:
        s+=i**3
    if n==s:
        return True
    else:
        return False
n=int(input())
b=arm(n)
print(b)
