n = int(input())

arr = [1]*n  # n = 7
arr[0] = 1
if n >= 2:
    arr[1] = 2
    for i in range(2,n): # 2, 3, 4, 5, 6
        arr[i] = (arr[i-1] + arr[i-2])%10007
        #print(f"i-1 and i-2, arr[i] = {arr[i-1]},{arr[i-2]},{arr[i]}")
print(arr[-1])