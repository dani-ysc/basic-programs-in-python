#Programa em que, dados os números x e y digitados, fornece a soma, a multiplicação, exponenciação e a divisão entre eles

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
soma = x + y
multiplicacao = x * y
exponencial = x ** y
divisao = x / y

print(f"A soma de x e y é: {soma}")
print(f"A multiplicação entre x e y é: {multiplicacao}")
print(f"O valor de x elevado a y é: {exponencial}")
print(f"A divisão entre x e y é: {divisao}")