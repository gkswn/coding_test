import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
arr.sort()

def binary(arr,target,start, end):
    if start>end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return arr[start:end+1].count(target)
    elif arr[mid] < target:
        return binary(arr,target,mid+1,end)
    else:
        return binary(arr,target,start,mid-1)

for i in range(m):
    a = binary(arr,find[i],0,n-1)
    if a is not None:
        print(a,end=' ')
    else:
        print(0,end=' ')