#Ej 12
import random

def menu():
    print("---------------------------------")
    print("Menu")
    print("1-Alta")
    print("2-Buscar")
    print("3-Modificar")
    print("4-Salir")
    opc= int(input("Ingrese opcion: "))
    return opc

def BuscarNombre(nombre, aBuscar, largo):
    for i in range(0, largo):
        if aBuscar == nombre[i]:
            return i 
    return -1

def Alta(nombre, cantidad, precio, largo):
    pos= BuscarNombre(nombre, "", largo)
    if pos == -1:
        print("No hay espacios vacios para agregar un producto")
    else:
        nombre[pos]= input("Ingrese el nombre: ")
        cantidad[pos]= int(input("Ingrese la cantidad: "))
        precio[pos]= float(input("Ingrese precio: "))

def Modificacion(nombre, cantidad,producto, largo):
    nombreABuscar= input("Ingrese nombre a buscar: ")
    
    pos= BuscarNombre(nombre, nombreABuscar, largo)
    if pos == -1:
        print("Nombre no encontrado")
    else:
        nombre[pos]= input("Ingrese el nombre: ")
        cantidad[pos]= int(input("Ingrese la cantidad: "))
        precio[pos]= float(input("Ingrese precio: "))
    
    
def Busqueda(nombre,cantidad,precio, largo):
    nombreABuscar= input("Ingrese nombre a buscar: ")
    
    pos= BuscarNombre(nombre, nombreABuscar, largo)
    if pos == -1:
        print("Nombre no encontrado")
    else:
        print("Producto: ", nombre[pos])
        print("Cantidad: ", cantidad[pos])
        print("Precio: ", precio[pos])

MAX= 10
nombre= [""]*MAX
cantidad= [0] * MAX
precio= [0] * MAX

for i in range(0,MAX - 3):
    nombre[i] = "Producto"+str(i)
    cantidad[i]= random.randint(1,100)
    precio[i]= random.random() * 100
    
opc= 0
while opc != 4:
    opc= menu()
    
    if opc == 1:
        Alta(nombre, cantidad, precio, MAX)
    if opc == 2:
        Busqueda(nombre,cantidad,precio, MAX)
    if opc == 3:
        Modificacion(nombre,cantidad,precio, MAX)
