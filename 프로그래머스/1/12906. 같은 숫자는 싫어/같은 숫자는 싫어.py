"""
def solution(arr):
    # 초기값 설정
    answer = [arr[0]]
    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer
"""
# 넣으려는 값이 가장 끝 값과 다르면 푸시
"""
1. 스
"""
def solution(arr):
    answer = []
    # 스택[0] = 배열[0]
    # answer[0] = arr[0]
    # i > 0,1,2,3,4
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if answer[-1] != arr[i]:
                answer.append(arr[i])
            else:
                pass
    
    return answer

















