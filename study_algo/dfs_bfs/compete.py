from collections import deque

n, k = map(int, input().split())

data = [] #전체 맵
virus = [] #바이러스 위치
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], 0, i, j)) #바이러스 종류, 시간, 위치x, 위치 y

s, a, b = map(int, input().split()) #시간, x, y

dx = [0,1,0,-1]
dy = [1,0,-1,0]

virus.sort() #낮은 바이러스 먼저 옮겨야 함
q = deque(virus)

while q:
    kind, t, x, y = q.popleft()
    if t == s:
        break
    #상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #위치 이동x
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        #방문o
        if data[nx][ny] != 0:
            continue

        data[nx][ny] = kind
        q.append((kind, t+1, nx, ny))

print(data)
print(data[a-1][b-1])
