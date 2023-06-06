# Ler um número inteiro x e mostrar na tela a tabuada de x de 1 até o número n escolhido
x = int(input("Deseja a tabuada para qual valor? "))
n = int(input("Deseja que x seja multiplicado até que número? "))

for i in range (0, n):
    resultado = x * (i+1)
    print(f"{x} x {i+1} = {resultado}")