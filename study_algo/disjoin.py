#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 대까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def find_parent2(parent , x):
    if parent[x] != x:
        parent[x] = find_parent2(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def union_parent2(parent, a, b):
    a = find_parent2(parent, a)
    b = find_parent2(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(e):
    a, b = map(int, input().split())
    union_parent2(parent, a, b)

#각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()