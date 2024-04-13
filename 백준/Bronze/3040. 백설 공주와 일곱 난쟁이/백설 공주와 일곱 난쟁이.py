def math_genius(dwarves):
  diff = sum(dwarves)-100
  for i in range(len(dwarves)): # 0,1,2,3,4,5,6,7,8
    for j in range(i+1,len(dwarves)): # 1,2,3,4,5,6,7,8 
      if diff == dwarves[i]+dwarves[j]:
        del dwarves[j]
        del dwarves[i]
        return dwarves

dwarves = []
for _ in range(9):
  dwarves.append(int(input()))


for dwarf in math_genius(dwarves):
  print(dwarf)
  