import random
def cifrado(mensaje_plano,ka,ene):
  
    mensaje_cifrado=mensaje_plano**ka%ene
    print("Mensaje cifrado",mensaje_cifrado)
    return(mensaje_cifrado)
    
def descifrado(mensaje_cifrado,jota,ene):
    mensaje_plano=round(mensaje_cifrado**jota%ene)
    print("Mensaje plano",mensaje_plano)
    return(mensaje_plano)
    
    
p=0
q=0

primos=[]
contador=0
j=1


lower = 100
upper = 500


    
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



n=p*q



F=(p-1)*(q-1)


eleccion_e=random.randint(0,len(primos))
while(primos[eleccion_e]>=F ):
    eleccion_e=random.randint(0,len(primos))
e=primos[eleccion_e]
e=3
d=1/(e%F)
mensaje_cifrado=cifrado(22,e,n)
descifrado(mensaje_cifrado,d,n)