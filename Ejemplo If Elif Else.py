importe = int(input("Ingrese el importe: "))

if importe<1000:
   descuento = importe*0.05
   print ("Descuento",descuento)
elif importe < 5000: 
   descuento = importe*0.10
   print ("Descuento",descuento)
else:
   descuento = importe*0.15
   print ("Descuento",descuento)
    
print ("Neto a Pagar:",importe-descuento)
