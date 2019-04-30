Habitacion = 1
 
def CostoHabitacion(H):
    if H == 1:
        return 600
    
    if H == 2:
        return 800
    
    if H == 3:
        return 1000
 
     return -1
 
Habitaciones = 0
 
while Habitacion > 0:
    
    Habitacion = int(input("Tipo de habitacion: "))
     
    Dinero = CostoHabitacion(Habitacion)
     
    if Habitacion > 0:
         
        Dias = int(input("Dias ocupados: "))
         
        CostoDia = Dinero * Dias
         
        Ubicacion = int(input("Ubicacion: "))
         
        if Ubicacion == 1:
            CostoExtra = CostoDia * 1.10
         
        elif Ubicacion == 2:
            CostoExtra =  CostoDia
         
        print("Costo de la Habitacion: ", CostoExtra)
             
        Habitaciones = Habitaciones + 1
        
print("Habitaciones: ", Habitaciones)
