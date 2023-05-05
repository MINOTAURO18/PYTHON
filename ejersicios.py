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

pesos = input('ingrese su valor en pesos: ')
cambio = input('escoja la moneda de cambio ["Dolares", Euros", "Libras"]: ')

pesos = float(pesos)
cambio = cambio.lower()

if cambio == "dolares":
    resultado = pesos * 0.00022
elif cambio == "euros":
    resultado = pesos * 0.00019
elif cambio == "libras":
    resultado = pesos * 0.00016
else:
    print('operacion invalida')

print('resultado: ', resultado , cambio)















