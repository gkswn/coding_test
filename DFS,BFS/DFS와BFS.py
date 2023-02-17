from collections import deque

import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\DFS,BFS\\input.txt")

def dfs(v):
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i]==0 and 




n,m,v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)

for i in range(m):
    array = 