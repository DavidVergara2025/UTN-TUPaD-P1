# TRABAJO PRACTICO N.6 - ESTRUCTURAS DE DATOS COMPLEJAS
# Vergara, David Emanuel
# Comision 5

# Ejercicio 1:  Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] =  2300
print(precios_frutas)

#===============================================================================================

#Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800 

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] =  2800
print(precios_frutas)

#===============================================================================================

#Ejercicio 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios. 
frutas = list(precios_frutas.keys())
print(frutas)

#===============================================================================================

#Ejercicio 4: Escribí un programa que permita almacenar y consultar números telefónicos. 
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
#• Luego, pedí un nombre y mostrale el número asociado, si existe. 
#Ejemplo:
# contactos = {"Juan": "123456", "Ana": "987654"}
# Consultar: "Juan" -> muestra "123456"

agenda = {}
for i in range(1,6):
    nombre = input(f'Ingrese el nombre del contacto {i}:\n')
    numero = input(f'Ingrese el numero de telefono:\n')
    agenda[nombre] = numero

consulta = input('Ingrese el nombre para conocer el numero registrado:\n')
if consulta in agenda:    
    print(f'El numero de {consulta} es {agenda[consulta]}.')
else:
    print('El contacto no esta en la lista.')

#===============================================================================================

#Ejercicio 5) Solicita al usuario una frase e imprime: 
#• Las palabras únicas (usando un set). 
#• Un diccionario con la cantidad de veces que aparece cada palabra. 
#Ejemplo:
#Entrada -> "hola mundo hola"
# Palabras_unicas: {'hola: 2, 'mundo': 1}

frase = input('Ingrese una frase: \n')
lista_palabras = frase.split()
palabras_unicas = set(lista_palabras) #Convierto la lista en un set
print(palabras_unicas) #Se muestra el set con las palabras unicas

#Recuento de cada palabra en la frase
recuento = {}
for palabra in lista_palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print(recuento)
