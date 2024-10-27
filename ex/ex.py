from collections import deque

def solution(number, k):
    answer = ''
    q = deque(list(map(int, number)))
    delete = 0
    samenum = 0

    while delete <= k:
        a = q.popleft()
        if a > q[0]:
            if samenum > 0:
                for _ in range(samenum + 1):
                    q.appendleft(a)
                samenum = 0
            else:
                q.appendleft(a)
        elif q[0] == a:
            samenum += 1
        else:
            if samenum > 0:
                delete += samenum + 1
                samenum = 0
            else:
                delete += 1

        print(q)
    return answer

t = solution("1924", 2)
print(t)