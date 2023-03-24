import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

t = int(input())

def bin(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()
    m = int(input())
    note2 = list(map(int, input().split()))
    
    for num in note2:
        print(bin(note1, num, 0, n-1))     