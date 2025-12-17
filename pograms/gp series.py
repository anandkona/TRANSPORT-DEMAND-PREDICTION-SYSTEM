'''def ap(a,d,n):
    return ((n // 2) * (2 * a + (n - 1) * d))
print(ap(5,6,2)) #n/2[2a+(n-1)d]#'''


def gp (a,r,n):
    return (a * (1 - pow(r, n))) / (1 - r)   print(a * (1 - r ** n) / (1 - r))
print(gp(1,0.5,3))

def sumOfGP(a, r, n) :
    
    sum = 0
    i = 0
    while i < n :
        sum = sum + a
        a = a * r
        i = i + 1
    
    return sum
