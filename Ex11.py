usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
while senha == usuario:
  print("A senha não pode ser igual ao nome de usuário")
  senha = input("Digite sua senha")
