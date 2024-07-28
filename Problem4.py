n = int(input())
p = int(input())
remaining_time = 240 - p
count = 0
for i in range(1, n+1):
    solving_time = i*5
    if remaining_time >= solving_time:
        remaining_time -= solving_time
        count += 1
print(count)