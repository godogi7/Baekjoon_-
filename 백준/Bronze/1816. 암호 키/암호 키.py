n = int(input())

for _ in range(n):
    number = int(input())
    for i in range(2, 1_000_001): # 2이상 100만 이하의 모든 수에 대해
        if  number % i == 0: # 나머지가 0이라면, 즉 100만 이하의 소인수라면 No 출력하고 멈추기
            print("NO")
            break
        if i == 1000000:
            print("YES")
