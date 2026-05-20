def ler_salario() -> float:
    while True:
        try:
            salario = float(input("Digite o seu salário: "))
            if salario < 0:
                print("Entrada inválida. Não utilize valores negativos")
                continue
            return salario
        except ValueError:
            print("Entrada inválida. Utilize somente números")

def ler_porcentagem() -> float:
    while True:
        try:
            porcentagem = float(input("Digite a porcentagem do aumento: "))
            if porcentagem < 0:
                print("Entrada inválida. Não utilize valores negativos")
                continue
            return porcentagem / 100
        except ValueError:
            print("Entrada inválida. Utilize somente números")

def calcular_novo_salario(salario: float, porcentagem: float) -> float:
    return (salario * porcentagem) + salario

def main() -> None:
    salario = ler_salario()
    porcentagem = ler_porcentagem()
    novo_salario = calcular_novo_salario(salario, porcentagem)
    aumento = novo_salario - salario
    print(f"O seu novo salário será de R$ {novo_salario:.2f}, então houve um aumento de R$ {aumento:.2f}")

if __name__ == "__main__":
    main()
