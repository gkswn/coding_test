import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.sort()

def bin(arr,target ,start, end):
    while start <= end:
        mid = (start+end)//2
        total = 0
        for i in arr:
            if i > mid:
                total += mid
            else:
                total += i
        if total <= target:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(bin(arr, m, 0, max(arr)))