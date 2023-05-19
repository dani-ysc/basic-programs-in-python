# Programa que lê o nome do funcionário, o valor recebido por hora e horas trabalhadas. Ao final, é exposto o pagamento do funcinário naquele determinado mês

n = int(input("Será realizado o pagamento de quantos funcionários? "))
nomes = [0 for x in range(n)]
pagamento_hora = [0 for x in range(n)]
horas_trabalhadas = [0 for x in range(n)]


for i in range(0, n):
    nomes = input("Nome: ")
    pagamento_hora = float(input("Valor por hora: R$"))
    horas_trabalhadas = int(input("Horas trabalhadas: "))
    pagamento_mes = pagamento_hora * horas_trabalhadas
    print(f"O pagamento para {nomes} deve ser R${pagamento_mes:.2f}")
