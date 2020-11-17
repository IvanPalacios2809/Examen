import numpy as np
import matplotlib.pyplot as plt
import math
x=[]
y=[]
x.append(0)
y.append(0)
pasos=int(input("Cuantos pasos dara tu borracho?"))
longitud=float(input("Que longitud tendran?"))
angulodelta=np.random.uniform(0,2*math.pi,pasos)
print("angulo  delta:",angulodelta)
for angulo in range(len(angulodelta)):
    x.append(longitud*math.cos(angulodelta[angulo]))
    y.append(longitud*math.sin(angulodelta[angulo]))    
print("x=",x)
print("y=",y)
rw=plt.plot(x,y,"ro-")


