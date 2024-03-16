# 0~9 든 세트
# 6 <-> 9 대체 가능
# 방번호 N(0<N<1,000,000)
"""
Cases
숫자 다 같은경우 : 11111
숫자 다 다를경우 : 12345
숫자 n개 같을경우 : 12224
같은 숫자 판별법?
[0,1,2,3,4,5,6,7,8,9]
[0,0,0,0,0,0,0,0,0,0]에서 +1씩
ex) 94666
[0,0,0,0,1,0,3,0,0,1] ->필요개수 3
입력 string? , int?
6이랑 9호환성.
6만 2개 or 9만 2개일 때:
  6(9) cover 9(6)
"""
#N = 123245
#N2 = 99999
#N3 = 1996 -> 2셋트 필요
#N4 = 1999 -> 2셋트 필요
#9999 -> [10] = 4, [7] = 0
# 1개, 2개 -> 2개
# 2개, 2개 -> 2개
# 0개, 2개 -> 1개
# 3개, 1개 -> 2개

N = input()
num_count = [0,0,0,0,0,0,0,0,0,0]
for num in N:
  num_count[int(num)] += 1
#print(num_count)

sum = num_count[6]+num_count[9]
#print(f"sum={sum}")
# 6과 9가 짝수일경우 그대로 절반만 반환, 아니면 1 더한 값 반환
avg = sum//2 if sum%2 == 0 else sum//2+1
#print(sum//2, sum/2)
#print(avg)
num_count[6]=avg
num_count[9]=avg
#print(num_count)

print(max(num_count))