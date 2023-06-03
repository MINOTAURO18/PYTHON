import math 
"""
ejersicios con python
calculadora 
"""


# num1 = input("Ingrese el primer número: ")
# ope = input("Ingrese la operación  [+, -, *, /]: ")
# num2 = input("Ingrese el segundo número: ")
# num1 = float(num1)
# num2 = float(num2)
# if ope == "+":
#     resultado = num1 + num2
# elif ope == "-":
#     resultado = num1 - num2
# elif ope == "*":
#     resultado = num1 * num2
# elif ope == "/":
#     resultado = num1 / num2
# else:
#     print("Operación no válida.")

# print("El resultado es: ", int(resultado))



# cambio de divisas 

# pesos = input('ingrese su valor en pesos: ')
# cambio = input('escoja la moneda de cambio ["Dolares", Euros", "Libras"]: ')

# pesos = float(pesos)
# cambio = cambio.lower()

# if cambio == "dolares":
#     resultado = pesos * 0.00022
# elif cambio == "euros":
#     resultado = pesos * 0.00019
# elif cambio == "libras":
#     resultado = pesos * 0.00016

# else:
#     print('operacion invalida')

# print('resultado: ', int(resultado) , cambio)


#-------------------------------------------------

# nombre = input('cual es tu nombre: ')
# idioma = input('que idioma hablas [Español, Ingles, Portugues, Chino-Mandarin]: ')

# idioma = idioma.lower()

# if idioma == 'chino':
#     print(f'{nombre} 你他媽的是個中國人')

# elif idioma == 'español':
#     print(f'{nombre} eres un latino de mierda(pobre)')

# elif idioma == 'ingles':
#     print(f'{nombre} you are a gringo of shit but you have money)')

# elif idioma == 'portugues':
#     print(f'{nombre} voce e um latino')

# else:
#     print('dato incorrecto')


# 10/5/2023

# 1  Crear un programa que calcule el promedio de tres números ingresados por el usuario.

# num1 = float(input('ingresar primer numero bastardo: '))
# num2 = float(input('ingresar segundo numero bastardo: '))
# num3 = float(input('ingresar tercero numero bastardo: '))

# resultado = num1 + num2 + num3 / 3

# print( f'resultado: {round(resultado,3)}')

#  Crear un programa que pida al usuario ingresar un número entero y luego imprima todos los números pares desde 0 hasta ese número.

#  Crear un programa que pida al usuario ingresar una lista de números separados por comas y luego calcule su suma.

# num1 = float(input('ingrese numero 1: '))
# num2 = float(input('ingrese numero 2: '))
# num3 = float(input('ingrese numero 3: '))
# num4 = float(input('ingrese numero 4: '))

# resu = num1 + num2 + num3 + num4

# print(int(resu))


#  Crear un programa que pida al usuario ingresar una cadena de caracteres y luego imprima su longitud.


#Cálculo de la edad: Pide al usuario que ingrese su fecha de nacimiento y calcula su edad en años.

#Cálculo de la potencia: Pide al usuario que ingrese una base y exponente y calcula la potencia.

# BASE = float(input('ingrese base(osea un numero que le de la puta gana): '))
# POTENCIA = float(input('ingrese potencia (otro numero soimbecil): '))

# RESULT = math.pow(BASE, POTENCIA)
# if POTENCIA < 0:
#     print('anda a joder a tu madre marikita')
# else:
#     print(int(RESULT))

# def NUMERO_RAMDON () :   
#     QUESTION = float(input('escribe un numero: '))

#     RANDON = random.randint(1,100)
#     if QUESTION != RANDON:
#         print(f'{int(QUESTION)} y {RANDON} intenta de nuevo')
#         NUMERO_RAMDON()
#     else:
#         print(f'{QUESTION} y {RANDON} ganaste care verga')

# NUMERO_RAMDON()


#Escriba un programa que tome una lista de números enteros y devuelva el número más grande de la lista.
# def COMPARACION ():   
#   cadena_uno = input('primera valor: ')
#   cadena_dos = input('segundo valor: ')

#   if cadena_uno == cadena_dos:
#       print('son iguales')
#   else:
#       print('no son iguales')
#       COMPARACION()


# COMPARACION()

#es hacer una lista de frutas que la persona pregunta por una fruta y uno debe decir si esta o no




#Calculadora de interés: Crea un programa que solicite al usuario una cantidad de dinero, una tasa de interés y un período de tiempo, y calcule el interés ganado.

#Donde K es el capital inicial
#i es el interés 
#n es el número de periodos

#K*(1+i)^n.
# CAPITAL_INICIAL = input('ingrese su capital: ')
# PERIODO = input('periodo de tiempo: ')

# CAPITAL_INICIAL = float(CAPITAL_INICIAL)
# PERIODO = float(PERIODO)

# RESULTADO = CAPITAL_INICIAL * (1.02) ** PERIODO

# print(f"{RESULTADO:.2f}")

#Validación de contraseñas: Escribe un programa que solicite al usuario una contraseña y valide si cumple con ciertos requisitos, como una longitud mínima y la inclusión de caracteres especiales.
# def PASSWORD_VALIDATOR ():    
#     PASSWORD = input('digite su password: ')

#     if '*' in PASSWORD and len(PASSWORD) > 9:
#         print('contraseña correcta')
#     else:
#         print('contraseña incorrecta')
#         PASSWORD_VALIDATOR()


# PASSWORD_VALIDATOR()
# def AREA ():    
#     RADIO = input('ESCRIBA UN RADIO(un numero gay): ')
#     RADIO = float(RADIO)
#     RESULT = 3.1416 * pow(RADIO,2)
#     print(f"el area del circulo es: {int(RESULT)} cm al cuadrado" )
#     AREA()

# AREA()


#Contador de palabras repetidas: Escribe un programa que reciba un texto y cuente cuántas veces se repite cada palabra en él.

# text = input('escriba una frase: ')
# text2 = text.split(' ')
# primero = text2[0]

# CONTADOR = 0
# for i in text2:
#     if primero == i:
#         CONTADOR += 1
#     print(f'el numero de palabras repetidas es {CONTADOR}')

#Encontrar todos los números pares e impares en una lista.
# question = input('escribe una lista de numeros: ')
# question = list(question)
# questionInt = map(int, question)

# pares = []
# inpares = []

# for i in questionInt:
#     if i % 2 == 0:
#         pares.append(i)

#     else:
#         inpares.append(i)

# print(f"los numeros pares son {pares} y los inpares son {inpares}")

#Verificar si dos listas tienen elementos comunes.


# poderoso
# uno = [6,2,3,4,5]  
# dos = [6,6,6,6]
# combi = uno + dos
# primer = combi[0]
# on=[]
# def com():  
#   for i in combi:
#       if primer == i+1:
#          return on.append('true')
      
#       return on.append('false')
# com()
  
# print(on)

#Escribe una función llamada sumar_digitos(numero) que tome un número entero como parámetro y calcule la suma de sus dígitos.

# def SUMAR (entero):
#     suma = 0
#     for i in entero:
#         suma += int(i)
#     return suma

# print(SUMAR('88644'))



#Escribe una función que tome una lista de números y devuelva la suma de los elementos pares.
# def suma_de_numeros_pares():
#     numeros = [1,2,3,4,5,6,7,8,9,10,11,22]
#     pares = []
#     suma = 0
#     for i in numeros:
#         if i % 2 == 0:
#             pares.append(i)
#     for a in pares:
#         suma = suma + a
#     print(f"los numeros pares de la lista son: {pares}")
#     print(f"la suma de los numeros pares es: {suma}")
# suma_de_numeros_pares()

# Implementa un juego de piedra, papel y tijeras en el que el jugador juegue contra la computadora.
# def ppt():
#     elige = input('Piedra - Papel - Tijera: ')
#     elige = elige.lower()
#     juego = ['piedra', 'papel','tijera']
#     al = random.choice(juego)
#     if elige == al:
#       ppt()
#     elif al == 'piedra' and elige == 'tijera':
#       print('gano la maquina')
#     elif al == 'tijera' and elige == 'piedra':
#        print('ganaste')
#     elif al == 'papel' and elige == 'piedra':
#       print('gano la maquina')
#     elif al == 'piedra' and elige == 'papel':
#       print('ganaste')
#     elif al == 'tijera' and elige == 'papel':
#       print('maquina')
#     elif al == 'papel' and elige == 'tijera':
#       print('ganaste')
#     else:
#       print('largate hija de la chingada')
      
# ppt()
"""
papel gana piedra

piedra gana tijeras

tijera gana papel 
"""

#Crea una función que tome una lista de palabras y devuelva la longitud promedio de las palabras.

# def lista_palabras(lista):
#     suma = 0
#     for i in lista:
#         suma += len(i) 
#     print(suma / len(lista))
# lista_palabras(['alex', 'coste', 'patron', 'santiago', 'chica'])


# Crear una función que calcule el factorial de un número dado.

# Desarrollar un programa que genere una lista de los primeros n números primos.

# def primos(num):
#     if num == 2:
#         return 'es primo'
#     if num < 2:
#         return 'no es primo'
#     for i in range(2,num):
#         if num % i != 0:
#             return 'es primo'
#         else:
#             return 'no es primo'      
   

# print(primos(7))

# def loquesea(n):
#     for i in range(n + 1 ):
#         print(i)

# print(loquesea(10))

# Crear una función que encuentre la suma de todos los números pares en una lista.

# def suma (arr):
#     sumaa = 0;
#     for i in arr:
#         if i % 2 == 0:
#             sumaa += i;
#     return sumaa

# print(suma([1,2,3,4,5,6,7,8,9,10,40]))