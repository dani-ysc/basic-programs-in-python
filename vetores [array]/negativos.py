# Escrever um programa que leia um número inteiro positivo (N=10) e depois N números inteiros e armazene-os em um vetor.
# Em seguida, mostrar na tela os números negativos lidos, e a sua soma.

n = int(input("Quantos números você vai digitar? "))
numero = [0 for x in range(n)]

soma_negativos = 0
for i in range(0, n):
    numero[i] = int(input("Digite um número: "))
    if numero[i] < 0:
        soma_negativos += numero[i]

print("\n")
print("NÚMEROS NEGATIVOS: ")
for i in range(0, n):
    if numero[i] < 0:
        print(numero[i])

print("\n")
print(f"A soma dos números negativos é de {soma_negativos}")
