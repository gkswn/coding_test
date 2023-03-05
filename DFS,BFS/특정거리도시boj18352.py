from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [-1] *(n+1)
visit[x] = 0

for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    
def bfs(start):
    answer = []
    visit[start] = True
    q = deque()
    q.append([start])
    while q:
        now = q.popleft()
        for i in range(m):
            pass
            
