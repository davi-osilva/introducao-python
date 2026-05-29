def ler_valores(ordem):
    while True:
        try:
            return int(input(f"Digite o {ordem} número: "))
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def verificar_maior_e_menor(n1, n2, n3):
    maior_numero = max(n1, n2, n3)
    menor_numero = min(n1, n2, n3)

    return maior_numero, menor_numero

def main():
    n1 = ler_valores("primeiro")
    n2 = ler_valores("segundo")
    n3 = ler_valores("terceiro")
    maior_numero, menor_numero = verificar_maior_e_menor(n1, n2, n3)

    print(f"Maior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")

if __name__ == "__main__":
    main()