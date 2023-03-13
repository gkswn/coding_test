import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

k,n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()
start, end = 1, max(arr)

while start<=end:
    mid = (start+end)//2
    lines = 0
    for i in arr:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)