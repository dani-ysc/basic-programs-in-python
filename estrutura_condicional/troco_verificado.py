# Programa que calcula o troco no processo de pagamento de um produto numa mercearia. O programa deve mostrar o valor do troco a ser devolvido ao cliente.
# Se o dinheiro dado não for suficiente, mostrar uma mensagem informando o valor restante.

preco_unitario = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))
valor_compra = preco_unitario * quantidade
troco = dinheiro_recebido - valor_compra

if valor_compra > dinheiro_recebido:
    print(f"Dinheiro insuficiente. Faltam R${-troco:.2f}")
else: 
    print(f"Troco = R${troco:.2f}")
