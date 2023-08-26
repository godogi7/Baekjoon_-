N = int(input())
a =input().split()
a = list(map(int,a))
M = max(a)
sum = 0
for i in range(N):
  sum+=a[i]/M*100
print(sum/N)