import sys
from itertools import permutations
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

t = int(input())

for i in range(t):
    n = int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    result = 0
    for j in range(2,n):
        result = max(result,abs(tree[j]- tree[j-2]))
    print(result)