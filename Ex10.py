numero = int(input("Digite um numero maior que 1: "))
cont = 0
for i in range(2, int(numero/2)+1):
  if numero % i == 0:
    cont += 1
if cont == 0:
  print("É primo")
else:
  print("Não é primo")
