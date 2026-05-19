LIMITE_IMPOSTO = 1200.0

def ler_salario() -> float:
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            break
        except ValueError:
            print("Entrada inválida. Utilize somente números")
    
    return salario

def verificar_imposto(salario: float) -> bool:
    return salario > LIMITE_IMPOSTO

def main() -> None:
    salario = ler_salario()
    if verificar_imposto(salario):
        print(f"Seu salário de R$ {salario:.2f} ultrapassa R$ {LIMITE_IMPOSTO:.2f}, então você deve pagar imposto")
    else:
        print(f"Seu salário é menor ou igual a R$ {LIMITE_IMPOSTO:.2f}, então não precisa pagar imposto")

if __name__ == "__main__":
    main()