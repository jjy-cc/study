n = input()

result = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)