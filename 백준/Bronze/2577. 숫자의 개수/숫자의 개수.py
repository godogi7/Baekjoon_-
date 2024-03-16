a = int(input())
b =int(input())
c = int(input())
d = a*b*c
count_list = [0,0,0,0,0,0,0,0,0,0]
for i in str(d):
  count_list[int(i)] += 1
for j in count_list:
  print(j)