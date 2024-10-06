# Generador de Contraseñas Aleatorias

import random
import string

def generar_contraseña(longitud, mayusculas=True, minusculas=True, numeros=True, especiales=True):
    try:
        caracteres = ''
        if mayusculas:
            caracteres += string.ascii_uppercase
        if minusculas:
            caracteres += string.ascii_lowercase
        if numeros:
            caracteres += string.digits
        if especiales:
            caracteres += string.punctuation
        
        if not caracteres:
            return 'Error: Debes seleccionar al menos un tipo de carácter.'
        
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contraseña
    except Exception as e:
        return f'Error: {e}'

# Ejemplo de uso
longitud = int(input("Ingresa la longitud de la contraseña: "))
mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
numeros = input("¿Incluir números? (s/n): ").lower() == 's'
especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

print(generar_contraseña(longitud, mayusculas, minusculas, numeros, especiales))