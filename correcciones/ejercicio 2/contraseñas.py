import random  # Se corrige el nombre del módulo "rando" a "random"
import string

# Se añade el parámetro 'longitud' en la definición de la función
def generar_contraseña(longitud=8):  # Se añade el signo de igual para definir un valor predeterminado para 'longitud'
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña  # Se corrige "retunr" a "return" para que la función devuelva la contraseña

# Se corrige el nombre de la función de "generar_contrasena" a "generar_contraseña"
print(generar_contraseña())  # Se corrige el nombre de la función a llamar para que coincida con su definición
