from collections import deque
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\DFS,BFS\\input.txt")

n = int(input())
tree = [ [] for _ in range(n+1) ]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs():
    queue = deque([1])

    while queue:
        node = queue.popleft()

        for i in tree[node]:
            if parent[i] == 0:
                parent[i] = node
                queue.append(i)

bfs()

for i in parent[2:]:
    print(i)