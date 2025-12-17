def ap(a,d,n):
    sum=0
    i=0
    while i<n:
        sum+=a
        i+=1
        a=a+d
    return sum
print(ap(5,6,2))