n = int(input("Quantos números você vai digitar? "))
numero = [0 for x in range(n)]

for i in range(0, n):
    numero[i] = int(input("Digite um número: "))

# Descobrindo a quantidade de números pares, e quais são eles
numeros_pares = 0
print("NÚMEROS PARES = ")
for i in range(0, n):
    if numero[i] % 2 == 0:
        numeros_pares += 1
        print(numero[i])

print(f"Quantidade de números pares = {numeros_pares}")
