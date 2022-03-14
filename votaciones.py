

print("**************************")
print("MENU DE CONTEO DE VOTOS")
print("**************************")

opcion=0
opcion2=0
senado=0
camara=0
pacto=0
centro=0
derecha=0

while(opcion!=4):
    #imprimo opciones
    print("\n1)senado \n2)camara \n3)consulta \n4)salir\n5)Mostrar votos")
    opcion=int(input("Bienvenido, digita una opcion: "))
    if opcion==1:
        senado+=1
    elif opcion==2:
        camara+=1
    elif opcion==3:
        print("\n1)Pacto \n2)Centro \n3)Derecha \n4)Salir")
        #evaluar condicion del usuario
        if opcion==1:
            pacto+=1
        elif opcion==2:
            centro+=1
        elif opcion ==3:
            derecha+=1
    elif opcion==5:
        print(f'los votos para el senado son: {senado}\n los votos para camara son: {camara}\n Los votos para consultas son: \n pacto={pacto}\n centro={centro}\n Derecha={derecha}')

