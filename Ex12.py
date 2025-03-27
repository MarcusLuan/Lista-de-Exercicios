turmas = int(input("Digite a quantidade de turmas: "))
alunos = int(input("Digite a quantidade de alunos total na escola: "))
if alunos // turmas >= 40:
  print(f"Tem {alunos // turmas} em media a mais de 40 em cada turma")
else:
  print(f"{alunos // turmas}, Não tem turma com mais de 40 alunos")
