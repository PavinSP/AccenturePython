n = int(input())
arr = list(map(int, input().split()))
d = {}
if len(arr) == 1:
    print(arr[0])
else:
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_count = 0
    max_count_element = None
    element_with_max_count = []
    for key, value in d.items():
        if value > max_count:
            max_count = value
            max_count_element = key
            element_with_max_count = [key]
        elif value == max_count:
            element_with_max_count.append(key)
    if len(element_with_max_count) > 1:
        print(-1)
    else:
        print(max_count_element)