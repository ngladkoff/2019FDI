#Ej 19
import random
MAX = 100
apellidos= [""] * MAX
nombres= [""] * MAX
edades= [0] * MAX
sexos= [0] * MAX
categorias= [0] * MAX
alturas= [0.0] * MAX
pesos= [0.0] * MAX

## Carga inicial de datos random
for i in range(0,MAX):
    apellidos[i]= "Apellido"+str(i+1)
    nombres[i]= "Nombre"+str(i+1)
    edades[i]= random.randint(1,99)
    sexos[i]= random.randint(1,2)
    categorias[i]= random.randint(1,3)
    alturas[i]= random.randint(100, 200) / 100
    pesos[i]= random.randint(100, 1500) / 10
    
# punto 2
cantHombres=0
cantMujeres=0
sumaHombres= 0
sumaMujeres= 0
for i in range(0,MAX):
    if sexos[i] == 1:
        cantHombres = cantHombres + 1
        sumaHombres = sumaHombres + edades[i]
    else:
        cantMujeres = cantMujeres + 1
        sumaMujeres = sumaMujeres + edades[i]

print("Promedio Edad Hombres: ", sumaHombres/cantHombres)
print("Promedio Edad Mujeres: ", sumaMujeres/cantMujeres)
print("Promedio Edad General: ", (sumaHombres + sumaMujeres)/(cantHombres + cantMujeres))

# punto 3
posMenor= 0
for i in range(0,MAX):
    if edades[i] < edades[posMenor]:
        posMenor= i
print("El apellido del socio de menor edad es: ", apellidos[posMenor])

# punto 4
posMayor= 0
for i in range(0,MAX):
    if edades[i] > edades[posMayor]:
        posMayor= i
print("El apellido del socio de mayor edad es: ", apellidos[posMayor])

# punto 5
cantHombres=0
cantMujeres=0
sumaHombres= 0
sumaMujeres= 0
for i in range(0,MAX):
    if sexos[i] == 1:
        cantHombres = cantHombres + 1
        sumaHombres = sumaHombres + alturas[i]
    else:
        cantMujeres = cantMujeres + 1
        sumaMujeres = sumaMujeres + alturas[i]

print("Promedio Altura Hombres: ", sumaHombres/cantHombres)
print("Promedio Altura Mujeres: ", sumaMujeres/cantMujeres)
print("Promedio Altura General: ", (sumaHombres + sumaMujeres)/(cantHombres + cantMujeres))

# punto 6
cantHombres=0
cantMujeres=0
sumaHombres= 0
sumaMujeres= 0
for i in range(0,MAX):
    if sexos[i] == 1:
        cantHombres = cantHombres + 1
        sumaHombres = sumaHombres + pesos[i]
    else:
        cantMujeres = cantMujeres + 1
        sumaMujeres = sumaMujeres + pesos[i]

print("Promedio Pesos Hombres: ", sumaHombres/cantHombres)
print("Promedio Pesos Mujeres: ", sumaMujeres/cantMujeres)
print("Promedio Pesos General: ", (sumaHombres + sumaMujeres)/(cantHombres + cantMujeres))

#punto 7 - apellido socios con IMC > 25
for i in range(0,MAX):
    if (pesos[i]/(alturas[i] * alturas[i])) > 25:
        print(apellidos[i])
    
