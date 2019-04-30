import random

# TORNEO
prj= 0
prm= 0

rondas= 1
while rondas <= 5:
    ## INICIO RONDA    
    pj=0
    pm=0
    
    partidas=1
    while partidas <= 3:
        ## INICIO PARTIDA
        sm= random.randint(1,3)
        sj= int(input("1-Piedra, 2-Papel, 3- Tijera: "))
        print("Maquina: ", sm)
    
        # defino ganador
        if sj == sm:
            #empate
            print("empate")
        elif (sj == 1 and sm == 3) or (sj == 2 and sm == 1) or (sj == 3 and sm == 2):
            # gj
            print("Gano jugador")
            pj= pj+1
        else:
            #gm
            print("Gano maq")
            pm=pm+1
        ## FIN PARTIDA
        partidas = partidas + 1
    # VER QUIEN GANA RONDA
    if pj == pm:
        #empate
        print("e")
    elif pj > pm:
        #gj
        prj= prj+1
    else:
        #gm
        prm=prm+1
    
    ## FIN RONDA
    rondas= rondas + 1
    
## VER QUIEN GANO EL TORNEO
if prj == prm:
    print("emp")
elif prj > prm:
    print("gj")
else:
    print("gm")
