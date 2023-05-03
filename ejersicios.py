"""
ejersicios con python
calculadora 
"""

#calculadora

# def Calculadora():
num1 = input("Ingrese el primer número: ")
ope = input("Ingrese la operación (+, -, *, /): ")
num2 = input("Ingrese el segundo número: ")
num1 = float(num1)
num2 = float(num2)
if ope == "+":
    resultado = num1 + num2
elif ope == "-":
    resultado = num1 - num2
elif ope == "*":
    resultado = num1 * num2
elif ope == "/":
    resultado = num1 / num2
else:
    print("Operación no válida.")

print("El resultado es: ", int(resultado))


# Calculadora()













