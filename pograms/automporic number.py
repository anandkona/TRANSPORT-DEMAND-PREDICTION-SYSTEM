 #automorpic number#
'''import math
number=int(input())
square=pow(number,2)
mod=pow(10,len(str(number)))
if square%mod==number:
    print("yes")
else:
    print("no")'''
    
    
number=int(input())
a=str(number)
b=number**2
c=str(b)
if c.endswith(a):
    print("yes")
                                        