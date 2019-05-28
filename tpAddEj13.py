#Ej 13
import random

MAX= 20
alumnos= [""]*MAX
notas= [0] * MAX

for i in range(0,MAX):
    alumnos[i] = "Alumno"+str(i)
    notas[i]= random.randint(1,10)

def Buscar(alumnos, notas, largo):
    nombre=input("Ingrese nombre: ")
    encontrado = False
    for i in range(0, largo):
        if alumnos[i] == nombre:
            encontrado= True
            print(alumnos[i], " : ", notas[i])
            modificar= input("Desea modificar nota? (s/n)")
            if modificar== "s":
                notas[i]= int(input("Ingrese nueva nota: "))

    if encontrado == False:
        print("no encontrado")

def Estadisticas(alumnos, notas, largo):
    promedioNotas=0
    promedioNotasMenor5=0
    posAlumnoMejorNota=0
    posAlumnoPeorNota=0

    sumaNotas=0
    sumaNotasMenor5= 0
    cantNotasMenor5= 0
    for i in range(0, largo):
        sumaNotas= sumaNotas + notas[i]
        if notas[i] < 5:
            sumaNotasMenor5= sumaNotasMenor5 + notas[i]
            cantNotasMenor5= cantNotasMenor5 + 1    
        if notas[i] > notas[posAlumnoMejorNota]:
            posAlumnoMejorNota= i
        if notas[i] < notas[posAlumnoPeorNota]:
            posAlumnoPeorNota= i
            
    promedioNotas= sumaNotas / largo
    promedioNotasMenor5= sumaNotasMenor5 / cantNotasMenor5 
    
    print("Prom. Notas: ", promedioNotas)
    print("Prom. Notas menores a 5: ", promedioNotasMenor5)
    print("Alumno mejor nota: ", alumnos[posAlumnoMejorNota])
    print("Nota mejor alumno: ", notas[posAlumnoMejorNota])
    print("Alumno peor nota: ", alumnos[posAlumnoPeorNota])
    print("Nota peor alumno: ", notas[posAlumnoPeorNota])

opc= 0
while opc!=3:
    opc= int(input("Ingrese 1-Buscar, 2-Estadisticas, 3-Salir"))
    if opc==1:
        Buscar(alumnos, notas, MAX)
    if opc==2:
        Estadisticas(alumnos, notas, MAX)


