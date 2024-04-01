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

operacion=int(input("Elija la operación que desea realizar:\n1.Suma \n2.Resta \n3.Multiplicación \n4.Division\n"))

if(operacion==1):
    print(f"El resultado de la suma es {suma(num1,num2)}")
elif(operacion==2):
    print(f"El resultado de la resta es {resta(num1,num2)}")
elif(operacion==3):
    print(f"El resultado de la multiplicación es {multiplicacion(num1,num2)}")
elif(operacion==4):
    if(num2==0):
        print("Error, no se puede deividir entre 0")
    else:
        print(f"El resultado de la división es {division(num1,num2)}")
else:
    print("Opción incorrecta")