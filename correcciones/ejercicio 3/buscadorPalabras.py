def contar_palabra(texto, palabra):  # Se agregó el parámetro que falta en la definición de la función
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

# Se corrigió el formato de f-string para que la llamada a la función se realice dentro de las llaves
print(f"La palabra '{palabra_buscada}' aparece {contar_palabra(texto, palabra_buscada)} veces.")
