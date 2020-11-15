class trapecio:
    base_menor=0
    base_mayor=0
    lado_izquierdo=0
    lado_derecho=0
    altura=0
    area=0
    perimetro=0
mitrapecio=trapecio()
mitrapecio.altura=float(input("ingrese la altura del trapecio"))
mitrapecio.base_menor=float(input("ingrese la base menor del trapecio"))
mitrapecio.base_mayor=float(input("ingrese la base mayor del trapecio"))
mitrapecio.lado_izquierdo=float(input("ingrese el lado izquierdo"))
mitrapecio.lado_derecho=float(input("Ingrese el lado derecho"))
if(mitrapecio.base_menor<mitrapecio.base_mayor):
    print("Base menor y mayor invalidas")
else:
    mitrapecio.area=mitrapecio.altura*(mitrapecio.base_menor+mitrapecio.base_mayor/2)
    mitrapecio.perimetro=mitrapecio.base_menor+mitrapecio.base_mayor+mitrapecio.lado_izquierdo+mitrapecio.lado_derecho
    print("El area es:",mitrapecio.area,"El perimetro",mitrapecio.perimetro)