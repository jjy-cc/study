def solution(number, k):
    answer = ''
    delete = 0
    arr = list(number)
    samenum = 0
    i = 0
    while delete <= k:
        if int(arr[i]) < int(arr[i + 1]) and arr[i] != '0' and i < len(arr) - 1:
            if samenum > 0:
                for j in range(samenum + 1):
                    arr[i - j] = '0'
                    delete += 1
            else:
                delete += 1
                arr[i] = '0'
            samenum = 0
            i = 0
            print(arr)
        elif len(arr) - 1 > i and int(arr[i]) == int(arr[i + 1]):
            samenum += 1
            i += 1
        else:
            samenum = 0
            i += 1

    print(arr)

    for i in range(len(arr)):
        if arr[i] == '0':
            continue

        answer += arr[i]

    return answer

t = solution("4177252841", 4)
print(t)