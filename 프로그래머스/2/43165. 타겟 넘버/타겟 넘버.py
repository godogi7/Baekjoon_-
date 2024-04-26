from collections import deque

def solution(numbers, target):
    # 현재 큐와 다음 단계 큐 두개로 진행
    current = deque([0])
    for i in range(len(numbers)):
        next = deque()
        while current:
            current_sum = current.popleft()
            next.append(current_sum + numbers[i])
            next.append(current_sum - numbers[i])
        current = next
    #print(f"current = {current}")
    return current.count(target)