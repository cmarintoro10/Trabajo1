def celsius_a_fahrenheit(celsius):  # Se agregó el signo de dos puntos para definir la función correctamente
    return (celsius * 9/5) + 32  # Se agregó el operador de suma para corregir la fórmula de conversión

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))  # Se corrigió la solicitud de entrada del usuario
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
