nota1= 0
while nota1 != -1:
    nota1 = int(input("ingrese nota 1: "))
    if nota1 != -1:
        nota2 = int(input("ingrese nota 2: "))


        if nota1>=7 and nota2>=7:
            print("Promociona")

        elif nota1 >=4 and nota2 >= 4:
            print("Aprobado")
            
        elif nota1 < 4 and nota2 < 4:
            print("desaprobado")
            
        else:
            if nota1<nota2:
                print("recupera parcial 1")
            else:
                print("recupera parcial 2")
print("fin")
        