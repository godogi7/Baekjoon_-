def solution(sizes):
    wallet = [0,0]
    for i in sizes:
        if i[0] <= i[1]:
            i[0], i[1] =   i[1], i[0]
            
        if wallet[0] < i[0]:
            wallet[0] = i[0]
        
        if wallet[1] < i[1]:
            wallet[1] = i[1]
    return wallet[0]*wallet[1]