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

