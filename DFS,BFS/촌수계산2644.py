from collections import deque
import sys
sys.stdin = open('C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt')

#################

n = int(input())
a,b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
result = []

#################

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v,num):
    num+=1
    visit[v] = True

    if v == b:
        result.append(num)

    for i in graph[v]:
        if not visit[i]:
            dfs(i,num)

dfs(a,0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)