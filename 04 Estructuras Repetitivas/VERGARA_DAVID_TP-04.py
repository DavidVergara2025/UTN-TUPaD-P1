#TRABAJO PRÁCTICO N°4 - ESTRUCTURAS REPETITIVAS
#Alumno: Vergara, David
#Comisión: 5

#Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (101):
    print(i)

#==========================================================================

#Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Se inicia contador de dígitos en 1 y se pide número al usuario
cont = 1
num = int(input("Ingrese un número entero: "))

#Si el número es mayor o igual a 10 positivo o negativo, se divide por 10 y se incrementa un dígito en cada repetición:
while num >= 10 or num <= -10:
    num = num/10
    cont +=1
#Se imprime la cantidad de dígitos hallados
print(cont)

#=====================================================================================================

#Ejercicio 3: Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

# Se solicitan dos números al usuario:
num1 = int(input(" Ingrese el primer número entero: "))
num2 = int(input(" Ingrese el segundo número entero: "))

#Se ordenan los números
if num1 >num2:
   mayor = num1
   num1 = num2
   num2 = mayor

#Se inicia el acumulador "suma" en 0. Se usa un bucle "for" para repetir la suma de cada número, excluyendo los dos extremos:
suma = 0
for i in range (num1+1, num2):
   suma += i

print(f"La suma de los números entre ambos valores(excluyéndolos) es {suma}")


#======================================================================================================================

#Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Se define valor inicial suma en 0 y se comienzan a pedir valores al usuario
suma = 0
num = int(input("Ingrese los números enteros que desea sumar (Ingrese 0 para finalizar): "))

#Si el usuario no presiona 0, se van sumando los valores que ingresa, y solicita un nuevo valor:

while num != 0:
    suma += num
    num = int(input("Ingrese el siguiente valor, o 0 para finalizar: "))

#Al ingresarse el 0, finaliza el bucle e imprime la suma total:
print(f"Total acumulado: {suma}")

#======================================================================================================================

#Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número

import random
#Se genera un número aleatorio y se inicia el contador de intentos en 1:
numAleat = random.randint(0,9)
cont = 1

#Se pide un número al usuario al menos una vez y se compara. Si es incorrecto, se pide un nuevo valor hasta coincidir y se cuentan los intentos:
num = int(input("Adiviná el número secreto entre 0 y 9: "))
while num != numAleat:
    cont += 1
    num = int(input("Incorrecto! Intentá de nuevo: "))

#Cuando coincide, se imprime un mensaje y se muestra la cantiadad de intentos:

print(f"Correcto! Cantidad de intentos: {cont}")

#======================================================================================================================

#Ejercicio 6:Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for i in range(98,0,-2):
    print(i)

#======================================================================================================================


