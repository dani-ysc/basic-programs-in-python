#Programa que lê a distância (em km) percorrida por um carro, a quantidade total de combustível gasto. Ao final, mostrar o consumo médio daquele veículo naquele percurso

distancia = int(input("Distância percorrida: "))
combustivel_total = float(input("Combustível gasto: "))
consumo_medio = distancia / combustivel_total

print(f"O consumo médio de combustível neste carro, numa viagem de {distancia}km foi de: {consumo_medio:.3f}km/l")
