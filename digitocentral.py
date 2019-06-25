def ObtenerDigitoCentral(nro):
    strNro= str(nro)
    tamanio = len(strNro)
    
    if tamanio % 2 == 0:
        return -1
    
    pos = (tamanio -1) // 2
    return int(strNro[pos])
    
print("Nro Central. ", ObtenerDigitoCentral(12345678911))