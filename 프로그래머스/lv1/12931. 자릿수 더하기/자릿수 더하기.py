def solution(n):
    sum = 0
    for i in range(len(str(n))):
        sum +=(n%(10**(i+1)))//10**i 

    return sum