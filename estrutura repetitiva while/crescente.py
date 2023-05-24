# Um programa que lê uma quantidaed indeterminada de valores X e Y e escreve uma mensagem para cada dupla informando se esses valores foram digitados em ordem crescente ou decrescente.
# O programa finalizará quando forem digitados dois valores iguais

print("Digite dois números: ")
x = int(input())
y = int(input())

while x != y:
    if x > y:
        print("DECRESCENTE!")
    elif x < y:
        print("CRESCENTE!")
    print("Digite outros dois números: ")
    x = int(input())
    y = int(input())
