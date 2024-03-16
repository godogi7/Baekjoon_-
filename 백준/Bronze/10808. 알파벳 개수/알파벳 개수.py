#s = 'baekjoon'
s = input()
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count_list = []
for alphabet in alphabet_list:
  count_list.append(str(s.count(alphabet)))
answer = ' '.join(count_list)
print(answer)
