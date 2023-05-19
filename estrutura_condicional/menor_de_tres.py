# Programa que lê 3 números inteiros. Em seguida, mostra o menor número dentre os três

x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = int(input("Terceiro valor: "))

if x < y and x < z:
    print(f"MENOR = {x}")
elif y < z and y < x:
    print(f"MENOR = {y}")
else:
    print(f"MENOR = {z}")
