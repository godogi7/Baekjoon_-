# 우선 소모 피로도가 작은 순으로 정렬해서 뽑아보자
# 각 피로도 쌍을 하나의 인자로 놓고, 모든 경우의 수를 테스트 해보는 것처럼
# 그래프 노드로 생각 후, 큐에 추가
import itertools

from collections import deque
def solution(k, dungeons):
    lists = list(itertools.permutations(dungeons,len(dungeons)))
    dungeon_count = []
    for case in lists:
        # 각 케이스별로 총 몇 개의 던전 갈 수 있는지 확인해야 하므로. total_fatigues여기에 추가
        total_fatigues = k
        count = 0
        #print(f"case = {case}")
        for fatigues in case:
            if fatigues[0] <= total_fatigues and fatigues[1] <= total_fatigues:
                total_fatigues -= fatigues[1]
                count += 1
            #print(f"total_fatigues = {total_fatigues}")
        dungeon_count.append(count)
    return(max(dungeon_count))
    #queue = deque()
    #for fatigues in dungeons:
        
    
    #dungeons.sort(key=lambda x:x[1])
    #for fatigues in dungeons:
    #    queue.append(fatigues[1])
    #print(dungeons)
    answer = -1
    return answer