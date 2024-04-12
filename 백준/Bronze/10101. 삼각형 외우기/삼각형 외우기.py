list = []
for _ in range(3):
  list.append(int(input()))

if sum(list) == 180:
  if list[0]==list[1]==list[2]: print("Equilateral")
  elif list[0]==list[1] or list[0]==list[2] or list[1]==list[2]:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")