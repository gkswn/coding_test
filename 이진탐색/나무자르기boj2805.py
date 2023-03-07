import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

n,m = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

def binary_search(array, start, end):
    res = 0
    while start<=end:
        mid = (start+end)//2
        total = 0

        for x in array:
            if x>mid:
                total += x -mid
        
        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid+1 
    return res

r = binary_search(arr,0,max(arr))
print(r)