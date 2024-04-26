target = list(map(int,input().split()))

def solution(target):
  E = 1
  S = 1
  M = 1
  date_list = []
  count = 1 
  while True:
    date_list = [E,S,M]
    if date_list == target:  
      return count
    E += 1
    S += 1
    M += 1
    count += 1
    if E == 16:
      E = 1
    if S == 29:
      S = 1
    if M == 20:
      M = 1
    #print(date_list)

#print(target)
print(solution(target))