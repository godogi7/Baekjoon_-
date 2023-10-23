def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price*(i+1)
    if money - total < 0:
        return (money-total)*(-1)
    else: 
        return 0
    return answer