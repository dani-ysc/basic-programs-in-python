# Leia um valor inteiro n. Este valor será a quantidade de números inteiros que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem dizendo se este valor lido é par ou ímpar, e também se é positivo ou negativo.
# Caso o valor ser igual a zero (0), o programa deverá imprimir apenas NULO.

n = int(input("Quantos números você vai digitar? "))

for i in range(0, n):
    x = int(input("Digite um número: "))
    if x == 0:
        print("NULO")
    elif x % 2 == 0 and x < 0:
        print("PAR NEGATIVO")
    elif x % 2 == 0 and x > 0:
        print("PAR POSITIVO")
    elif x % 2 == 1 and x < 0:
        print("ÍMPAR NEGATIVO")
    elif x % 2 == 1 and x > 0:
        print("ÍMPAR POSITIVO")
