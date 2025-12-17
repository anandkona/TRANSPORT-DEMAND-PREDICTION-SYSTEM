palindrome number

'''n=int(input())
rev=0
temp=n
while temp!=0:
    orde=temp%10
    rev=rev*10+orde
    temp=temp//10
if n==rev:
    print("yes")
else:
    print("no")'''


'''n=int(input())
rev=int(str(n)[::-1])
if n==rev:
    print("yes")'''
    