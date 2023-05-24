# Um programa que lê uma quantidade indeterminada de dados, contendo a idade de um indivíduo. O programa parará de rodar a partir do momento que for colocado um número negativo.
# Ao final, calcular a idade média do grupo de indivíduos, desconsiderando a idade negativa que finalizou o programa. Caso um número negativo for colocado ao iniciar o programa, apresentar a mensagem "IMPOSSÍVEL CALCULAR!"

print("Digite as idades: ")
idade = int(input())

if idade < 0:
    print("IMPOSSÍVEL CALCULAR!")
else:
    soma_idades = 0
    n = 0
    while idade >= 0:
        soma_idades += idade
        n += 1
        idade = int(input())
        
    media_idades = soma_idades / n
    print(f"MÉDIA = {media_idades:.2f}")