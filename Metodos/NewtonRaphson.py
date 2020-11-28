from sympy import * 
def f(evaluacion):
    x=evaluacion
    resultado=eval(funcion)
    return resultado
def df(evaluacion):
    x=Symbol('x')
    derivada=diff(funcion,x)
    x=evaluacion
    resultado=eval(str(derivada))
    return resultado
lst = [] 
  
# number of elemetns as input 

# iterating till the range 

funcion=input("Ingrese una funcion en terminos de x (nota: para potencias se utiliza **)")
x_i=float(input("Ingrese el valor de x_0"))
error=10
iteracion=0
while(error>=1e-10):
    x_imasuno=x_i-(f(x_i)/df(x_i))
    error=abs(x_i-x_imasuno)
    x_i=x_imasuno
    iteracion=iteracion+1
    file=open("newtonrapson.txt","a")
    file.write("\n Iteracion "+str(iteracion)+" Valor x: "+str(x_i)+" Error: "+str(error))
    file.close()
f=open("newtonrapson.txt","r")
print(f.read())    
f.close()