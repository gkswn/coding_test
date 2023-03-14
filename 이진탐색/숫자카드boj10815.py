import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
arr.sort()

def binary(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary(arr, find[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')