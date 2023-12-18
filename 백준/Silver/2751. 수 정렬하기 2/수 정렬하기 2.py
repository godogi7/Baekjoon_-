import sys

N = int(input())

order = []
for _ in range(N):
    num = int(sys.stdin.readline())
    order.append(num)
order.sort()

for n in order:
  print(n)