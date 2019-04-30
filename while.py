mayor = 0
numero = 0
indice = 0

while indice < 10:
    numero = int(input("nro:"))
    if numero > mayor:
        mayor= numero
    indice = indice + 1

print("mayor: ", mayor)
