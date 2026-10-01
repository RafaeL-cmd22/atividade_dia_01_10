import math
def ex18_diferenca():
    
    global num_a, num_b
    print("\n--- Exercício 18 ---")
    num_a = int(input("Digite o primeiro valor inteiro: "))
    num_b = int(input("Digite o segundo valor inteiro: "))
    
    if num_a > num_b:
        print(f"Diferença do maior pelo menor: {num_a - num_b}")
    else:
        print(f"Diferença do maior pelo menor: {num_b - num_a}")


def ex19_maior_real():
    
    global num_a, num_b
    print("\n--- Exercício 19 ---")
    num_a = float(input("Digite o primeiro valor real: "))
    num_b = float(input("Digite o segundo valor real: "))
    
    if num_a > num_b:
        print(f"O maior valor é: {num_a}")
    else:
        print(f"O maior valor é: {num_b}")


def ex20_equacao_segundo_grau():
   
    global coef_a, coef_b, coef_c
    print("\n--- Exercício 20 ---")
    coef_a = float(input("Digite o coeficiente A: "))
    coef_b = float(input("Digite o coeficiente B: "))
    coef_c = float(input("Digite o coeficiente C: "))
    
    if coef_a == 0:
        print("Não é uma equação do 2º grau (A não pode ser 0).")
        return
        
    delta = (coef_b ** 2) - (4 * coef_a * coef_c)
    
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta == 0:
        x = -coef_b / (2 * coef_a)
        print(f"Existe uma raiz real: X = {x:.2f}")
    else:
        x1 = (-coef_b + math.sqrt(delta)) / (2 * coef_a)
        x2 = (-coef_b - math.sqrt(delta)) / (2 * coef_a)
        print(f"Existem duas raízes reais: X1 = {x1:.2f} e X2 = {x2:.2f}")


def ex21_media_aluno():
    
    global nota1, nota2, nota3, nota4
    print("\n--- Exercício 21 ---")
    nota1 = float(input("Digite a nota do 1º bimestre: "))
    nota2 = float(input("Digite a nota do 2º bimestre: "))
    nota3 = float(input("Digite a nota do 3º bimestre: "))
    nota4 = float(input("Digite a nota do 4º bimestre: "))
    
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"Média calculada: {media:.2f}")
    
    if media >= 6.0:
        print("Status: APROVADO")
    elif media >= 3.0:
        print("Status: EXAME")
    else:
        print("Status: RETIDO")


def ex22_ordem_crescente_2():
    
    global num_a, num_b
    print("\n--- Exercício 22 ---")
    num_a = int(input("Digite o primeiro valor inteiro: "))
    num_b = int(input("Digite o segundo valor inteiro (diferente): "))
    
    if num_a < num_b:
        print(f"Ordem crescente: {num_a}, {num_b}")
    else:
        print(f"Ordem crescente: {num_b}, {num_a}")


def ex23_ordem_crescente_4():
    
    global v1, v2, v3, v4
    print("\n--- Exercício 23 ---")
    print("Digite 3 valores OBRIGATORIAMENTE em ordem crescente:")
    v1 = float(input("1º valor: "))
    v2 = float(input("2º valor: "))
    v3 = float(input("3º valor: "))
    v4 = float(input("Digite o 4º valor (qualquer ordem): "))
    
    if v4 >= v3:
        print(f"Ordem crescente: {v1}, {v2}, {v3}, {v4}")
    elif v4 >= v2:
        print(f"Ordem crescente: {v1}, {v2}, {v4}, {v3}")
    elif v4 >= v1:
        print(f"Ordem crescente: {v1}, {v4}, {v2}, {v3}")
    else:
        print(f"Ordem crescente: {v4}, {v1}, {v2}, {v3}")


def ex24_divisivel_2_3():
    
    global num_a
    print("\n--- Exercício 24 ---")
    num_a = int(input("Digite um valor inteiro: "))
    
    if num_a % 2 == 0 and num_a % 3 == 0:
        print(f"O número {num_a} É divisível por 2 e por 3.")
    else:
        print(f"O número {num_a} NÃO É divisível por 2 e por 3 simultaneamente.")


def ex25_duracao_jogo():
    
    global h_ini, m_ini, h_fim, m_fim
    print("\n--- Exercício 25 ---")
    h_ini = int(input("Hora de início (HH): "))
    m_ini = int(input("Minuto de início (MM): "))
    h_fim = int(input("Hora de término (HH): "))
    m_fim = int(input("Minuto de término (MM): "))
    
    
    minutos_inicio = (h_ini * 60) + m_ini
    minutos_fim = (h_fim * 60) + m_fim
    
    if minutos_fim >= minutos_inicio:
        duracao_total = minutos_fim - minutos_inicio
    else:
       
        duracao_total = (minutos_fim + (24 * 60)) - minutos_inicio
        
    horas_res = duracao_total // 60
    minutos_res = duracao_total % 60
    
    print(f"Duração do jogo: {horas_res} hora(s) e {minutos_res} minuto(s).")


def ex26_multiplo():
    
    global num_a, num_b
    print("\n--- Exercício 26 ---")
    num_a = int(input("Digite o primeiro número inteiro: "))
    num_b = int(input("Digite o segundo número inteiro: "))
    
    if num_a > num_b:
        maior, menor = num_a, num_b
    else:
        maior, menor = num_b, num_a
        
    if menor == 0:
        print("Não é possível dividir por zero para verificar o múltiplo.")
    elif maior % menor == 0:
        print(f"{maior} É múltiplo de {menor}.")
    else:
        print(f"{maior} NÃO É múltiplo de {menor}.")




def main():
    
    while True:
        print("\n================ MENU PRINCIPAL ================")
        print("18 - Diferença do maior pelo menor")
        print("19 - Maior de dois reais")
        print("20 - Equação do 2º grau")
        print("21 - Média aritmética de notas")
        print("22 - Dois valores em ordem crescente")
        print("23 - Três valores ordenados + um quarto")
        print("24 - Divisível por 2 e 3")
        print("25 - Duração de jogo (HH, MM)")
        print("26 - Maior é múltiplo do menor?")
        print("0  - Sair")
        print("================================================")
        
        opcao = input("Escolha o exercício que deseja rodar: ")
        
        if opcao == "18": ex18_diferenca()
        elif opcao == "19": ex19_maior_real()
        elif opcao == "20": ex20_equacao_segundo_grau()
        elif opcao == "21": ex21_media_aluno()
        elif opcao == "22": ex22_ordem_crescente_2()
        elif opcao == "23": ex23_ordem_crescente_4()
        elif opcao == "24": ex24_divisivel_2_3()
        elif opcao == "25": ex25_duracao_jogo()
        elif opcao == "26": ex26_multiplo()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Escolha um número de 18 a 26 ou 0.")

 
if __name__ == "__main__":
    main()