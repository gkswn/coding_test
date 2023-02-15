from collections import deque

import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\DFS,BFS\\input.txt")

n,m,v = map(int,input().split())

def dfs(v):
    dfs_visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if dfs_visited[v] == 0:
           dfs_visited[i] = 1
           dfs(i)


def bfs(v):
    q = deque([v])
    bfs_visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for next_node in graph[v]:
            if bfs_visited[next_node] == 0:
                bfs_visited[next_node] = 1
                q.append(next_node)

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 양방향 그래프와 낮은 수를 가지는 정점부터 탐색을 시작하기 위함
    graph[b].append(a)
    graph[a].sort()

dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

dfs(v)
print()
bfs(v)