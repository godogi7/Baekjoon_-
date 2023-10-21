def solution(common):
    # 등차수열이면
    if sub(common, 2) == sub(common,1):
        last = common[-1]+sub(common, 1)
    # 등비수열이면
    else: 
        last = common[-1]*(common[-1]/common[-2])
    return last

# 두 항의 차 리턴
def sub(list, pos):
    return list[pos] - list[pos-1]
    