arr = list(map(int, input().split()))
position = 0
answer = 0
for i in arr:
    position += i
    answer = max(position, answer)
print(answer)