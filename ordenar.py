def Ordenar(lst, MAX):
    print("+++++++ ORDENAR +++++++")
    print(lst)
    for j in range(0,MAX-1):
        for i in range(0, MAX-1):
            if lst[i] > lst[i+1]:
                aux = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = aux
        print(lst)

lista = [70, 10, 60, 30, 25, 90, 8, 5]
lista2 = [70, 10, 60, 30, 25, 90, 8, 5, 3, 80, 12, 54, 45, 67]
Ordenar(lista, 8)
Ordenar(lista2, 14)

def BusquedaBinaria(nro, lst, MAX):
    posSup = MAX - 1
    posInf = 0
    
    while posInf < posSup:
        idx = (posSup + posInf) // 2
        print(posInf, " / ", idx, " / ", posSup)
        if lst[idx] == nro:
            return idx
        if lst[idx] > nro:
            posSup= idx
        else:
            posInf= idx
    return -1    

listaOrdenada = [0] * 100
for i in range(0,100):
    listaOrdenada[i] = i + 1
print("+++++++ LISTA ORDENADA +++++++")
print(listaOrdenada)

nro = 75
pos = BusquedaBinaria(nro, listaOrdenada, 100)
print("El número buscado es: ", nro)
print("Está en la posición: ", pos)
print("Validacion: ", listaOrdenada[pos])



