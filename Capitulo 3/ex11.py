def solicitar_valores(tipo: float) -> float:
    while True:
        try:
            valor = float(input(f"Digite o valor do {tipo}: "))
            if valor < 0:
                print(f"Esse valor não é permitido para um {tipo}. Tente novamente")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Utilize somente números")

def calcular_pagamento(preco_produto: float, percentual_desconto: float) -> float:
    valor_desconto = preco_produto * (percentual_desconto / 100)
    preco_final = preco_produto - valor_desconto

    return valor_desconto, preco_final

def main():
    preco_produto = solicitar_valores("produto")
    percentual_desconto = solicitar_valores("desconto")
    valor_desconto, preco_final = calcular_pagamento(preco_produto, percentual_desconto)
    
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Valor do produto com desconto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()