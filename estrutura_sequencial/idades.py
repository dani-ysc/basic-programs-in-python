#Programa em que os dados das pessoas (como nome e idade) ficam salvos num array. E, ao final, é exposto a idade média dos indivíduos.

n = int(input("Você irá colocar os dados de quantas pessoas? "))
nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]
soma_idades = 0

for i in range(0, n):
    print(f"Dados da {i+1} pessoa: ")
    nomes = input("Nome: ")
    idades = int(input("Idade: "))
    soma_idades += idades

idade_media = soma_idades / n
print(f"A idade média das {n} pessoas é de {idade_media} anos")