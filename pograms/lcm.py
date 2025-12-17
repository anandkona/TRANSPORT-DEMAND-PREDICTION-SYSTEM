#LCM#

'''def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
def lcm(a,b):
    a=(a*b)//gcd(a,b)
    return a
print(lcm(54,24))'''

def lcm(a,b):
    greater=1
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if(greater%a==0 and greater%b==0):
            c=greater
            break
        greater+=1
    return c
print(lcm(54,24))
