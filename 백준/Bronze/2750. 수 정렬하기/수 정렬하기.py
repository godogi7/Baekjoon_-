n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())
a.sort()
for i in range(n):
  print(a[i])