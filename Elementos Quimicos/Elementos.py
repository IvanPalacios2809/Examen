# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 20:54:40 2020

@author: LAST_
"""
class Elemento:
    def __init__(self,ne,sim,na,ma,ra):
        self.Nombre_elemento=ne
        self.Simbolo=sim
        self.Numero_Atomico=na
        self.Masa_Atomica=ma
        self.Radio_atomico=ra
decision=1
while(decision<3):
    decision=int(input("Que desea? \n 1. Leer los datos almacenados \n 2. Almacenar datos \n 3.salir"))
    if(decision==1):
        f=open("elementos.txt")
        print(f.read())
    elif(decision==2):
        N_Elemento=input("Ingrese el nombre del elemento")
        Simbolo=input("Ingrese el simbolo del elemento")
        Numero=int(input("Ingrese el numero atomico del elemento"))
        Masa=float(input("Ingrese el masa del elemento"))
        Radio=float(input("Ingrese el radio atomico del elemento"))
        El1=Elemento(N_Elemento,Simbolo,Numero,Masa,Radio)
        f=open("elementos.txt","a")
        f.write("\n Nombre del elemento:"+El1.Nombre_elemento+"\t Simbolo: "+El1.Simbolo+"\t Numero Atomico "+str(El1.Numero_Atomico)+"\t Masa:"+str(El1.Masa_Atomica)+"\t Radio:"+str(El1.Radio_atomico))
        f.close()