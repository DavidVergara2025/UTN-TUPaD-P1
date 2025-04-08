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

#Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#Se solicita un número al usuario:
num = int(input("Ingrese un número entero positivo: "))

#Se restringe entrada de datos a valores positivosy sepide nuevo valor al usuario en caso de corresponder:
while num <0:
    print("El valor ingresado no es válido")
    num = int(input("Ingrese un número entero positivo: "))

#Mediante el bucle for, se realiza la suma de cada número desde el 0 hasta el número ingresado por el usuario, excluyendo ese valor:
suma = 0
for i in range(0,num):
    suma += i

print(suma)

#======================================================================================================================

#Ejercicio 8: Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Se inician los acumuladores en 0 (pares, impares, positivos y negativos, y neutro si es 0):
par = 0
impar = 0
neg = 0
pos = 0
neutro = 0
#Se pide al usuario ingresar 100 números enteros, mediante el bucle for:
for i in range(1,101):
    num = int(input(f"Ingrese el {i}° número entero: "))
    #Se evalúa si es par, y se incrementa la variable correspondiente:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    #Se evalúa si es positivo negativo, y se incrementa la variable correspondiente:
    if num < 0:
        neg +=1
    elif num > 0:
        pos += 1
    else:
        neutro += 1

#Se muestran en pantalla los totales:
print(f"""
Pares: {par}
Impares: {impar}
Positivos: {pos}
Negativos: {neg}
Neutros: {neutro}
""")

#======================================================================================================================

#Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#Se pide al usuario ingresar 100 números enteros, mediante el bucle for, y se suman en cada repetición:
suma = 0
for i in range(1,101):
    num = int(input(f"Ingrese el {i}° número entero: "))
    suma += num

#Se muestra el resultado en pantalla:
print(f"La media de los valores ingresados es: {suma/100}")

#======================================================================================================================

#Ejercicio 10: Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Se solicita un valor al usuario:
num =int(input("Ingrese el número a invertir: "))

#Se toman los restos de dividir por 10 en cada ciclo(como texto), y se unen de manera invertida a una nueva variable(invertida)
#Por último, se realiza la división entera por 10 hasta que el resto es 0:

invertido = ""
while num > 0:
    resto = str(num % 10)
    invertido = (invertido+resto)
    num = num//10

print(f"Su número invertido es: {invertido}")