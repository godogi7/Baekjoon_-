"""def solution(numbers):
    answer=[]
    for i in range(len(numbers)-1):
        if str(numbers[i])+str(numbers[i+1]) < str(numbers[i+1])+str(numbers[i]):
            numbers[i],numbers[i+1] = numbers[i+1], numbers[i]
        print(numbers)
    return numbers"""

def solution(numbers):
    # 숫자들을 문자열로 변환
    numbers_str = [str(num) for num in numbers]
    # 정렬 기준으로 문자열 결합 비교를 사용하여 정렬
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    # 정렬된 문자열을 합치기
    answer = ''.join(numbers_str)
    # 모든 숫자가 0인 경우를 처리 (예: "000" -> "0")
    return answer if answer[0] != '0' else "0"