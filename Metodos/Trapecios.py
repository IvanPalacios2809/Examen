# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:36:36 2020

@author: LAST_
"""
from sympy import integrate, init_printing
from sympy.abc import x

funcion=input("Dame tu funcion")
n=int(input("Dame los cuantos trapecios necesitas"))
a=float(input("Dame el valor de a"))
b=float(input("Dame el valor de b"))
resultado_real=integrate(funcion, (x,a,b))
h=(b-a)/n
resultado=(h/2)*a





file=open("Integral.txt","a")
error=resultado-resultado_real
file.write("\niteracion: 0 h: "+str(h)+" Valor integral: "+str(resultado)+" error "+str(error))
file.close()
    
    

x=a+h
iteracion=1
while(x<=b-h):
    resultadofuncion=2*eval(funcion)
    resultado=resultado+(h/2)*(resultadofuncion)
    x=x+h
    file=open("Integral.txt","a")
    error=resultado-resultado_real
    file.write("\niteracion: "+str(iteracion)+" h: "+str(h)+" Valor integral: "+str(resultado)+" error "+str(error))
    file.close()
    iteracion=iteracion+1
file=open("Integral.txt","a")
resultado=resultado + (h/2)*b
error=resultado-resultado_real

file.write("\niteracion: "+str(iteracion)+" h: "+str(h)+" Valor integral: "+str(resultado)+" error "+str(error))
file.close()
f=open("Integral.txt","r")
print(f.read())    
f.close()