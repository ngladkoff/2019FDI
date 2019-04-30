
importe= int(input("Imp. a ext.?: "))

# Calcular billetes de 100
billetes= importe // 100 
resto = importe - billetes * 100
print("Billetes 100: ", billetes)

billetes= resto // 50
resto = resto - billetes * 50
print("Billetes 50: ", billetes)

billetes10= resto // 10
resto = resto - billetes10 * 10
print("Billetes 10: ", billetes10)

billetes5= resto // 5
resto = resto - billetes5 * 5
print("Billetes 5: ", billetes5)

billetes1= resto // 1
resto = resto - billetes1 * 1
print("Billetes 1: ", billetes1)

print("Resto: ", resto)
