n, m = map(int, input().split())
data = []
temp = [[0]*m for _ in range(n)]

for i in range(n):
    data.append(list(map(int, input().split())))

dx,dy = [-1,0,1,0],[0,1,0,-1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #상하좌우->바이러스 퍼질 수 있는 곳
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스 배치, 다시 재귀
                temp[nx][ny] == 2
                virus(ny, ny)
#안전영역 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
#깊이우선탐색 -> 울타리 설치 -> 안전 영역 크기 계산
def dfs(count):
    global result
    #울타리 3개 설치(조건)
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] == data[i][j]

        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    #빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)