from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
    k = map(int, input().split())
    for j in range(n):
        if k[j] == 1:
            house.append((i, j))
        elif k[j] == 2:
            chicken.append((i, j))

#모든 치킨 집에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    #모든 집에 대하여
    for hx, hy in house:
        #가장 가까운 집 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cy) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
