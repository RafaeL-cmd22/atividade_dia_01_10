def calcular_rendimento(opcao_investimento: int, capital_inicial: float) -> None:
    
    valor_corrigido = capital_inicial
    
    if opcao_investimento == 1:
        valor_corrigido = capital_inicial * 1.03  # Poupança = +3%
        print(f"Valor corrigido em 30 dias (Poupança): R$ {valor_corrigido:.2f}")
    elif opcao_investimento == 2:
        valor_corrigido = capital_inicial * 1.05  # Renda Fixa = +5%
        print(f"Valor corrigido em 30 dias (Renda Fixa): R$ {valor_corrigido:.2f}")
    else:
        print("Erro: Tipo de investimento inválido. Demais tipos não serão considerados.")

def main():
    
    print("Selecione o tipo de investimento:")
    print("1 = Poupança")
    print("2 = Renda Fixa")
    tipo = int(input("Opção: "))
    valor = float(input("Digite o valor a ser investido: R$ "))
    
    
    calcular_rendimento(tipo, valor)

if _name_ == "_main_":
    main()