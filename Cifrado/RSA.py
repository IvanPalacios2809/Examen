import random
def cifrado(mensaje_plano,ka,ene):
    mensaje_cifrado=[]
    mensaje_numero=[]
    
    letra=0
    for letra in range(len(mensaje_plano)):
        if(mensaje_plano[letra]=='A'):
            mensaje_numero.append(10)
        elif(mensaje_plano[letra]=='B'):
            mensaje_numero.append(11)  
        elif(mensaje_plano[letra]=='C'):
            mensaje_numero.append(12)  
        elif(mensaje_plano[letra]=='D'):
            mensaje_numero.append(13)  
        elif(mensaje_plano[letra]=='E'):
            mensaje_numero.append(14)  
        elif(mensaje_plano[letra]=='F'):
            mensaje_numero.append(15)  
        elif(mensaje_plano[letra]=='G'):
            mensaje_numero.append(16)  
        elif(mensaje_plano[letra]=='H'):
            mensaje_numero.append(17)  
        elif(mensaje_plano[letra]=='I'):
            mensaje_numero.append(18)  
        elif(mensaje_plano[letra]=='J'):
            mensaje_numero.append(19)  
        elif(mensaje_plano[letra]=='K'):
            mensaje_numero.append(20)  
        elif(mensaje_plano[letra]=='L'):
            mensaje_numero.append(21)  
        elif(mensaje_plano[letra]=='M'):
            mensaje_numero.append(22)  
        elif(mensaje_plano[letra]=='N'):
            mensaje_numero.append(23)  
        elif(mensaje_plano[letra]=='O'):
            mensaje_numero.append(24)  
        elif(mensaje_plano[letra]=='P'):
            mensaje_numero.append(25)  
        elif(mensaje_plano[letra]=='Q'):
            mensaje_numero.append(26)  
        elif(mensaje_plano[letra]=='R'):
            mensaje_numero.append(27)  
        elif(mensaje_plano[letra]=='S'):
            mensaje_numero.append(28)  
        elif(mensaje_plano[letra]=='T'):
            mensaje_numero.append(29)  
        elif(mensaje_plano[letra]=='U'):
            mensaje_numero.append(30)  
        elif(mensaje_plano[letra]=='V'):
            mensaje_numero.append(31)  
        elif(mensaje_plano[letra]=='W'):
            mensaje_numero.append(32)  
        elif(mensaje_plano[letra]=='X'):
            mensaje_numero.append(33)  
        elif(mensaje_plano[letra]=='Y'):
            mensaje_numero.append(34)  
        elif(mensaje_plano[letra]=='Z'):
            mensaje_numero.append(35)#TERMINA ASIGNACION DE LETRAS  
    for  numero in mensaje_numero:    
        mensaje_cifrado.append(numero**ka%ene)
    print(mensaje_cifrado)
    
    return(mensaje_cifrado)
    
def descifrado(mensaje_cifrado,jota,ene):
    mensaje_plano=[]
    mensaje_real=[]
    for pos_cripto in range(len(mensaje_cifrado)):
        mensaje_plano.append(round(mensaje_cifrado[pos_cripto]**jota%ene))
    for letras_reales in mensaje_plano:
        if(letras_reales==10):
            mensaje_real.append('A')
        elif(letras_reales==11):
            mensaje_real.append('B')
        elif(letras_reales==12):
            mensaje_real.append('C')
        elif(letras_reales==13):
            mensaje_real.append('D')
        elif(letras_reales==14):
            mensaje_real.append('E')
        elif(letras_reales==15):
            mensaje_real.append('F')
        elif(letras_reales==16):
            mensaje_real.append('G')
        elif(letras_reales==17):
            mensaje_real.append('H')
        elif(letras_reales==18):
            mensaje_real.append('I')
        elif(letras_reales==19):
            mensaje_real.append('J')
        elif(letras_reales==20):
            mensaje_real.append('K')
        elif(letras_reales==21):
            mensaje_real.append('L')
        elif(letras_reales==22):
            mensaje_real.append('M')
        elif(letras_reales==23):
            mensaje_real.append('N')
        elif(letras_reales==24):
            mensaje_real.append('O')
        elif(letras_reales==25):
            mensaje_real.append('P')
        elif(letras_reales==26):
            mensaje_real.append('Q')
        elif(letras_reales==27):
            mensaje_real.append('R')
        elif(letras_reales==28):
            mensaje_real.append('S')
        elif(letras_reales==29):
            mensaje_real.append('T')
        elif(letras_reales==30):
            mensaje_real.append('U')
        elif(letras_reales==31):
            mensaje_real.append('V')
        elif(letras_reales==32):
            mensaje_real.append('W')
        elif(letras_reales==33):
            mensaje_real.append('X')
        elif(letras_reales==34):
            mensaje_real.append('Y')
        elif(letras_reales==35):
            mensaje_real.append('Z')
    print(mensaje_real)
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
mensaje=input("Dame tu mensaje a encriptar (En mayusculas.)")
e=3
d=1/(e%F)
mensaje_cifrado=cifrado(mensaje,e,n)
descifrado(mensaje_cifrado,d,n)