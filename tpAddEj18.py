#Ej 18
import random

def fechaMayor(anio1, mes1, dia1, anio2, mes2, dia2):
    if (anio1 > anio2):
        return 1
    elif (anio2 > anio1):
        return -1
    
    if (mes1 > mes2):
        return 1
    elif(mes2 > mes1):
        return -1
    
    if dia1 > dia2:
        return 1
    elif dia2 > dia1:
        return -1
    return 0

MAX= 20
volcanes= [""] * MAX
magnitudes= [0]* MAX
anios= [0]* MAX
mes= [0]* MAX
dia= [0]* MAX

for i in range(0, MAX):
    volcanes[i]= "Volcan" + str(i+1)
    magnitudes[i]= random.randint(0,10)
    anios[i]= random.randint(2009, 2018)
    mes[i]= random.randint(1,12)
    dia[i]= random.randint(1,28)
    
posMayor= 0
for i in range(0,MAX):
    if magnitudes[i] > magnitudes[posMayor]:
        posMayor= i
    elif magnitudes[i] == magnitudes[posMayor]:
        if fechaMayor(anios[i], mes[i], dia[i], anios[posMayor], mes[posMayor], dia[posMayor]) > 0:
            posMayor= i
print ("El volcan de mayor magnitud es: " + volcanes[posMayor])

suma= 0
for i in range(0, MAX):
    suma= suma + magnitudes[i]

print("Promedio de magnitudes: ", suma/MAX)

r1= 0
r2= 0
r3= 0
for i in range(0,MAX):
    if (magnitudes[i] <= 5):
        r1= r1 + 1
    elif (magnitudes[i] >= 8):
        r3= r3 + 1
    else:
        r2 = r2 + 1
        
print("Cantidad Rango 1 a 5: ", r1)
print("Cantidad Rango 6 y 7: ", r2)
print("Cantidad Rango 8 o más: ", r3)

cantEventos= [0] * 10
for i in range(0, MAX):
   pos= 2018 - anios[i]
   cantEventos[pos] = cantEventos[pos] + 1
   
posM= 0
for i in range(0,10):
    if cantEventos[i] > cantEventos[posM]:
        posM = i

print ("El anio con mayor cantidad de erupciones es: ", 2018-posM)
