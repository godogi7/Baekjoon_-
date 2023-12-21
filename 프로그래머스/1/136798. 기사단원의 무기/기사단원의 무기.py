# 약수 개수 구하는 함수
def measure2(num):
  count = 0
  for i in range(1, int(num**0.5)+1):
    if (num%i ==0):
      count+=1
      if (i**2 != num):
        count+=1
  return count


def solution(number, limit, power):
  measure_count = []  # 약수의 개수 담는 리스트
  result = 0
  for i in range(0,number):
    measure_count.append(measure2(i+1))
    if measure_count[i] > limit:
      result += power
    else:
      result += measure_count[i]
  return result
