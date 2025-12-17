#abundant number#
n=int(input())
sum=1
for i in range(2,n):
    if n%i==0:
        sum+=i
if sum>n:
    print("yes")
else:
    print("no")