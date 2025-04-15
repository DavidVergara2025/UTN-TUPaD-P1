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
#Se llama la funcion para solicitar datos, con el argumento correspondiente en cada uno
nombre = pedir_dato("nombre")
apellido = pedir_dato("apellido")
edad = pedir_dato("edad")
residencia = pedir_dato("residencia")
informacion_personal(nombre, apellido, edad, residencia)

#----------------------------------------------------------------------------------------------------------------

