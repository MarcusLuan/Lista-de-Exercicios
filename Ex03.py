valor =  int(input("Valor total da mercadoria? "))
if valor > 500:
  print(f"Receita federal taxou, agora ta em: R${(valor*1.5)}")
else:
  print("Pode passar sem problema -_-")
