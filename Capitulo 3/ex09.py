def validar_valores(grandeza):
    while True:
        try:
            valor = int(input(f"Digite a quantidade de {grandeza}: "))
            if valor < 0:
                print("Não é permitido valores negativos para essa grandeza. Tente novamente")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Tente novamente utilizando somente números")

def converter_para_segundos(dias, horas, minutos, segundos):
    dias_em_segundos = dias * 86400
    horas_em_segundos = horas * 3600
    minutos_em_segundos = minutos * 60

    return dias_em_segundos + horas_em_segundos + minutos_em_segundos + segundos

def main():
    dias = validar_valores("dias")
    horas = validar_valores("horas")
    minutos = validar_valores("minutos")
    segundos = validar_valores("segundos")
    total_segundos = converter_para_segundos(dias, horas, minutos, segundos)

    print(f"Total de segundos: {total_segundos}")

if __name__ == "__main__":
    main()