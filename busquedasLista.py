## busquedas

lista= [19,5,9,5,33,87,12]
suma= 0

for i in range(0, 7):
    if lista[i] >= 10:
        print(lista[i])   
    suma= suma + lista[i]    
print("Total: ", suma)

val= int(input("V: "))
pos= -1
for i in range(0, 7):
    if lista[i] == val:
        pos= i
print("Posicion : ", pos)

pos= 0
for i in range(0, 7):
    if lista[i] > lista[pos]:
        pos= i
print("Pos Mayor : ", pos)
print("Val Mayor : ", lista[pos])

pos= 0
for i in range(0, 7):
    if lista[i] < lista[pos]:
        pos= i
print("Pos Menor : ", pos)
print("Val Menor : ", lista[pos])

