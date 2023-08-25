
N, M = map(int, input().split())
basket =[i+1 for i in range(N)]
for j in range(M):
  x,y=map(int,input().split())
  first =basket[x-1]
  second=basket[y-1]
  basket[y-1] = first
  basket[x-1] = second
print(*basket)
  
 