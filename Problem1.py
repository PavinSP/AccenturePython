n = int(input())
k = int(input())
arr = list(map(int, input().split()))
max_score = 0
for i in range(n-k+1):
    current_score = 0
    for j in range(1, k+1):
        current_score += arr[i+j-1] * j
    max_score = max(max_score, current_score)
print(max_score)