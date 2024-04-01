#Realizar una calculadora con la operaciones básicas con funciones

def suma(x,y):
    suma=x+y
    return suma

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

def division(num1, num2):
    res = num1 / num2
    return res

print("Ingrese 2 números")

num1= int(input())
num2= int(input())