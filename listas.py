nombres=['juan','catalina','luis']
edades=[32,28,25]
descuentos=[True,False,False]

#imprimiendo una lista
print(nombres)
#accediendo a un elemento de la lista
print(nombres[0])

#accediendo a los elementos de una lista
for nombre in nombres:
    print(nombre)
for edad in edades:
    print(edad)
for descuento in descuentos:
    print(descuento)

#agregando elementos a un lista en python
nombres.append('marta')
print(nombres)
