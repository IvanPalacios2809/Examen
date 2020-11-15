import math

class Circulo():
    radio=0;
    perimetro=0.0;
    area=0.0;


micirculo=Circulo()
micirculo.radio=float(input("Dame tu radio"))
micirculo.perimetro=2*math.pi*micirculo.radio
micirculo.area=math.pi*micirculo.radio*micirculo.radio
print("Tu area es:",micirculo.area,"Mientras que tu perimetro es:",micirculo.perimetro)


