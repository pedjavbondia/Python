#Función para Calcular el Factorial de un Número

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def General():
    print("\n Función para Calcular el Factorial de Cualquier Número")
    n=int(input("\n Ingrese el número del cual desea calcular su factorial: "))
    if n <0:
        print("\n Por favor ingresar un número positivo.")
    else:
        print("\n El factorial de {} es {}".format(n,factorial(n)))

General()
