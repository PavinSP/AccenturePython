str = input()
p = int(input()) - 1
k = int(input())
result = ""
if len(str) == 0:
    print("")
    exit()
while k > 0:
    if 0 < p < len(str) - 1:
        if str[p-1] < str[p+1]:
            result = str[p-1]
            p -= 1
        else:
            result = str[p+1]
            p += 1
        k -= 1
    elif p == 0:
        p += 1
    elif p == len(str) - 1:
        p -= 1
print(result)