def ler_numeros() -> list[int]:
    numeros = []
    for i in range(1, 3):
        while True:
            try:
                numero = int(input(f"Digite o número {i}: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Utilize somente números")

    return numeros

def somar_numeros(numeros: list[int]) -> int:
    return sum(numeros)

def main() -> None:
    numeros = ler_numeros()
    print(f"A soma dos números vale {somar_numeros(numeros)}")

if __name__ == "__main__":
    main()