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

#====================================================================================================

#Ejercicio 4: Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación
# en binario como una cadena de texto.

def decimal__a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return str(decimal__a_binario(n//2))+str(n % 2)
    
n = int(input("Ingrese en numero entero decimal a convertir: "))
print(decimal__a_binario(n))

#====================================================================================================

#Ejercicio 5: Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    def invertida(palabra):
        if len(palabra) == 0:
            return palabra
        else:
            return palabra[-1] + invertida(palabra[:-1])
    return palabra == invertida(palabra)

palabra = input("Ingrese la palabra a evaluar: ").lower()
if es_palindromo(palabra):
    print("Es palindromo")
else:
    print("No es palindromo")

#====================================================================================================

#Ejercicio 6: Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma
# de todos sus dígitos.
#Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingrese un numero entero positivo: "))
print(f"La suma de los digitos de {n} es {suma_digitos(n)}")
        
#====================================================================================================

#Ejercicio 7:Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1),
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita
# para construir toda la pirámide.
#Ejemplos:
#contar_bloques(1) → 1 (1)
#contar_bloques(2) → 3 (2 + 1)
#contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
n = int(input("Ingrese el numero de bloques del nivel mas bajo: "))
print(f"El numero de bloques necesarios es {contar_bloques(n)} bloques")

