class rectangulo:
    base=0;
    altura=0;
    area=0;
    perimetro=0;

mirectangulo=rectangulo()
mirectangulo.base=float(input("Dame tu base"))
mirectangulo.altura=float(input("Dame tu altura"))
mirectangulo.area=mirectangulo.base*mirectangulo.altura/2
mirectangulo.perimetro=mirectangulo.base*2+mirectangulo.altura*2
print("Tu area es:",mirectangulo.area,"Mientras que tu perimetro es:",mirectangulo.perimetro)