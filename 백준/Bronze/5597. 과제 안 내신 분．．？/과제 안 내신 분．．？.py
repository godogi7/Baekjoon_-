
number = set([])
for i in range(28):
  number.add(int(input()))
total = set([])
for j in range(30):
  total.add(j+1)
res = list(total-number)
res.sort()
print(res[0])
print(res[1])
