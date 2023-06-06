n = int(input("Quantas pessoas serão digitadas? "))
altura = [0 for x in range(n)]
genero = [0 for x in range(n)]

# Guardando os dados das pessoas nos arrays
for i in range(n):
    altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
    genero[i] = input(f"Gênero da {i+1}a pessoa: ").upper()

# Descobrindo a menor altura das pessoas
menor_altura = altura[0]
for i in range(n):
    if altura[i] < menor_altura:
        menor_altura = altura[i]
print(f"A pessoa com a menor altura possui {menor_altura:.2f}m")

# Descobrindo a maior altura das pessoas
maior_altura = 0
for i in range(n):
    if altura[i] > maior_altura:
        maior_altura = altura[i]
print(f"A pessoa com a maior altura possui {maior_altura:.2f}m")

# Descobrindo a média de altura das mulheres
alturatotal_F = 0
n_mulheres = 0
for i in range(n):
    if genero[i] == 'F':
        alturatotal_F += altura[i]
        n_mulheres += 1

altura_mediaF = alturatotal_F / n_mulheres
print(f"A média de altura das mulheres é de {altura_mediaF:.2f}m")

# Quantidade de homens na amostra
n_homens = n - n_mulheres
print(f"A quantidade de homens na amostra é de {n_homens}")
