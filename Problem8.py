n = int(input())
arr = list(map(int, input().split()))
num = int(input())
factors = {}
def isPrime(a):
    if a <= 1:
        return False
    for i in range(2, (a//2) + 1):
        if a % i == 0:
            return False
    return True
for i in range(2, (num // 2) + 1):
    if num % i == 0:
        if isPrime(i):
            count = 0
            while (num % i == 0):
                count += 1
                num //= i
            factors[i] = count
sum = 0
for key, value in factors.items():
    if key < len(arr):
        sum += arr[key] * value
    else:
        print(0)
        exit()
if len(arr) == 0:
    print(-1)
else:
    print(sum)