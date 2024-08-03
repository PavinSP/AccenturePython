n = input()
steps = 0
i = 0
while i < len(n):
    if i < len(n) - 1 and n[i] == '0' and n[i + 1] == '0':
        steps += 1
        i += 2
    else:
        steps += 1
        i += 1
print(steps)