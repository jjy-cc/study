n = int(input())
guild = list(map(int, input().split()))

guild.sort()
result = 0
count = 0

for num in guild:
    count += 1
    if count >= num:
        result += 1
        count = 0

print(result)