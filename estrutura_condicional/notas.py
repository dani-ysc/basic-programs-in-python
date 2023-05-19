# Um programa que lê as notas que os alunos obtiveram no primeiro e segundo semestres de uma disciplina anual. Em seguida mostrar a média das notas do aluno.
# Caso a nota final do aluno seja inferior a 6.0, mostrar a mensagem "Reprovado!"

n = int(input("Quantos alunos fazem parte da disciplina? "))
nome = [0 for x in range(n)]
nota1 = [0 for x in range(n)]
nota2 = [0 for x in range(n)]

for i in range(0, n):
    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota_final = (nota1 + nota2) / 2

    if nota_final < 6.0:
        print(f"A nota final de {nome} foi {nota_final}. Infelizmente, você foi reprovado")
    else:
        print(f"A nota final de {nome} foi {nota_final}. Meus parabéns, você foi aprovado!")
    
