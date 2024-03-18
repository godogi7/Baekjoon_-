def solution(clothes):
    cloth_dict = {}
    for cloth in clothes:
        # 옷의 종류를 키로 사용하여, 같은 종류의 옷을 리스트로 모읍니다.
        # cloth[1]은 옷의 종류
        if cloth[1] not in cloth_dict:
            cloth_dict[cloth[1]]=1
        else:
            cloth_dict[cloth[1]] +=1
    answer = 1

    for key,value in cloth_dict.items():
        print(value)
        answer *=(value+1)
        
    return answer-1
# 각 (value별 개수 +1) * 다음 value

# 하나의 키 -> 케이스 추가
# value별로 하나씩만 선택
# 