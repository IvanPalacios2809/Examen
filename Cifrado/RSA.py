import random

p=0
q=0

primos=[]
contador=0
j=1
# Python program to display all the prime numbers within an interval

lower = 100000
upper = 500000



for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primos.append(num)

eleccion_p=random.randint(0,len(primos))
eleccion_q=random.randint(0,len(primos))
p=primos[eleccion_p]
q=primos[eleccion_q]
z=(p-1)*(q-1)
eleccion_k=random.randint(0,len(primos))
k=primos[eleccion_k]
