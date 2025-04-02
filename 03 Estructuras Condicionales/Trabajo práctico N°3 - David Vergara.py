#TRABAJO PRÁCTICO N°3 - ESTRUCTURAS CONDICIONALES
#ALUMNO: VERGARA, DAVID EMANUEL
#Comisión : 5

#EJERCICIO 1 : Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
#Restricción para valores menores a 0:
if edad < 0:
    print("El número ingresado no es válido")

    #Condicion mayor de edad
elif edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
#===================================================================================


#Ejercicio 2
#Escribir un programa que solicite su nota al usuario.
nota = float(input("Ingrese su nota: "))
#Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
#(Se agrega restricción para no ingresar valores fuera del rango)
if (0 <= nota <=10):
    if nota >= 6:
        print("Aprobado")
     # en caso contrario deberá mostrar el mensaje “Desaprobado”.   
    else:
        print("Desaprobado")
#Instrucción si no cumple con la restricción
else:
    print("Valor inválido")

#======================================================================================================

#Ejercicio 3
#Escribir un programa que permita ingresar solo números pares. 
#Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
#en caso contrario, imprimir por pantalla "Por favor, ingrese un número par"

#Pedir dato al usuario
num = int(input("Ingrese un número par: "))

#Evaluar si es par mediante el uso del operador de módulo (%) e imprimir el mensaje correspondiente
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#======================================================================================================

#Ejercicio 4:  Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

#Solicitud de datos al usuario:
edad = int(input("Ingrese su edad: "))
#Restricción de datos válidos y clasificación por edad
if edad < 0:
    print("Por favor, ingrese una edad válida.")
elif edad < 12:
    print("Niño")
elif edad < 18:
    print ("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto mayor")

#======================================================================================================

#Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

#Solicitud de datos al usuario
clave = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

    #Se evalúa la longitud y se valida si es correcta:

if 8 <= len(clave) <= 14:
        print("Ha ingresado una contraseña correcta")
else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#======================================================================================================

#Ejercicio 6: Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare 
# para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Se importan las funciones necesarias del paquete statistics y random:
from statistics import mode, median, mean
import random

#Se genera una lista de 50 números enteros aleatorios y los muestra por pantalla:
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"Lista de números: {numeros_aleatorios}")

#Se calculan moda, mediana y media, y se muestran por pantalla:
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print(f"Moda: {moda}; Mediana: {mediana}; Media:{media}")

#Se comparan valores y se determina si hay sesgo. Se imprime el resultado por pantalla:
if media > mediana> moda:
    print("El sesgo es positivo")
elif media < mediana < moda:
    print("El sesgo es negativo")
elif media == mediana == moda:
    print("Sin sesgo")

#======================================================================================================

#Ejercicio 7: Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#Solicitud de cadena al usuario.
cadena = input("Ingrese una palabra o frase: ")

#Se aisla el último caracter y se pasa a minúsculas para luego analizarlo:
ultimo = cadena[-1].lower()

#Analizar último caracter de la cadena mediante indexación []. Determinar si es vocal (más prolijo con listas):
if ultimo == "a" or ultimo == "e" or ultimo == "i" or ultimo == "o" or ultimo == "u":
    print(cadena+"!")
else:
    print(cadena)

#======================================================================================================

#Ejercicio 8: Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee

#Solicitud de nombre y opción al usuario:
nombre = input("Ingrese su nombre: ")
print("Seleccione una de las siguientes opciones: ")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre con la primera letra mayúscula")
opcion = int(input("Ingrese la opción correspondiente:"))

#Conversión según la opción seleccionada y restricción:
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("La opción ingresada es incorrecta.")

#======================================================================================================

#Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes 
# categorías según la escala de Richter e imprima el resultado por pantalla:
#●Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible)
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#Solicitud de valor al usuario:
magn = float(input("Ingrese la magnitud del terremoto en escala de Richter: "))

#Categorización e impresión de resultado: 
if magn < 0:
    print("Valor incorrecto.")
elif magn < 3:
    print("Muy leve (imperceptible)")
elif magn <4:
    print("Leve (ligeramente perceptible)")
elif magn < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magn < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magn < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#======================================================================================================

#Ejercicio 10: Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

#Se pide al usuario datos de hemisferio(se valida), mes y día, y se convierte a minúsculas:
hemi = input("Ingrese su hemisferio (N o S): ").lower()
if not(hemi == "n" or hemi == "s"):
    print("Ingrese un hemisferio correcto.")
else:
    mes = input("Ingrese el nombre del mes: ").lower()
    dia = int(input("Ingrese el día del mes: "))

    #Validación de fecha. Si no es una fecha válida, se imprime un mensaje de error y se cierra el programa.
    if not((mes=="febrero" and 0<dia<=29) or ((mes=="enero" or mes=="marzo" or mes=="mayo" or mes=="julio" or mes=="agosto" or mes=="octubre" or mes=="diciembre")and 0<dia<=31) or ((mes=="abril" or mes=="junio" or mes == "septiembre" or mes == "setiembre" or mes=="noviembre")and 0<dia<=30)):
        print("La fecha ingresada no es válida")
        
    #Determinar si es invierno o verano (periodo 21/12 a 20/03) según hemisferio:
    elif (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia<=20):
        if hemi == "n":
            print("Usted se encuentra en Invierno.")
        else:
            print("Usted se encuentra en Verano.")

    #Determinar si es otoño o primavera (periodo 21/03 a 20/06) según el hemisferio:
    elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia<=20):
        if hemi == "n":
            print("Usted se encuentra en Primavera.")
        else:
            print("Usted se encuentra en Otoño.")

    #Determinar si es invierno o verano (periodo 21/06 a 20/09) según hemisferio:
    elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or ((mes == "septiembre" or mes == "setiembre") and dia<=20):
        if hemi == "n":
            print("Usted se encuentra en Verano.")
        else:
            print("Usted se encuentra en Invierno.")
    
    #Determinar si es otoño o primavera (periodo restante 21/09 a 20/12)según el hemisferio:
    elif hemi == "n":
            print("Usted se encuentra en Otoño.")
    else:
            print("Usted se encuentra en Primavera.")
