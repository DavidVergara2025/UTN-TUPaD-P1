#TRABAJO PRACTICO N°6 - LISTAS
#Alumno: Vergara, David
#Comisión: 5

#Ejercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista1 = list(range(4,101,4))
print(lista1)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista2 = ["a", "b", "c", "d", "e"]
print(lista2[-2])

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. 
# Por ejemplo: lista_vacia = []

unidades = []
unidades.append("secuenciales")
unidades.append("condicionales")
unidades.append("repetitivas")

print(unidades)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos 
# o bien investigar cómo funciona el indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#El programa evalúa los números de la lista buscanado el máximo de ellos, lo elimina de la lista y luego
#muestra la nueva lista (sin el elemento que fue eliminado)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros.

lista_6 = list(range(10,31,5))

print(lista_6[0:2])

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos 
# nuevos valores cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = "corolla", "peugeot"
print(autos)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.

#a) 
compras[2].append("jugo")
#b) Se investiga la función index, para btener el índice del elemento "fideos" y poder reemplazarlo
compras[1][compras[1].index("fideos")] = "tallarines"
#c)
compras[0].remove("pan")
print(compras)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)