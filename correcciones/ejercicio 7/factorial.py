def factorial(n):  # Se agregó el parámetro que falta en la definición de la función y se corrigió el operador de comparación en la condición
    if n == 0 or n == 1:  # Se corrigió el operador de asignación (=) a un operador de comparación (==)
        return 1  # Se corrigió el error tipográfico en "return"
    else:
        return n * factorial(n - 1)  # Se corrigió el error tipográfico en "return" y se corrigió el signo menos (-) para restar 1

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")  # Se pasó el número como argumento a la función factorial
