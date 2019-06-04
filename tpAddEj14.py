#Ej14

ventasSucursales= [0] * 10

for i in range(0,10):
    cant= int(input("Ingrese cantidad sucursal " + str(i+1) + ": "))
    ventasSucursales[i]= cant
    
suma=0
cont= 0
for i in range(0,10):
    suma= suma + ventasSucursales[i]
    cont= cont + 1

prom= suma/cont

for i in range(0, 10):
    if ventasSucursales[i] > prom:
        print("Sucursal ", i+1)

