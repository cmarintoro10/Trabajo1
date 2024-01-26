def es_palindromo(texto):  # Se agregó el parámetro que falta en la definición de la función
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra_frase):  # Se pasó la palabra o frase como argumento a la función es_palindromo
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
