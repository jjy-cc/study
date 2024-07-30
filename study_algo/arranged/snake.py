n = int(input())
k = int(input())

data = [[0] * (n+1) for _ in range(n+1)]
#사과 위치 삽입
for _ in range(k):
    x, y = map(int, input().split())
    data[x][y] = 1

l = int(input())
info = []
#뱀 위치 삽입
for _ in range(l):
    a, b = input().split()
    info.append((int(a), b))

#처음에는 오른쪽, (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 #뱀 머리 위치
    data[x][y] = 2 #뱀이 존재하는 위치는 2로 표시
    direction = 0 #처음에는 동쪽
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] #뱀이 차지하고 있는 위치 정보(꼬리 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        #맵 범위 안에 있고 뱀의 몸통이 없는 위치라면
        if nx > 0 and nx <= n and ny > 0 and ny <= n and data[nx][ny] != 2:
            #사과가 없다면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[ny][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0
            #사과 있으면 이동 후 꼬리 두기
            elif data[ny][ny] == 1:
                data[ny][ny] = 2
                q.append((nx, ny))
        #벽이나 뱀의 몸통과 부딪히면
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
    return time