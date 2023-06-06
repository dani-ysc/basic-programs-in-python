n = int(input("Quantas pessoas serão digitadas? "))
nome = [0 for x in range(n)]
idade = [0 for x in range(n)]
altura = [0 for x in range(n)]

# Salvando as informações das pessoas que serão digitadas 
for i in range(0, n):
    print(f"Dados da {i+1}ª pessoa: ")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

# Descobrindo a média de altura das pessoas digitadas
altura_total = 0
for i in range(0, n):
    altura_total += altura[i]

print("\n")
altura_media = altura_total / n
print(f"Altura média: {altura_media:.2f}")

# Verificando a porcentagem de pessoas com menos de 16 anos
pessoas_menos16 = 0
for i in range(0, n):
    if idade[i] < 16:
        pessoas_menos16 += 1

porcentagem_menos16 = (pessoas_menos16 / n) * 100
print(f"Pessoas com menos de 16 anos: {porcentagem_menos16:.1f}%")

# Mostrando o nome das pessoas com menos de 16 anos
for i in range(0, n):
    if idade[i] < 16:
        print(nome[i])
