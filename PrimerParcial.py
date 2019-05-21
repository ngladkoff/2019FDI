## 1er Parcial

#Tema 1
#Ej1

a= int(input("A: "))
b= int(input("B: "))
c= int(input("C: "))

if a<c and c<b:
    print("Correcto")
else:
    print("Incorrecto")
    
#Tema 2 ej 1
mes= int(input("mes: "))
anio= int(input("año: "))
if mes>=1 and mes<=12 and anio>=1900 and anio<=2100:
    print("Correcto")
else:
    print("Incorrecto")
    
#Tema 1 Ej 2
nro= 0
while nro<=0:
    nro= int(input("nro: "))
    if nro<=0:
        print("ingrese nro mayor a cero")

indice= 1
while indice <= nro:
    if indice % 2 == 0:
        print(indice)
    indice= indice + 1
    
#Tema 2 ej 2
nro= 0
while nro<=0:
    nro= int(input("nro: "))
    if nro<=0:
        print("ingrese nro mayor a cero")

indice= 1
while indice <= nro:
    if indice % 4 == 0:
        print(indice)
    indice= indice + 1
    
#Tema 1 ej 3
    
nro= 0
acumulado= 0
cant= 0
while nro != -1:
    nro= int(input("Nro:"))
    if nro != -1:
        acumulado= acumulado + nro
        cant= cant + 1

print("Promedio: ", acumulado / cant)

# Tema 2 ej 3
nro= 0
acumulado= 0
cant= 0
while nro != -1:
    nro= int(input("Nro:"))
    if nro != -1:
        acumulado= acumulado + nro
        cant= cant + 1

print("Acc: ", acumulado)
print("Cant: ", cant)

#Tema 1 Ej 4
def CalcularInflacion(importeActual, importeAnterior)
    return ((importeActual/importeAnterior) - 1) * 100

print("Inflacion: ", CalcularInflacion(120, 100))

#Tema 2 Ej 4
def Calcular(a, b, opc)
    if opc==1:
        return a * b
    if opc==2:
        return a / b
    print("Error")
    return -1

# Tema 1 ej 5
fc= int(input("Fc: "))
saldo= fc
while saldo>0:
    pago= int(input("pago: "))
    saldo= saldo - pago
    
# Tema 2 Ej 5
cant= int(input("Cant fc: "))
i= 0
fca= 0
fcb= 0
while i < cant:
    tipo= int(input("tipo: "))
    imp= int(input("imp: "))
    if tipo= 1:
        fca= fca+1
    else:
        fcb= fcb+1
print("fca: ", fca)
print("fcb: ", fcb)






