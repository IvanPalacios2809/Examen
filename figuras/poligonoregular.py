import math 

class poligonoregular:
    numero_lados=0
    longitud_lado=0
    area=0
    perimetro=0
    apotema=0
    an_triangulo=0
poligono=poligonoregular()
poligono.numero_lados=int(input("dame el numero de los lados de tu poligono"))
poligono.longitud_lado=float(input("dame la longitud de los lados de tu poligono"))
poligono.an_triangulo=float(input("dame el angulo de un triangulo interior de uno de los lados de tu poligono"))
poligono.apotema=(poligono.longitud_lado/2)/math.tan(poligono.an_triangulo/2)
poligono.area=(poligono.numero_lados*poligono.longitud_lado*poligono.apotema)/2
poligono.perimetro=poligono.numero_lados*poligono.longitud_lado
print("El area de tu poligono es:",poligono.area,"Mientras que el perimetro de tu poligono es:",poligono.perimetro)