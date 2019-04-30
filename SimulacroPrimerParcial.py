## ALUMNO: ...........
## LU: ...........

print("##############################")
print("#                            #")
print("#  SIMULACRO PRIMER PARCIAL  #")
print("#                            #")
print("##############################")
print("")
print("")

print("#################")
print("#  EJERCICIO 1  #")
print("#################")
print("")
print("")

mayor = 0

vuelta= 11
while vuelta < 10:
    
    numero = int(input("Ingrese un numero: "))
    
    if numero > mayor:
        mayor = numero
    
    vuelta = vuelta + 1


print("El numero mayor es: ", mayor)

input()
print("")
print("")
print("#################")
print("#  EJERCICIO 2  #")
print("#################")
print("")
print("")

def CalcularTiempo(e,c):
    if c==1:
        return 15
    
    if c==2:
        return 30
    
    if e >= 60:
        return 120
    
    return 240

cantPacientes =0
edad = 0
while edad >=0:
    edad = int(input("Edad: "))
    if edad >= 0:
        codigo= int(input("Codigo: "))
        tiempo = CalcularTiempo(edad, codigo)
        print("Tiempo maximo: ", tiempo)
        cantPacientes = cantPacientes + 1

print("Pacientes atendidos: ", cantPacientes)
input()
print("")
print("")
print("#################")
print("#  EJERCICIO 3  #")
print("#################")
print("")
print("")

ventasChicas = 0
ventasMedianas = 0
ventasGrandes = 0

vueltas =0
while vueltas < 10:
    nro= int(input("Ingrese importe venta: "))    

    if nro < 1000:
        ventasChicas = ventasChicas + 1
    elif nro >= 1000 and nro < 5000:
        ventasMedianas = ventasMedianas + 1
    else:
        ventasGrandes = ventasGrandes + 1

    vueltas = vueltas + 1


print("Ventas Grandes: ", ventasGrandes)
print("Ventas Medianas: ", ventasMedianas)
print("Ventas Chicas: ", ventasChicas)



