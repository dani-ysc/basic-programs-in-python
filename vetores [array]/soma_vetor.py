n = int(input("Quantos números serão digitados? "))
valor = [0 for x in range(n)]
soma = 0

for i in range(0, n):
    valor[i] = float(input("Digite um número: "))
    soma += valor[i]


for i in range(0, n):
    print(f"VALORES = {valor[i]}")

media = soma / n
print(f"SOMA = {soma:.2f}")
print(f"MÉDIA = {media:.2f}")