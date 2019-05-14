# TP6 Ej 1 - listas

def esCapicua(lista, tamanio):
    
    
    return True

def ingresarNro(min, max):
    nro = 0
    while (nro < min or nro > max) and nro != -1:
        nro=int(input("Ingrese numero: "))
        if (nro < min or nro >max) and nro != -1:
            print("Ingrese un número entre ", min, " y ", max)
    return nro    

def cargarLista():
    lst= [0] * 50

    nro = 0
    i = 0
    while nro != -1 and i < 50: 
        nro = ingresarNro(1,20)
        if nro != -1:
            lst[i] = nro
            i = i + 1

    #print("ok")
    return lst


lista = cargarLista()
# b = ingresarNro(1,50)

# TP6 EJ 2
# sumar la lista
suma= 0
qty= 0
i= 0
while i < 50 and lista[i] != 0:
    if lista[i] >= 10:
        suma = suma + lista[i]
        qty= qty + 1
    i = i + 1
print ("La suma es: ", suma)

#TP6 EJ 3
capicua = [5,4,3,2,1,2,3,4,5]
nocapicua = [5,4,3,2,1,2,4,4,5]
print ("Capicua: ", esCapicua(capicua, 9))
print ("NoCapicua: ", esCapicua(nocapicua, 9))


# lista2 = cargarLista()