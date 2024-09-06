n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(input())
data.sort()

start = 1
end = data[-1]
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = data[0]
    count = 1

    for i in range(1, n):
        if data[i] >= value + mid:
            value = data[i]
            count += 1
    if count == c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)