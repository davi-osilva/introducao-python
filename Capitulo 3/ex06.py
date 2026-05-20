def ler_medias() -> list[float]:
    lista_medias = []

    for i in range(1, 4):
        while True:
            try:
                media = float(input(f"Digite sua média {i}: "))
                if media < 0 or media > 10:
                    print("As médias vão de 0 à 10. Tente novamente")
                    continue
                lista_medias.append(media)
                break
            except ValueError:
                print("Entrada inválida. Utilize somente números")

    return lista_medias

def verificar_aprovacao(lista_medias: list[float]) -> bool:
    return all(media >= 7 for media in lista_medias)

def main() -> None:
    medias = ler_medias()
    mensagem = "Aprovado" if verificar_aprovacao(medias) else "Reprovado"
    print(mensagem)

if __name__ == "__main__":
    main()