import sys
sys.stdin = open("C:\\Users\\hanju\\workspace\\coding_test\\완전탐색\\input.txt")
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

cases = list(permutations(arr,n))

answer = 0
for case in cases:
    mid_sum = 0
    for i in range(n-1):
        mid_sum += abs(case[i]-case[i+1])
    answer = max(mid_sum, answer)

print(answer)