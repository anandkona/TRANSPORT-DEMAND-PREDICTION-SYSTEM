#perfect number#
'''n=int(input())
sum1=0
for i in range(1,n):
    if n%i==0:
        sum1+=i
if sum1==n:
    print("perfect")
else:
    print("no")'''
n=int(input())
sum=0
i=1
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("yes")
