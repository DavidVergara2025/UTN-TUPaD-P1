#TRABAJO PRACTICO N° 7 - RECURSIVIDAD
#Alumno:Vergara, David Emanuel
#Comision: 5

#Ejercicio 1 : Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
num= int(input("Ingrese un numero positivo para calcular su factorial: "))

if num < 0:
    print("Valor invalido")
else:
    print(f"El factorial de {num} es: {factorial(num)}")

#====================================================================================================

#Ejercicio 2: Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
num= int(input("Ingrese la posicion en la serie de Fibonacci: "))

for i in range(num +1):
    print(f"Posicion: {i}. Fibonacci: {fibonacci(i)}")

#====================================================================================================

#Ejercicio 3: Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un 
#algoritmo general.

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m-1)
    
n = float(input("Ingrese la base: "))
m = float(input("Ingrese el exponente: "))
print(f"El resultado es: {potencia(n, m)}")

