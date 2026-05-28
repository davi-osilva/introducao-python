def validar_valores(grandeza):
    while True:
        try:
            valor = int(input(f"Digite a quantidade de {grandeza}: "))
            if valor < 0:
                print("Não são permitidos valores negativos para esse campo. Tente novamente")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")
            
def calcular_valor(cigarros_por_dia, anos_fumando):
    cigarros_fumados_em_dias = cigarros_por_dia * (anos_fumando * 365)
    minutos_de_vida_perdidos = 10 * cigarros_fumados_em_dias
    minutos_para_dias = minutos_de_vida_perdidos * (1 / 1440)

    return minutos_para_dias

def main():
    cigarros_por_dia = validar_valores("cigarros fumados por dia")
    anos_fumando = validar_valores("anos fumando")
    dias_perdidos = calcular_valor(cigarros_por_dia, anos_fumando)

    print(f"Foram perdidos {dias_perdidos:.2f} dias de vida")

if __name__ == "__main__":
    main()
