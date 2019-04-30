def CalcularTiempo (var1,var2):
    if var2 == 1:
        ## print("Ambulancia llega en 15m,")
        return "Ambulancia llega en 15m"
    elif var2 == 2:
        #print("Ambulancia llega en 30m.")
        return "Ambulancia llega en 30m."
    elif var1 >= 59 and var2 == 3:
        #print("Ambulancia llega en 2 horas.")
        return "Ambulancia llega en 2 horas."
    elif var1 < 59 and var2 == 3:
        #print("Ambulancia llega en 4 horas.")
        return "Ambulancia llega en 4 horas."

edad = 0
while edad >=0:
    edad= int(input("Edad del paciente: "))
    if edad >= 0:
        gravedad= int(input("Codigo de gravedad: "))
        tiempo= CalcularTiempo(edad,gravedad)
        print("Tiempo: ", tiempo)
