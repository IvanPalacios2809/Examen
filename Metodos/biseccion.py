def f(evaluacion):
    x=evaluacion
    resultado=eval(funcion)
    return resultado
funcion=input("Ingrese una funcion en terminos de x (nota: para potencias se utiliza **)")
a=float(input("Ingrese el valor del limite inferior (a)"))
b=float(input("Ingrese el valor del limite superior(b)"))
guardado=a
mitad=b
error=0.1
iteracion=0
if(f(a)*f(b)>0):
    print("la funcion requiere que cambie de signo")
while(abs(guardado-mitad)>=error):    
    guardado=mitad        
    mitad=(a+b)/2    
    if(f(a)*f(mitad)<0):
        b=mitad
    if(f(b)*f(mitad)<0):
        a=mitad
    iteracion=iteracion+1
    error_relativo=(mitad-guardado/mitad)
    file=open("iteraciones","a")
    print("iteracion:",iteracion,"a:",a,"b:",b,"x",iteracion,"",mitad,"error relativo:",error_relativo,"%") 
    file.write("\n iteracion: "+str(iteracion)+" a:"+str(a)+" b:"+str(b)+" x_"+str(iteracion)+": "+str(mitad)+"error relativo:"+str(error_relativo)+"%")
    file.close()
    
print("La raiz es",mitad)