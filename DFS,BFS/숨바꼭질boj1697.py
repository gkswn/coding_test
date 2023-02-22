from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

n,k = map(int,input().split())
max = 10**5
dist = [0]*(max+1)

################################

def bfs(v,k):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        if v == k:
            print(dist[v])
            break
        for  nx in (v-1,v+1, v*2):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[v]+1
                queue.append(nx)

bfs(n,k)