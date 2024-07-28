arr = input()
vowels = ['a', 'e', 'i', 'o', 'u']
d = {}
for i in arr:
    d[i] = 0
for i in arr:
    if i in vowels:
        d[i] += 1
max_count = 0
max_value = None
for key, value in d.items():
    if value > max_count:
        max_count = value
        max_value = key
print(max_value)