Nombre=input("Ingresa tu nombre")
Primer_Apellido=input("Ingresa tu primer apellido")
Segundo_Apellido=input("Ingresa tu segundo apellido")
Ano=(input("Ingresa el numero del año de tu nacimiento"))
Mes=(input("Ingresa el numero de tu mes de tu nacimiento"))
dia=(input("Ingresa el numero del dia de tu nacimiento"))
#primera regla
rfc=""+Primer_Apellido[0]
letra=1

for letra in Primer_Apellido:
    if(len(Primer_Apellido<=2)):
        rfc=Primer_Apellido[0]+Segundo_Apellido[0]+Nombre[0]+Nombre[1]
        break
    elif(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" ):
        rfc=rfc+letra.upper()
        break
    else:
        continue
rfc=rfc+Segundo_Apellido[0].upper()+Nombre[0].upper()+Ano[len(Ano-2)]+Ano[len(Ano-3)]




print(rfc)
