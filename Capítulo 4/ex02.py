def validar_velocidade():
    while True:
        try:
            km = float(input("Digite o valor da velocidade em km/h: "))
            if km < 0:
                print("Não é permitido valores negativos para essa grandeza")
                continue
            return km
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def verificar_velocidade(velocidade: float):
    if velocidade < 80:
        return "Você está dentro do limite de velocidade"
    
    velocidade_ultrapassada = velocidade - 80
    valor_a_pagar = velocidade_ultrapassada * 5
    return f"Você ultrapassou a velocidade permitida e deverá pagar R$ {valor_a_pagar:.2f} de multa."
        
def main():
    velocidade = validar_velocidade()
    mensagem = verificar_velocidade(velocidade)
    print(mensagem)

if __name__ == "__main__":
    main()