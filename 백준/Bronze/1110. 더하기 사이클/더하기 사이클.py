
def cycle_sum(N):
  original = N # 56
  cycle = 0
  while True:
    sum = N//10 + N%10 # 5+6 = 11
    new_sum = 10*(N%10) +sum%10 # 6*10 + 11%10 = 61
    N = new_sum
    #print(N)
    cycle +=1
    if N == original:
      break
  return cycle
N = int(input())
print(cycle_sum(N))