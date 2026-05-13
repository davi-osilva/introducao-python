soma = 0

for i in range(1, 4):
    while True:
        try:
            valor = int(input(f"Digite o número {i}: "))
            soma += valor
            break
        except ValueError:
            print("Entrada inválida. Utilize somente números")

print(f"A soma dos valores é igual a {soma}")