n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)
def dfs(n):
    return

def bfs(n):
    return