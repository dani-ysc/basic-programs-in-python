# Um posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. 
# Este programa irá ler o tipo de combustível abastecido (1.Álcool 2.Gasolina 3.Diesel 4. Fim). Caso o usuário informe um código inválido (fora da faixa [1,4]) deve ser informado para solicitar um novo código
# O programa será encerrado quando o código informado for o número 4, mostrando a mensagem "Muito obrigado!", bem como as quantidades de cada combustível

combustivel = int(input("Informe um código (1, 2, 3) ou 4 para parar o programa: "))
alcool = 0
gasolina = 0
diesel = 0

while combustivel != 4:
    if combustivel == 1:
        alcool += 1
    elif combustivel == 2:
        gasolina += 1
    elif combustivel == 3:
        diesel += 1
    combustivel = int(input("Informe um código (1, 2, 3) ou 4 para parar o programa: "))

print("Muito obrigado!")
print(f"Álcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")

