n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = []
answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #북 동 남 서
dy = [0, -1, 0, 1]

graph[x][y] = 2

#왼쪽 방향에 가지 않은 곳 있으면 방향 틀기, 가보거나/바다면 방향 틀기

while True:
    cnt = 0
    #print(graph)
    for i in range(direction+1, direction+5):
        dir = i % 4
        direction = dir
        nx, ny = x + dx[dir], y + dy[dir]
        if graph[nx][ny] == 0 and 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
            graph[nx][ny] = 2
            answer += 1
            #print("x : " , x, " y : ", y)
            break

        cnt += 1

    if cnt == 4:
        if graph[x-dx[(direction)%4]][y-dy[(direction)%4]] == 1:
            break
        else:
            x, y = x-dx[(direction)%4], y-dy[(direction)%4]
            answer += 1
            #print("x : ", x, " y : ", y)

print(answer)