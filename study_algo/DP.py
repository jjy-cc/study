def dp1():
    x = int(input())
    d = [0] * 30001

    for i in range(2, x+1):
        #현재의 수에서 1을 빼는 경우
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        elif i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        elif i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)

    print(d[x])

def dp2():
    n = int(input())
    arr = list(map(int, input().split()))

    d = [0] * 100

    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + arr[i])


    print(d[n-1])

def dp3():
    n = int(input())

    d = [0] * 1001

    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = (d[i-1]+2 * d[i-2]) %796796

    print(d[n])

def dp4():
    n, m = map(int, input().split())

    coin = []

    for i in range(n):
        coin.append(int(input()))

    d = [10001] * (m+1)

    d[0] = 0
    for i in range(n):
        for j in range(coin[i], m+1):
            if d[j-coin[i]] != 10001:
                d[j] = min(d[j], d[j-coin[i]+1])

    if d[m] == 10001:
        print(-1)
    else:
        print(d[m])