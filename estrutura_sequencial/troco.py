#Realizar um programa que calcule o troco no processo de pagamento de um produto numa mercearia.

preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))
troco = dinheiro_recebido - (preco * quantidade)

print(f"TROCO = R${troco:.2f}")
