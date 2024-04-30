#처음 내 풀이
def solution(brown, yellow):
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            a = i
            b = yellow//a
            #print(a,b)
            if (a+2)*(b+2) == brown+yellow:
                return([max(a+2, b+2), min(a+2,b+2)])

"""
a*b = brown + yellow
a+b = (brown+4)//2
if a <= b : a는 1~ (a+b)//2 의 값을 가짐
"""
"""
def solution(brown, yellow):
  m = brown + yellow
  s = (brown + 4)//2

  diff = (s // 2)
  a = diff // 2
  b = s - a
  diff //= 2

  while a * b != m:
    if diff != 1:
      diff //= 2

    if a * b > m:
      a -= diff
      b += diff

    else: 
      a += diff
      b -= diff

  return [a,b]
  """