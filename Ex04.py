dias = int(input("Digite a quantidade de dias: "))
distancia = int(input("Digite a quantidade de km percorridos: "))
if distancia > 100:
  print(f"Vai ter que pagar: R${dias*90+(distancia-100)*12}")
else:
  print(f"Vai ter que pagar: R${dias*90}")
