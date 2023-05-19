largura_terreno = float(input("Digite a largura do terreno: "))
comprimento_terreno = float(input("Digite o comprimento do terreno: "))
metro_quadrado = float(input("Digite o valor do metro quadrado: "))

area = largura_terreno * comprimento_terreno
preco = metro_quadrado * area

print(f"Área do terreno = {area:.2f}")
print(f"Preço do terreno = {preco:.2f}")
