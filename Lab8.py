# Conversor de Temperatura

def convertir_temperatura(temperatura, unidad):
    try:
        if unidad.upper() == 'C':
            # De Celsius a Fahrenheit
            fahrenheit = (temperatura * 9/5) + 32
            return f'{temperatura}°C son {fahrenheit:.2f}°F'
        elif unidad.upper() == 'F':
            # De Fahrenheit a Celsius
            celsius = (temperatura - 32) * 5/9
            return f'{temperatura}°F son {celsius:.2f}°C'
        else:
            return 'Unidad no válida. Usa "C" para Celsius o "F" para Fahrenheit.'
    except Exception as e:
        return f'Error: {e}'

# Ejemplo de uso
temp = float(input("Ingresa la temperatura: "))
unidad = input("Ingresa la unidad (C o F): ")
print(convertir_temperatura(temp, unidad))

