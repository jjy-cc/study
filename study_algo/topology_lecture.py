from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트
graph = [[] for i in range(v+1)]
#각 강의 시간을 0으로 초기화
time = [0] * (v+1)

#방향 그래프의 모든 간선정보 입력
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

#위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    #처음 시작 > 진입차수 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()