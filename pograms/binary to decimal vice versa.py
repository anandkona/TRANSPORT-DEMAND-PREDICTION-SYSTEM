'''def binary_decimal(n):
    decimal=0
    power=1
    while n>0:
        rem=n%10
        n//=10
        decimal+=rem*power
        power*=2
    return decimal
n=int(input())
a=binary_decimal(n)
print(a)'''


#decimal to binary#

n=int(input())
res=''
while n>0:
    res+=str(n&1)
    n>>=1
print(res)

 s=''
        while n>0:
            if n&1==1:
                s+="1"
            else:
                s+="0"
            n=n>>1
            
        return s[::-1]

        