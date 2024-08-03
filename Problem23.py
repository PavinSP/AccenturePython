n, k, a = map(int, input().split())
lastChild = ((a + (k - 1) - 1) % n) + 1
print(lastChild)