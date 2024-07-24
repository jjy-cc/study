def sol():
    n = int(input())

    result = []

    for i in range(n):
        result.append(int(input()))

    array = sorted(result, reverse=True)

    for i in array:
        print(i, end=' ')

def sol2():
    n = int(input())

    dic = []
    for i in range(n):
        input_data = input().split()
        dic.append(input_data[0], int(input_data[1]))

    array = sorted(dic, key=lambda x: x[1])

    for student in array:
        print(student[0], end=' ')

def sol3():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    print(sum(a))