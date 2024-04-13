def draw_star(n):
    if n == 1:
        return ["*"]
    
    # n//3 크기의 패턴을 먼저 구성
    stars = draw_star(n//3)
    result = []

    # 크기 n의 패턴을 만들기 위해 n//3 패턴을 확장
    for s in stars:
        result.append(s * 3)
    for s in stars:
        result.append(s + ' ' * (n//3) + s)
    for s in stars:
        result.append(s * 3)

    return result

# 사용자로부터 입력 받기
n = int(input())
output = draw_star(n)

# 결과 출력
for line in output:
    print(line)