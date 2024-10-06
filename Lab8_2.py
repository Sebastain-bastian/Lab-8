# Calculadora Simple

def calculadora_simple(num1, num2, operacion):
    try:
        if operacion == '+':
            return num1 + num2
        elif operacion == '-':
            return num1 - num2
        elif operacion == '*':
            return num1 * num2
        elif operacion == '/':
            return num1 / num2
        else:
            return 'Operación no válida. Usa +, -, * o /.'
    except ZeroDivisionError:
        return 'Error: No se puede dividir entre cero.'
    except Exception as e:
        return f'Error: {e}'

# Ejemplo de uso
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
print(calculadora_simple(num1, num2, operacion))