import sys
T = int(input())
for i in range(T):
    # input() 사용시, 런타임 에러 뜸, T의 최대 개수는 1,000,000이었기에, input 사용하면 백만번의 입력을 백만번 처리해야 한다
    # 그런데, sys.stdin.readline 사용하면 시간 복잡도 O(1) 가지기에, 1번 입력하나 백만번 입력하나 처리의 속도에 큰 차이가 없다.
    # sys.stdin.readline() 함수 사용해, 입력 시간 줄임
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
