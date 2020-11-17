nombre=input("Ingresa tu nombre")
apellido_paterno=input("Ingresa tu apellido paterno")
apellido_materno=input("Ingresa tu apellido materno")
dia=int(input("Ingresa el numero de tu dia de nacimiento"))
mes=int(input("Ingresa el numero de tu mes de nacimiento"))
ano=input("Ingresa el numero de tu año de nacimiento")
curp=apellido_paterno[0]
    
for letra in apellido_paterno:     
    if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" ):
        curp=curp+letra.upper()
        break
curp=curp+apellido_materno[0]+nombre[0]+ano[len(ano-2)]+ano[len(ano-1)]
if(mes<10):
    curp=curp+0+dia
else:
    curp=curp+dia
if(dia<10):
    curp=curp+0+dia
else:
    curp=curp+dia
