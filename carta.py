#MENU OPCIONES
opcion=100

#ciclo/bucle/loop/iteracion




print("MENU DE VOTACION")
print("**************************")
print("1-->calcular la suma")
print("2-->calcular la resta")
print("3-->calcular la multiplicacion")
print("4-->calcular la division")
print("0-->SALIR")
print("***************************")

while(opcion!=0):
    opcion=int(input("Bienvenido, digita una opcion: "))
    if(opcion==1):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}+{numero2}={numero1+numero2}')
    elif(opcion==2):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}-{numero2}={numero1-numero2}')
    elif(opcion==3):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}*{numero2}={numero1*numero2}')
    elif(opcion==4):
        numero1=int(input("digita un numero: "))
        numero2=int(input("digita otro numero: "))
        print(f'{numero1}/{numero2}={numero1/numero2}')
    elif(opcion==0):
        break
    else:
        print(f'Digita una opcion valida')

