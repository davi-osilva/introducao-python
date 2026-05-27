def validar_valores(grandeza: float) -> float:
    while True:
        try:
            valor = float(input(f"Digite o valor da {grandeza} da sua viagem: "))
            if valor < 0:
                print("Não é permitido valores negativos para essa grandeza")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def calcular_tempo_viagem(velocidade_media: float, distancia: float) -> float:
    return distancia / velocidade_media

def main():
    velocidade_media = validar_valores("velocidade média em km/h")
    distancia = validar_valores("distância em km")
    tempo_em_horas = (calcular_tempo_viagem(velocidade_media, distancia))
    tempo_em_minutos = tempo_em_horas * 60

    print(f"O tempo da viagem será de {tempo_em_horas:.2f} hora(s), que é igual a {tempo_em_minutos:.2f} minuto(s)")

if __name__ == "__main__":
    main()