def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Se corrigió la falta de dos puntos al final de la línea y se añadió el +1 para incluir el límite superior en el rango
        if numero % i == 0:
            return False  # Se corrigió el error tipográfico en "return"
    return True  # Se corrigió el error tipográfico en "return"

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(num)]  # Se pasó el número actual como argumento a la función es_primo
print("Números primos:", primos)
