
NN, M = map(int, input().split())
basket =[0]*NN
for n in range(M):
  i,j,k = map(int,input().split())
  for x in range(i,j+1):
    basket[x-1]=k
print(*basket)
