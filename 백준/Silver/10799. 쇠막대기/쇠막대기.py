s = input()

stack = []
count = 0
for i in range(len(s)):
	if s[i] == '(':
		stack.append(s[i])
	elif s[i] == ')' and s[i-1] == '(':
		stack.pop()
		count += len(stack)
	else:
		stack.pop()
		count += 1
print(count)