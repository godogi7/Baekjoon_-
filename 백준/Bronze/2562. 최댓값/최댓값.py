list = []
for i in range(9):
  num = int(input())
  list.append(num)

for j in range(9):
  if list[j] == max(list):
    where = j+1
print(max(list))
print(where)