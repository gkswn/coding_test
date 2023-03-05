import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
find = list(map(int, input().split()))

for num in find:
    start, end = 0, n-1
    exist = False

    while start<=end:
        mid = (start + end) // 2
        if num == arr[mid]:
            exist = True
            print(1)
            break
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    
    if not exist:
        print(0)
