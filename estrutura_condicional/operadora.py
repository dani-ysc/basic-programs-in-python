# Um programa que lê a quantidade de minutos consumidos num plano telefônico em que o plano básico dá direito a 100 minutos por R$50
# Cada minuto que excede os 100 iniciais custa R$2

qtd_minutos = int(input("Digite a quantidade de minutos: "))

if qtd_minutos > 100:
    minutos_excedidos = qtd_minutos - 100
    valor_a_pagar = 50 + minutos_excedidos * 2
    print(f"Valor a pagar: R${valor_a_pagar:.2f}")
else:
    print("Valor a pagar: R$50.00")
