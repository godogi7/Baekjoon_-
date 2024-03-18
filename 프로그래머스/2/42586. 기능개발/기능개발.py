def solution(progresses, speeds):
    # progresses 빌 때까지 진행. 
    answer = []
    while progresses:
        # 첫 번째 인덱스 기준(100보다 작은 경우_배포 X)
        empty_list = []
        if progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        # 100 이상이면, progresses에서 제거하고, answer 보낼거에 추가 : 배포개수 세야 하니까
        
        if progresses[0] >= 100:
            while progresses and progresses[0] >= 100:
                empty_list.append(progresses.pop(0))
                speeds.pop(0)

            answer.append(len(empty_list))
    return answer
    
    
    
    
    """
    deploy = [0]*len(progresses)
    day = 0
    # 진도에서 하나씩 뺄거니까, 진도 개수가 0 되면 stop
    while len(progresses) > 0:
        day += 1
        for i in range(len(progresses)):
            progresses[i] = progresses[i]+speeds[i]*day
            # 진도 100이상이면, deploy 인덱스에 날짜만 추가
            if progresses[i] >= 100:
                deploy[i] += day
                print(f"before remove {progresses}")
                
            else:
                pass
            
                
    return answer
"""
# 배포시 몇 개의 기능 배포되는지 return
# 93 + 1*7, 30 + 30*3, 55 + 5*9
# 100 초과된거 확인시, array[0] 확인 -> 빼버리고
# 기능 구현 -> 추가
# 100, 100, 98, 100이라면 -> 100,100 만 한번에 배포됨

"""def solution(progresses, speeds):
    real_progresses = []
 """   

