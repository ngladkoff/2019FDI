import random
MAX= 20
categorias= [0] * MAX
empleados= [""] * MAX
hijos = [0] * MAX
sueldos= [0] * MAX

for i in range(0,MAX):
    categorias[i]= random.randint(1,3)
    empleados[i]= "Empleado" + str(i+1)
    hijos[i]= random.randint(0,5)
    sueldos[i]= random.randint(10000, 50000)
    
def Menu():
    print("****MENU****")
    print("11- Tema 1 Ej 1")
    print("21- Tema 2 Ej 1")
    print("31- Tema 3 Ej 1")
    print("41- Tema 4 Ej 1")
    print("12- Tema 1 Ej 2")
    print("22- Tema 2 Ej 2")
    print("32- Tema 3 Ej 2")
    print("42- Tema 4 Ej 2")
    print("13- Tema 1 Ej 3")
    print("23- Tema 2 Ej 3")
    print("33- Tema 3 Ej 3")
    print("43- Tema 4 Ej 3")
    print("14- Tema 1 Ej 4")
    print("24- Tema 2 Ej 4")
    print("34- Tema 3 Ej 4")
    print("44- Tema 4 Ej 4")
    print("15- Tema 1 Ej 5")
    print("25- Tema 2 Ej 5")
    print("35- Tema 3 Ej 5")
    print("45- Tema 4 Ej 5")
    print("99- Salir")
    return int(input("Ingrese opcion: "))

def SueldoPorCategoria(categorias, sueldos, cat):
    acc= 0
    for i in range(0,20):
        if categorias[i] == cat:
            acc = acc + sueldos[i]
    return acc

def HijosPorCategoria(categorias, hijos, cat):
    acc= 0
    for i in range(0,20):
        if categorias[i] == cat:
            acc = acc + hijos[i]
    return acc

def SinHijosPorCategoria(categorias, hijos, cat):
    acc= 0
    for i in range(0,20):
        if categorias[i] == cat:
            if hijos[i] == 0:
                acc = acc +1
    return acc

def Buscar(nombre, empleados, MAX):
    for i in range(0,MAX):
        if empleados[i] == nombre:
            return i
    return -1

opc = 1
while opc != 99:
    opc= Menu()
    if opc == 11:
        cat= int(input("Ingrese categoria"))
        for i in range(0,MAX):
            if categorias[i] == cat:
                print(empleado[i])
    elif opc == 21:
        for i in range(0,MAX):
            if hijos[i] == 0:
                print(empleado[i])
    elif opc == 31:
        cat= int(input("Ingrese categoria"))
        for i in range(0,MAX):
            if categorias[i] == cat and hijos[i] == 0:
                print(empleado[i])
    elif opc == 41:
        for i in range(0,MAX):
            if categorias[i] == 1:
                print(empleado[i])
    elif opc == 12:
        acumulador = 0
        contador = 0
        for i in range(0,MAX):
            if categorias[i] == 2:
                acumulador = acumulador + sueldos[i]
                contador = contador + 1
        print("Promedio: ", acumulador/contador)
    elif opc == 22:
        cantEmpleados = 0
        cat= int(input("Ingrese categoria"))
        for i in range(0,MAX):
            if categorias[i] == cat:
                cantEmpleados = cantEmpleados + 1
        print("Cant. Empleados: ", cantEmpleados)
    elif opc == 32:
        acumulador = 0
        for i in range(0,MAX):
            if categorias[i] == 3:
                acumulador = acumulador + sueldos[i]
        print("Total Sueldos: ", acumulador)
    elif opc == 42:
        acumulador = 0
        contador = 0
        cat= int(input("Ingrese categoria"))
        for i in range(0,MAX):
            if categorias[i] == cat:
                acumulador = acumulador + sueldos[i]
                contador = contador + 1
        print("Promedio: ", acumulador/contador)
    elif opc == 13:
        posMayor = 0
        for i in range(0,MAX):
            if hijos[i] > hijos[posMayor]:
                posMayor= i
        print("Empleado con mayor cant. hijos: ", empleados[posMayor])
    elif opc == 23:
        posMenor = 0
        for i in range(0,MAX):
            if sueldos[i] < sueldos[posMenor]:
                posMenor= i
        print("Empleado con menor sueldo: ", empleados[posMenor])
    elif opc == 33:
        posMayor = 0
        for i in range(0,MAX):
            if sueldos[i] > sueldos[posMayor]:
                posMayor= i
        print("Empleado con mayor sueldo: ", empleados[posMayor])
    elif opc == 43:
        pos = 0
        for i in range(0,MAX):
            if hijos[i] < hijos[pos]:
                pos= i
        print("Empleado con menor cant. hijos: ", empleados[pos])
    elif opc == 14:
        cant1=0
        cant2=0
        cant3=0
        for i in range(0,MAX):
            if categorias[i] == 1:
                cant1 = cant1 + 1
            if categorias[i] == 2:
                cant2 = cant2 + 1
            if categorias[i] == 3:
                cant3 = cant3 + 1
        print("Cant cat 1: ", cant1)
        print("Cant cat 2: ", cant2)
        print("Cant cat 3: ", cant3)
    elif opc == 24:
        print("Sdos Cat 1: ", SueldoPorCategoria(categorias, sueldos, 1))
        print("Sdos Cat 2: ", SueldoPorCategoria(categorias, sueldos, 2))
        print("Sdos Cat 3: ", SueldoPorCategoria(categorias, sueldos, 3))
    elif opc == 34:
        print("Hijos Cat 1: ", HijosPorCategoria(categorias, hijos, 1))
        print("Hijos Cat 2: ", HijosPorCategoria(categorias, hijos, 2))
        print("Hijos Cat 3: ", HijosPorCategoria(categorias, hijos, 3))
    elif opc == 44:
        print("Sin Hijos Cat 1: ", SinHijosPorCategoria(categorias, hijos, 1))
        print("Sin Hijos Cat 2: ", SinHijosPorCategoria(categorias, hijos, 2))
        print("Sin Hijos Cat 3: ", SinHijosPorCategoria(categorias, hijos, 3))
    elif opc == 15:
        nombre = input("Nombre: ")
        pos = Buscar(nombre, empleados, MAX)
        if pos == -1:
            print("No encontrado")
        else:
            sueldos[pos]= int(input("Ingrese el nuevo sueldo: "))
    elif opc == 25:
        nombre = input("Nombre: ")
        pos = Buscar(nombre, empleados, MAX)
        if pos == -1:
            print("No encontrado")
        else:
            hijos[pos]= int(input("Ingrese cant hijos: "))
    elif opc == 35:
        nombre = input("Nombre: ")
        pos = Buscar(nombre, empleados, MAX)
        if pos == -1:
            print("No encontrado")
        else:
            categorias[pos]= int(input("Ingrese la nueva categoria: "))
    elif opc == 45:
        nombre = input("Nombre: ")
        pos = Buscar(nombre, empleados, MAX)
        if pos == -1:
            print("No encontrado")
        else:
            sueldos[pos]= sueldos[pos] * 1.10
            
        