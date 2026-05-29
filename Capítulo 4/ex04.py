def validar_salario():
    while True:
        try:
            salario = float(input("Digite o seu salário: "))
            if salario < 0:
                print("Não é permitido valor negativo para salários. Tente novamente")
                continue
            return salario
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def calcular_aumento(salario):
    if salario > 1250:
        aumento = salario * 10 / 100
    else:
        aumento = salario * 15 / 100

    novo_salario = aumento + salario
    return aumento, novo_salario

def main():
    salario = validar_salario()
    aumento, novo_salario = calcular_aumento(salario)

    print(f"O aumento foi de R$ {aumento:.2f}, então o novo salário será de R$ {novo_salario:.2f}")

if __name__ == "__main__":
    main()