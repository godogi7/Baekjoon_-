def solution(dartResult):
    a = list(dartResult)
    scores = []
    i = 0 
    while i < len(a): # 0,1,2,3,4,...len(a)
        if a[i].isdigit():
            if a[i] == '1' and i +1 < len(a) and a[i+1] == '0': # 10 처리
                score = 10
                i += 2
            else: 
                score = int(a[i])
                i += 1 # 숫자 넣었으면, 그 다음 인덱스로 넘어감, 10은 어케 처리하지? 우선 한 자리 숫자들 해결

        if i < len(a) and (a[i] == 'S' or a[i] == 'D' or a[i] == 'T'):
            if a[i] == 'D':
                score **= 2
            elif a[i] == 'T':
                score **= 3

        i+=1            
        if i < len(a):
            if a[i] == '*':
                if len(scores) > 0:
                    scores[-1] *= 2
                score *=2
                i+=1

            elif a[i] == '#':
                score *= -1
                i+=1
        scores.append(score)

    return sum(scores)
  

