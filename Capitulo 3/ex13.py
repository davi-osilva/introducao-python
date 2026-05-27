def validar_temperatura_celsius():
    while True:
        try:
            return int(input("Digite o valor da temperatura em celsius: "))
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def transformar_em_fahrenheit(celsius: int) -> int:
    return (9 * celsius) // 5 + 32

def main():
    celsius = validar_temperatura_celsius()
    fahrenheit = transformar_em_fahrenheit(celsius)

    print(f"{celsius} °C = {fahrenheit} °F")

if __name__ == "__main__":
    main()