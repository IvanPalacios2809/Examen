class triangulo:
    lado1=0
    lado2=0
    lado3=0
    perimetro=0
    area=0
    s=0
mitriangulo=triangulo()
mitriangulo.lado1=float(input("dame el primer lado del triangulo"))
mitriangulo.lado2=float(input("dame el segundo lado del triangulo"))
mitriangulo.lado3=float(input("dame el tercer lado del triangulo"))
mitriangulo.s=(mitriangulo.lado1+mitriangulo.lado2+mitriangulo.lado3)/2
mitriangulo.area=mitriangulo.s*(mitriangulo.s-mitriangulo.lado1)*(mitriangulo.s-mitriangulo.lado2)*(mitriangulo.s-mitriangulo.lado3)