# Leia um valor inteiro x. Em seguida mestre os ímpares de 1 até x, um valor por linha, inclusive o x, se for o caso.

x = int(input("Digite o valor de x: "))

for i in range (0, x+1):
    if i % 2 == 1:
        print(i)