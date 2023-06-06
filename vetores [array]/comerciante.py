n = int(input("Serão digitados quantos produtos? "))
nome_produto = [0 for x in range(n)]
preco_compra = [0 for x in range(n)]
preco_venda = [0 for x in range(n)]
porcentagem_lucro = [0 for x in range(n)]

# Coletando os dados acerca dos produtos
for i in range(n):
    print(f"Produto {i+1}: ")
    nome_produto[i] = input("Nome: ")
    preco_compra[i] = float(input("Preço de compra: R$"))
    preco_venda[i] = float(input("Preço de venda: R$"))
    porcentagem_lucro[i] = ((preco_venda[i] / preco_compra[i]) - 1.0) * 100
    print(f"A margem de lucro deste produto foi de: {porcentagem_lucro[i]:.2f}%")

# Categorizando a margem de lucro dos produtos vendidos pelo comerciante
lucro_abaixo_de_10 = 0
lucro_entre_10e20 = 0
lucro_acima_de_20 = 0

for i in range(n):
    if porcentagem_lucro[i] < 10.00:
        lucro_abaixo_de_10 += 1
    elif 10.00 <= porcentagem_lucro[i] <= 20.00:
        lucro_entre_10e20 += 1
    else:
        lucro_acima_de_20 += 1

# Calculando o lucro bruto do comerciante
total_compra = 0
total_venda = 0

for i in range(n):
    total_compra += preco_compra[i]
    total_venda += preco_venda[i]

lucro_total = total_venda - total_compra

# Construindo um relatório dos produtos vendidos pelo comerciante
print("RELATÓRIO: ")
print(f"Lucro abaixo de 10%: {lucro_abaixo_de_10}")
print(f"Lucro entre 10% e 20%: {lucro_entre_10e20}")
print(f"Lucro acima de 20%: {lucro_acima_de_20}")
print(f"Valor total de compra: R${total_compra:.2f}")
print(f"Valor total de venda: R${total_venda:.2f}")
print(f"Lucro total: R${lucro_total:.2f}")
