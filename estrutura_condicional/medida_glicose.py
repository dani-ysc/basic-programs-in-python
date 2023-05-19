# Um programa que lê a quantidade de glicose no sangue de uma pessoa e depois mostra na tela a classificação de acordo com a tabela de referência abaixo
# Normal -> até 100mg/dl; Elevado -> Maior que 100mg/dl até 140mg/dl; Diabetes -> Maior que 140mg/dl;

glicose = float(input("Digite a medida da glicose: "))

if glicose <= 100:
    print("Classificação: normal")
elif 100 < glicose <= 140:
    print("Classificação: elevado")
elif glicose > 140:
    print("Classificação: diabetes")
