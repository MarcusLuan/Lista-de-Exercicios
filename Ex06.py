num = 1
while num < 100:
  num += 1
  cont = 0
  for i in range(2, int(num/2)+1):
      if num % i == 0:
          cont += 1
  if cont == 0:
      print(num)
