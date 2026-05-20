def ler_metros() -> float:
    while True:
        try:
            metros = float(input("Digite a medida em metros: "))
            if metros < 0:
                print("Entrada inválida. Não utilize números negativos")
                continue
            return metros
        except ValueError:
            print("Entrada inválida. Utilize somente números")

def transformar_milimetros(metros: float) -> float:
    return metros * 1000

def main() -> None:
    metros = ler_metros()
    milimetros = transformar_milimetros(metros)
    print(f"{metros:.2f} m = {milimetros:.2f} mm")

if __name__ == "__main__":
    main()