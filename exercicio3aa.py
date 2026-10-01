def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

        return resultado

def divisao(primeiro, segundo):
    return primeiro / segundo

def main():
    n = int(input("Digite um numero inteiro não negativo: "))

    if n < 0:
        print("N deve ser um número inteiro não negativo.")
        return

    soma = 1

    for i in range(1, n + 1):
        denominador = fatorial(i)
        parcela = divisao(1, denominador)
        soma += parcela

    print(f"O resultado da soma é: {soma}")

if __name__ == "__main__":
    main()