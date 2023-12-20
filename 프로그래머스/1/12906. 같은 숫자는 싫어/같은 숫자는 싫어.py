
def solution(arr):
    # 초기값 설정
    answer = [arr[0]]
    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

#넣으려는 값이 가장 끝 값과 다르면 푸시