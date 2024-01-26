def calcular_precio_con_descuento(precio_base, porcentaje_descuento):  # Se corrigió el nombre de la función
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final  # Se corrigió el error tipográfico en "return"

precio_base = float(input("Ingrese el precio base del producto: "))  # Se corrigió la solicitud de entrada del usuario
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
