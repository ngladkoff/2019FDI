from isNumber import isNumber

ingreso = input("numero: ")

if not isNumber(ingreso):
    print("no es numero entero")
else:
    print("es numero entero")
    