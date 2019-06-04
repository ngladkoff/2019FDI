#Ej 15

ventasSucursales= [0] * 10

## Ingreso de datos
## Se asume que el usuario va a cargar todas las sucursales, en cualquier orden
## pero todas van a tener la cantidad de ventas, recién ahi sale.
suc = 1
while suc > 0:
    suc = int(input("Ingrese nro de Sucursal: (0 para salir)"))
    
    if suc > 0:
        cant= int(input("Ingrese cantidad sucursal " + str(suc) + ": "))
        ventasSucursales[suc - 1]= cant

## Calculo Promedio
suma=0
cont= 0
for i in range(0,10):
    suma= suma + ventasSucursales[i]
    cont= cont + 1

prom= suma/cont

## Sucursales con ventas por arriba del promedio
for i in range(0, 10):
    if ventasSucursales[i] > prom:
        print("Sucursal ", i+1)


