# Um programa que lê as notas referentes às duas avaliações de um aluno. O programa calcula, e imprime a média semestral
# O programa só aceitará notas válidas (notas que pertencem ao intervalo [0,10]). Cada nota deve ser validada separadamente.

nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10.0:
    nota1 = float(input("Valor inválido! Tente novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10.0:
    nota2 = float(input("Valor inválido! Tente novamente: "))

media = (nota1 + nota2) / 2
print(f"MÉDIA = {media:.2f}")
