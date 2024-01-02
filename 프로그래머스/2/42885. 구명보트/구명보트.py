def solution(people, limit):
  people.sort()
  count = 0
  left, right = 0, len(people)-1
  for _ in range(len(people)):
    if left <= right :
      if people[left] + people[right]<= limit:
        left +=1 
      right -=1
      count +=1

  return count



# 50,70,80 아 같아지는 경우 있네