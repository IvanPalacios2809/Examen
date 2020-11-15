class cuadrado:
    lado=0
    area=0
    perimetro=0
micuadrado=cuadrado()
micuadrado.lado=float(input("Dame la medida de los lados de tu cuadrado"))
micuadrado.area=micuadrado.lado*micuadrado.lado
micuadrado.perimetro=micuadrado.lado*4
print("Tu area es:",micuadrado.area,"Mientras que tu perimetro es:",micuadrado.perimetro)