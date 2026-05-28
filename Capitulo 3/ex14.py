def validar_valores(grandeza):
    while True:
        try:
            valor = float(input(f"Digite a quantidade de {grandeza}: "))
            if valor < 0:
                print(f"Não são permitidos valores negativo para esse campo. Tente novamente")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def calcular_preco(dias, km):
    return (60 * dias) + (0.15 * km)

def main():
    dias = validar_valores("dias de aluguel para o carro")
    km = validar_valores("km percorridos")
    total_a_pagar = calcular_preco(dias, km)

    print(f"Total a pagar: R$ {total_a_pagar:.2f}")

if __name__ == "__main__":
    main()