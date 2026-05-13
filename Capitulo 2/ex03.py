while True:
    nome = input("Digite seu nome: ").strip()
    if not nome.replace(" ", "").isalpha():
        print("Entrada inválida. Utilize somente letras")
        continue
    print(f"Olá, {nome}. Como vai?")
    break
    