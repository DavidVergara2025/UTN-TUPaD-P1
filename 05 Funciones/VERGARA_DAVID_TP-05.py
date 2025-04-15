#TRABAJO PRACTICO N°5 - FUNCIONES
#Alumno: Vergara, David Emanuel
#Comisión: 5

#Ejercicio 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal

#Se define la funcion:
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Se llama a la función:
imprimir_hola_mundo()

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva
#  un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”.
#  Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#DEFINICION DE FUNCIONES
#Se define funcion saludar
def saludar_usuario(nombre):  
    print(f"Hola, {nombre}!")

#PROGRAMA PRINCIPAL
nombre = input("¿Cómo te llamás?: ")
saludar_usuario(nombre)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba 
# cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los 
# datos al usuario y llamar a esta función con los valores ingresados.

#FUNCIONES
#Se crea función para imprimir mensaje con la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Se crea una función para solicitar datos al usuario
def pedir_dato(dato):
    informacion = input(f"Ingrese su {dato}: ")
    return informacion

#PROGRAMA PRINCIPAL
#Se llama la funcion que imprimirá la informacion personal, utilizando la funcion pedir_dato para completar cada argumento correspondiente

informacion_personal(pedir_dato("nombre"), pedir_dato("apellido"), pedir_dato("edad"), pedir_dato("residencia"))

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como parámetro y devuelva el 
# perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#Se importa el valor pi de la librería math:
from math import pi

#FUNCIONES:

#Área del círculo:
def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return area

#Perímetro:
def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

#PROGRAMA PRINCIPAL
radio = float(input("Ingrese el valor del radio: "))
#Se imprimen los valores llamando las funciones correspondeintes
print (f"""El área del círculo es de {calcular_area_circulo(radio)}.
El perímetro del circulo es de {calcular_perimetro_circulo(radio)}.""")

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos 
# como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar 
# el resultado usando esta función.

#FUNCIONES
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

#PROGRAMA PRINCIPAL
#Se solicita dato a usuario
segundos = int(input("Ingrese la cantidad de segundos a convertir en horas: "))
#Se imprime el resultado usando la función
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas")

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e 
# imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

#FUNCIONES
def tabla_multiplicar(numero):
    for i in range (1,11):
        print (f"{numero} * {i} = {numero*i}")

#PROGRAMA PRINCIPAL
#Se solicita el número al usuario
numero = int(input("Ingrese el número del cual desea ver las tablas del 1 al 10: "))
#Se llama a la funcion
tabla_multiplicar(numero)

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y 
# devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los 
# resultados de forma clara.

#FUNCIONES
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    if b == 0:
        div = "No se puede dividir por 0."
    else:
        div = a / b
    return (suma, resta, mult, div)

def mostrar_resultados(a, b, resultados):
    print(f"""{a} + {b} = {resultados[0]} 
{a} - {b} = {resultados[1]}
{a} * {b} = {resultados[2]}
{a} / {b} = {resultados[3]}
""")

#PROGRAMA PRINCIPAL
#Se solicitan los números al usuario
a = float(input("Ingrese el 1° número: "))
b = float(input("Ingrese el 2° número: "))

#Se llaman las funciones. En la segunda función, el argumento "resultados" es la tupla devuelta en la primera función:

operaciones_basicas(a, b)
mostrar_resultados(a, b, operaciones_basicas(a, b))

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura 
#en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales   

#FUNCIONES
def calcular_imc(peso, altura):
    IMC = peso / altura**2
    return IMC

#PROGRAMA PRINCIPAL

#Solicitud de datos:
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))

#Se muestra el resultado con solo dos decimales (:.2f)
print(f"Su IMC es {calcular_imc(peso, altura):.2f}")

#----------------------------------------------------------------------------------------------------------------

#Ejercicio 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
#y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando 
# la función.

#FUNCIONES
def celsius_a_fahrenheit(celsius):
    F = 9/5*celsius + 32
    return F

#PROGRAMA PRINCIPAL
celsius = float(input("Ingrese la temperatura en °C: "))
print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius)} °F")

#----------------------------------------------------------------------------------------------------------------

