# by 상혁
def solution(s):
    # stack , 열려있으면 ( 넣고, 
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
            
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True

