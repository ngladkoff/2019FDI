edades= [0] * 20
for i in range (0,20):
    edades[i]= int(input("Ingrese edad: "))
    
acc= 0
qty= 0
for i in range(0,20):
    if edades[i] > 30:
        acc = acc + edades[i]
        qty= qty + 1
    
print("promedio ", acc/qty)
