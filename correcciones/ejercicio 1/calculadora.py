# Corrección del código con comentarios

# Se solicita al usuario ingresar el primer número y se convierte a tipo float
num1 = float(input("Ingrese el primer número: "))

# Se solicita al usuario ingresar el segundo número y se convierte a tipo float
num2 = float(input("Ingrese el segundo número: "))

# Se realiza la suma entre num1 y num2, previamente definidos por el usuario
suma = num1 + num2

# Se realiza la resta entre num1 y num2, previamente definidos por el usuario
resta = num1 - num2

# Se verifica que num2 no sea cero antes de realizar la división
if num2 != 0:
    # Se realiza la división entre num1 y num2, previamente definidos por el usuario
    division = num1 / num2
else:
    division = "Error: división por cero"

# Se realiza la multiplicación entre num1 y num2, previamente definidos por el usuario
multiplicacion = num1 * num2

# Se imprime el resultado de la suma, resta, multiplicación y división
# Los resultados se convierten a cadenas para poder concatenarlos en la salida
print("Resultado de la suma:", str(suma))
print("Resultado de la resta:", str(resta))
print("Resultado de la multiplicación:", str(multiplicacion))
print("Resultado de la división:", str(division))
