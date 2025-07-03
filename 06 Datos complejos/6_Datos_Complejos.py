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

#=====================================================================================================================

#Ejercicio 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno. Ejemplo:
#alumnos = {
#"Sofía": (10, 9, 8),
#"Luis": (6, 7, 7)
#}

#Funcion para ingresar los nombres de los alumnos
def nombres_alumnos():
    nombres = []
    for i in range(3):  
        nombre = input(f"Ingrese el nombre del alumno N°{i+1}: ")
        nombres.append(nombre)
    return nombres

#Funcicon para ingresar las notas de los alumnos
def notas_alumnos(nombres):
    alumnos_notas = {}
    for nombre in nombres:
        notas = []
        print(f"Ingrese las notas para {nombre}:")
        for j in range(3):
            nota = float(input(f"Nota N°{j+1}: "))
            notas.append(nota)
        alumnos_notas[nombre] = tuple(notas)
    return alumnos_notas

# Función para calcular promedios:
def calcular_promedios(alumnos_notas):
    promedios = {}
    for nombre, notas in alumnos_notas:
        promedio = sum(notas) / len(notas)
        promedios[nombre] = promedio
    return promedios

def main():
    nombres = nombres_alumnos()
    print("Nombres de los alumnos:", nombres)
    alumnos_notas = notas_alumnos(nombres)
    print("Alumnos y sus notas:", alumnos_notas)
    promedios = calcular_promedios(alumnos_notas.items())
    print(f"Promedios de los alumnos: ")
    for nombre, promedio in promedios.items():
        print(f"{nombre}: {promedio:.2f}")

main()

#=====================================================================================================================

#Ejercicio 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {1, 2, 6, 7, 10, 13, 15, 18, 19, 20, 24, 26, 28}
parcial_2 = {2, 3, 5, 6, 7, 9, 11, 13, 17, 18, 19, 20, 22, 23, 25, 26, 27}
# Estudiantes que aprobaron ambos parciales
def ambos(parcial_1, parcial_2):
    ambos = []
    for i in parcial_1:
        if i in parcial_2:
            ambos.append(i)
    return ambos

# Estudiantes que aprobaron solo uno de los dos
def solo_uno(parcial_1, parcial_2):
    solo = []
    for i in parcial_1:
        if i not in parcial_2:
            solo.append(i)
    for j in parcial_2:
        if j not in parcial_1:
            solo.append(j)
    return solo

# Estudiantes que aprobaron al menos un parcial (sin repetir)
def al_menos_un_parcial(parcial_1, parcial_2):
    al_menos_uno = []
    for i in parcial_1:
        if i not in parcial_2:
            al_menos_uno.append(i)
    for j in parcial_2:
        if j not in al_menos_uno:
            al_menos_uno.append(j)
    al_menos_uno.sort()  # Ordenar la lista para una mejor presentación
    return al_menos_uno

print("Estudiantes que aprobaron ambos parciales:", ambos(parcial_1, parcial_2))
print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno(parcial_1, parcial_2))
print("Estudiantes que aprobaron al menos un parcial (sin repetir):", al_menos_un_parcial(parcial_1, parcial_2))

