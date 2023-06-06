n = int(input("Quantos números serão digitados? "))
numero = [0 for x in range(n)]

for i in range(0, n):
    numero[i] = float(input("Digite um número: "))

print("\n")
# Descobrindo qual o número que possui o maior valor, e qual a sua posição
maior_valor = 0
posicao = 0
for i in range(0, n):
    if numero[i] > maior_valor:
        maior_valor = numero[i]
        posicao = i

print(f"O maior valor digitado foi: {maior_valor}")
print(f"A posição do maior valor é: {posicao}")
