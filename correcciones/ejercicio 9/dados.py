import random  # Se corrigió el nombre del módulo "radom" a "random"

def simular_lanzamiento_dados(cantidad_dados, caras_por_dado):  # Se corrigieron los parámetros de la función
    resultados = [random.randint(1, caras_por_dado) for _ in range(cantidad_dados)]
    return resultados  # Se corrigió el error tipográfico en "return"

cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))
caras_por_dado = int(input("Ingrese la cantidad de caras por dado: "))
lanzamientos = simular_lanzamiento_dados(cantidad_dados, caras_por_dado)  # Se corrigieron los argumentos en la llamada a la función
print(f"Resultados del lanzamiento: {lanzamientos}")
