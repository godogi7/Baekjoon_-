N,M = map(int,input().split())
a = list(range(1,N+1,1))

for i in range(M):
  x,y = map(int,input().split())
  b =a[x-1:y]
  b.reverse()
  a[x-1:y] = b
print(*a)
