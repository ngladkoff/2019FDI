def esNumero(nro):
    try:
        float(nro)
        return True
    except ValueError:
        return False
