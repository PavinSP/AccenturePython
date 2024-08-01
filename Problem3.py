n = int(input())
arr = list(map(int, input().split()))
a_count = 0
for i in range(len(arr)):
    while arr[i] > 0:
        if arr[i] >= 3:
            a_count += 1
            arr[i] -= 3
        elif arr[i] >= 2:
            a_count += 1
            arr[i] -= 2
        elif arr[i] >= 1:
            a_count += 1
            arr[i] -= 1
print(a_count)