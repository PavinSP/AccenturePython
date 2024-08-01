n = int(input())
for i in range(2, n):
    if n % i == 0:
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag == 0:
            print(i, end=" ")
