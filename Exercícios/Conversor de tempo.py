import time
start = time.time()

duracao_evento = int(input("Digite a duração do evento em segundos: "))

horas = duracao_evento // 3600
resto = duracao_evento % 3600
minutos = resto // 60
segundos = resto % 60

print("\nResultado:")
print(f"O evento durou: {horas:02d} horas, {minutos:02d} minutos e {segundos:02d} segundos.")

finish = time.time()

print(f"\nTempo de execução do script: {finish - start:.2f} segundos")
