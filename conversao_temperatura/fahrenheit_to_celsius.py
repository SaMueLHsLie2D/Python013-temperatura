def fahrenheit_to_celsius(fahrenheit):

    try:
        return (float(fahrenheit) - 32) / 1.8
    except ValueError:
        raise ValueError("Temperatura inválida. Deve ser um número.")
