## Listas
## TP6 Ej 3
def esCapicua(lista, tamanio):
 
     idx= 0
     idx2= tamanio - 1
     
     while idx<idx2:
         if lista[idx] != lista[idx2]:
             return False
     
         idx = idx + 1
         idx2 = idx2 - 1
 
     return True

capicua = [5,4,3,2,1,2,3,4,5]
nocapicua = [5,4,3,2,1,2,4,4,5]
print ("Capicua: ", esCapicua(capicua, 9))
print ("NoCapicua: ", esCapicua(nocapicua, 9))
print("Prueba: ", esCapicua("neuquen", 7))
print("Prueba2: ", esCapicua("neuqen", 6))
