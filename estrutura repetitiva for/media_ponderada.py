# Leia um valor inteiro n, que reprensenta o números de casos realizados. Cada caso consiste em 3 valores reais, para os quais você deverá calcular e mostrar a média ponderada.
# O primeiro valor possui o peso 2; o segundo possui o peso 3 e o terceiro valor possui o peso 5. 

n = int(input("Quantos casos serão digitados? "))

for i in range(0, n):
    print("Digite três números: ")
    x = float(input())
    y = float(input())
    z = float(input())
    media_ponderada = ((x * 2) + (y * 3) + (z * 5)) / 10
    print(f"A média ponderada dos valores digitados é {media_ponderada:.1f}")