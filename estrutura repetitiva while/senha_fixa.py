# Um programa que repetirá a leitura de uma senha até que ela seja válida. Para cada leitura incorreta, apresentar a mensagem: "Senha Inválida! Tente novamente:".
# Quando a senha informada for a correta, apresentar a mensagem "Acesso permitido!" e o programa encerrado.
# A senha correta é o valor "2002"

senha_correta = 2002
senha = int(input("Digite a senha: "))

while senha != senha_correta:
    senha = int(input("Senha Inválida! Tente novamente: "))

print("Acesso permitido!")
