import sys
sys.stdin = open('C:\\Users\\안한주\\Desktop\\coding_test\\구현\\input.txt')

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = [0]*n
for i in range(n):
    ans[i] = arr[i] + arr[2*n-1-i]

print(min(ans))