n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
print(data)
data.sort(reverse=True)
print(data)