'''prime num

n=int(input())
def prime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
a=prime(n)
print(a)'''


num = 15
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")
  
  
  
  num = 15
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,num):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")
  
  
  num = 15
flag = 0
if num<2:
  flag = 1
else:
  for i in range(2,int((num/2)+1)):
    if num%i==0:
      flag = 1
      break

if flag == 1:
  print('Not Prime')
else:
  print("Prime")
  
  
  
  
  
  
  
  
  low, high = 2, 10
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)



low, high = 2, 10
primes = [2, 3]

for num in range(low, high + 1):
    flag = 0
    
    if num < 2:
        flag = 1
        
    if num % 2 == 0:
        continue
        
    if num % 3 == 0:
        continue
        
    iter = 2
    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
        iter += 1
        
    if flag == 0:
        primes.append(num)

print(primes)




low, high = 2, 10
primes = [2, 3]

for num in range(low, high + 1):
    flag = 0
    if num < 2:
        flag = 1

    if num % 2 == 0:
        continue
        
    if num % 3 == 0:
        continue

    iter = 3

    while iter < int(pow(num, 0.5)):
        if num % iter == 0:
            flag = 1
            break
         iter += 2

    if flag == 0:
        primes.append(num)

print(primes)