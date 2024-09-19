t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = (list(map(int, input().split())))
    data = []
    for i in range(0, len(a), m):
        data.append(a[i:i+m])

    answer = data
    for i in range(m - 1):
        for j in range(n):
            if j == 0:
                answer[j][i] += max(answer[j][i + 1], answer[j + 1][i + 1])
            elif j == 1:
                answer[j][i] += max(answer[j - 1][i + 1], answer[j][i + 1], answer[j + 1][i + 1])
            else:
                answer[j][i] += max(answer[j - 1][i + 1], answer[j][i + 1])

    result = 0
    for i in range(n):
        result = max(result, answer[i][-2])

    print(result)
    print(answer)