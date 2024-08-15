from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1

    point = len(weak)
    for i in range(point):
        weak.append(weak[i] + n)

    for start in range(point):
        for friends in list(permutations(dist, len(dist))):
            count = 0
            position = weak[start] + friends[count]
            for index in range(start, start + point):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count]
            answer = min(answer, count + 1)
    if answer > len(dist):
        return -1
    return answer