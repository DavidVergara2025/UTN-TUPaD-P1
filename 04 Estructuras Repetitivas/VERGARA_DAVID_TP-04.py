#TRABAJO PRÁCTICO N°4 - ESTRUCTURAS REPETITIVAS
#Alumno: Vergara, David
#Comisión: 5

#Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (101):
    print(i)

#==========================================================================

#Ejercicio 2: 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
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
