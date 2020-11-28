# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:02:29 2020

@author: LAST_
"""
import matplotlib.pyplot as plt
import urllib.request
datos = urllib.request.urlopen('https://automatetheboringstuff.com/files/rj.txt').read().decode()
contador_a=0
contador_b=0
contador_c=0
contador_d=0
contador_e=0
contador_f=0
contador_g=0
contador_h=0
contador_i=0
contador_j=0
contador_k=0
contador_l=0
contador_m=0
contador_n=0
contador_o=0
contador_p=0
contador_q=0
contador_r=0
contador_s=0
contador_t=0
contador_u=0
contador_v=0
contador_w=0
contador_x=0
contador_y=0
contador_z=0
letras=[]
for letra in range (len(datos)):
    
    if datos[letra]=='a':
        contador_a=contador_a+1
    elif datos[letra]=='b':
        contador_b=contador_b+1
    elif datos[letra]=='c':
        contador_c=contador_c+1
    elif datos[letra]=='d':
        contador_d=contador_d+1
    elif datos[letra]=='e':
        contador_e=contador_e+1
    elif datos[letra]=='f':
        contador_f=contador_f+1
    elif datos[letra]=='g':
        contador_g=contador_g+1
    elif datos[letra]=='h':
        contador_h=contador_h+1
    elif datos[letra]=='i':
        contador_i=contador_i+1
    elif datos[letra]=='j':
        contador_j=contador_j+1
    elif datos[letra]=='k':
        contador_k=contador_k+1
    elif datos[letra]=='l':
        contador_l=contador_l+1
    elif datos[letra]=='m':
        contador_m=contador_m+1
    elif datos[letra]=='n':
        contador_n=contador_n+1
    elif datos[letra]=='o':
        contador_o=contador_o+1
    elif datos[letra]=='p':
        contador_p=contador_p+1
    elif datos[letra]=='q':
        contador_q=contador_q+1
    elif datos[letra]=='r':
        contador_r=contador_r+1
    elif datos[letra]=='s':
        contador_s=contador_s+1
    elif datos[letra]=='t':
        contador_t=contador_t+1
    elif datos[letra]=='u':
        contador_u=contador_u+1
    elif datos[letra]=='v':
        contador_v=contador_v+1
    elif datos[letra]=='w':
        contador_w=contador_w+1
    elif datos[letra]=='x':
        contador_x=contador_x+1
    elif datos[letra]=='y':
        contador_y=contador_y+1
    elif datos[letra]=='z':
        contador_z=contador_z+1
        
print("Cantidad de letras a:",contador_a)
print("Cantidad de letras b:",contador_b)
print("Cantidad de letras c:",contador_c)
print("Cantidad de letras d:",contador_d)
print("Cantidad de letras e:",contador_e)
print("Cantidad de letras f:",contador_f)
print("Cantidad de letras g:",contador_g)
print("Cantidad de letras h:",contador_h)
print("Cantidad de letras i:",contador_i)
print("Cantidad de letras j:",contador_j)
print("Cantidad de letras k:",contador_k)
print("Cantidad de letras l:",contador_l)
print("Cantidad de letras m:",contador_m)
print("Cantidad de letras n:",contador_n)
print("Cantidad de letras o:",contador_o)
print("Cantidad de letras p:",contador_p)
print("Cantidad de letras q:",contador_q)
print("Cantidad de letras r:",contador_r)
print("Cantidad de letras s:",contador_s)
print("Cantidad de letras t:",contador_t)
print("Cantidad de letras u:",contador_u)
print("Cantidad de letras v:",contador_v)
print("Cantidad de letras w:",contador_w)
print("Cantidad de letras x:",contador_x)
print("Cantidad de letras y:",contador_y)
print("Cantidad de letras z:",contador_z)
letras.append(contador_a)
letras.append(contador_b)
letras.append(contador_c)
letras.append(contador_d)
letras.append(contador_e)
letras.append(contador_f)
letras.append(contador_g)
letras.append(contador_h)
letras.append(contador_i)
letras.append(contador_j)
letras.append(contador_k)
letras.append(contador_l)
letras.append(contador_m)
letras.append(contador_n)
letras.append(contador_o)
letras.append(contador_p)
letras.append(contador_q)
letras.append(contador_r)
letras.append(contador_s)
letras.append(contador_t)
letras.append(contador_u)
letras.append(contador_v)
letras.append(contador_w)
letras.append(contador_x)
letras.append(contador_y)
letras.append(contador_z)
print(letras)
valor_letras=[]
valor_letras.append("a")
valor_letras.append("b")
valor_letras.append("c")
valor_letras.append("d")
valor_letras.append("e")
valor_letras.append("f")
valor_letras.append("g")
valor_letras.append("h")
valor_letras.append("i")
valor_letras.append("j")
valor_letras.append("k")
valor_letras.append("l")
valor_letras.append("m")
valor_letras.append("n")
valor_letras.append("o")
valor_letras.append("p")
valor_letras.append("q")
valor_letras.append("r")
valor_letras.append("s")
valor_letras.append("t")
valor_letras.append("u")
valor_letras.append("v")
valor_letras.append("w")
valor_letras.append("x")
valor_letras.append("y")
valor_letras.append("z")
plt.title('MOS')
plt.plot(valor_letras,letras)
plt.grid(True)
plt.show()
plt.clf()
