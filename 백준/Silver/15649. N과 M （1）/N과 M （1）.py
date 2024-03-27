def combinations(n, m, selected_numbers):
    if len(selected_numbers) == m:
        print(' '.join(map(str, selected_numbers)))
        return
    
    # 선택할 수 있는 모든 숫자에 대해 반복
    for i in range(1, n + 1):
        # 이미 들어간 건 넘어가고
        if i in selected_numbers:
            continue
        # 현재 숫자를 선택하고 다시 반복
        combinations(n, m, selected_numbers + [i])

N, M = map(int, input().split())
combinations(N, M, [])
