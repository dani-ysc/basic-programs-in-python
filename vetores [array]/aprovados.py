n = int(input("Quantos alunos serão digitados: "))
nome = [0 for x in range(n)]
nota1 = [0 for x in range(n)]
nota2 = [0 for x in range(n)]
nota_final = [0 for x in range(n)]

# Coletar as informações acerca das notas dos alunos
for i in range(0, n):
    print(f"Digite o nome, a primeira e a segunda nota do {i+1}o aluno: ")
    nome[i] = input("Nome: ")
    nota1[i] = float(input("Nota 1: "))
    nota2[i] = float(input("Nota 2: "))
    nota_final[i] = (nota1[i] + nota2[i]) / 2
    print("\n")

# Verificar quais alunos foram aprovados
quantidade_aprovados = 0
print(f"Alunos aprovados: ")
for i in range(0, n):
    if nota_final[i] >= 6.0:
        quantidade_aprovados += 1
        print(nome[i])

# Mensagem final com mostrando a quantidade de alunos aprovados
if n == 1 and quantidade_aprovados == 0:
    print("O único aluno que frequenta a disciplina foi reprovado!")
elif n == 1 and quantidade_aprovados != 0:
    print("O único aluno que frequenta a disciplina foi aprovado!")
else:
    print(f"Dos {n} alunos que frequentam a disciplina, {quantidade_aprovados} foram aprovados.")
