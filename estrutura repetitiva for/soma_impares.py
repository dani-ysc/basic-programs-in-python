# Leia dois valores inteiros x e y (em qualquer ordem). Em seguida, calcule e mostre a soma dos números impares entre eles.

print("Digite dois números: ")
x = int(input())
y = int(input())
soma = 0

if x > y:
    for i in range(y, x):
        if i % 2 == 1:
            soma += i
if y > x:
    for i in range(x, y):
        if i % 2 == 1:
            soma += i

print(f"SOMA DOS ÍMPARES = {soma}")