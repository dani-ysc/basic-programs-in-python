# Leia um valor inteiro n. Este valor será a quantidade de números inteiros x que serão lidos em seguida.
# Moster quantos destes valores x estão dentro do intervalo [10, 20] e quantos estão fora do intervalo.

n = int(input("Quantos números você vai digitar? "))

dentro = 0
fora = 0
for i in range(0, n):
    x = int(input("Digite um número: "))
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1

print(f"Dentro = {dentro}\nFora = {fora}")