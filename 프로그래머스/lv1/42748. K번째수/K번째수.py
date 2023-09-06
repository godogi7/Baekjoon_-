def solution(array, commands):
    answer = []
    for list in commands:
        new = array[list[0]-1:list[1]]
        new.sort()
        answer.append(new[list[2]-1])
    return answer