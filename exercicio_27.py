def calcular_velocidade_media(n_voltas: int, metros_circuito: float, minutos_total: float) -> None:
    
    distancia_km = (n_voltas * metros_circuito) / 1000
    tempo_horas = minutos_total / 60
    velocidade_final = distancia_km / tempo_horas
    
    print(f"A velocidade média foi de: {velocidade_final:.2f} km/h")

def main():
    
    voltas = int(input("Digite o número de voltas: "))
    extensao = float(input("Digite a extensão do circuito (em metros): "))
    tempo = float(input("Digite o tempo de duração (em minutos): "))
    
    
    calcular_velocidade_media(voltas, extensao, tempo)

if __name__ == "__main__":
    main()