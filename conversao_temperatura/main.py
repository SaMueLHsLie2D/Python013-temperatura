from fahrenheit_to_celsius import fahrenheit_to_celsius


def main():
    f = input("Digite a temperatura em Fahrenheit: ")
    try:
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F equivalem a {c:.2f}°C")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
