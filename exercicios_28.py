def processar_reajuste(preco_base: float, vendas_periodo: int) -> None:
   
    novo_valor = preco_base
    
    if vendas_periodo < 500 and preco_base < 30:
        novo_valor = preco_base * 1.10  # +10%
    elif (500 <= vendas_periodo < 1000) and (30 <= preco_base < 80):
        novo_valor = preco_base * 1.15  # +15%
    elif vendas_periodo >= 1000 and preco_base >= 80:
        novo_valor = preco_base * 0.95  # -5%
        
    print(f"O novo preço do produto é: R$ {novo_valor:.2f}")

def main():
    
    preco_atual = float(input("Digite o preço atual do produto: R$ "))
    venda_mensal = int(input("Digite a média de venda mensal: "))
    
    
    processar_reajuste(preco_atual, venda_mensal)

if _name_ == "_main_":
    main()