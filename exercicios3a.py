def fatorial(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado

def main():
    numero = int(input("Digite um Numero inteiro não negativo:"))

    if numero <0:
        print("não existe fatorial de número negativo")
        return

    resultado= fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")

if __name__=="__main__":
    main()
