class rombo:
    Diametro=0
    diametro=0
    area=0
    perimetro=0
mirombo=rombo()
mirombo.Diametro=(float(input("Dame tu diametro mayor")))
mirombo.diametro=(float(input("Dame tu diametro menor")))
mirombo.lado1=(float(input("Dame tu primer lado")))
mirombo.lado2=(float(input("Dame tu segundo lado")))
mirombo.lado3=(float(input("Dame tu tercer lado")))
mirombo.lado4=(float(input("Dame tu cuarto lado")))
mirombo.area=mirombo.Diametro*mirombo.diametro/2
mirombo.perimetro=mirombo.lado1+mirombo.lado2+mirombo.lado3+mirombo.lado4
print("el perimetro del trapecio es",mirombo.perimetro,"y el area es:",mirombo.area)