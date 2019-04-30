from esNumero import esNumero

def menu():
    print("1-Sumar")
    print("2-Restar")
    print("3-Mult")
    print("4-Potencia")
    print("5-Salir")

def ingresarEntero():
    ok= 0
    resp= 0
    while ok==0:
        ret= input("Ingrese Entero: ")
        if esNumero(ret):
            resp= int(ret)
            ok=1
        else:
            print("ingrese numero valido")
    return resp
            

def sumar(p1, p2):
    return p1 + p2
    
def restar(val1, val2):
    return val1 - val2

def multiplicar(nro1, nro2):
    i= 0
    resp= 0
    while i < nro2:
        resp= sumar(resp, nro1)
        i= i+1
    return resp

def potencia(nro1, nro2):
    i= 0
    resp= 1
    while i < nro2:
        resp= multiplicar(resp, nro1)
        i= i+1
    return resp


menu()
opc= ingresarEntero()
if opc== 1:
    #sumar
    print("suma 2 + 3: ", sumar(2, 3))
elif opc==2:
    #restar
    print("resta 7 - 3: ", restar(7, 3))
elif opc == 3:
    print("2 * 5 = ", multiplicar(2, 5))
elif opc == 4:
    print("2 * 5 = ", potencia(2, 5))
    
else:
    #salir
    print("chau!")