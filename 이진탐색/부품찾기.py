import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt")

def binary_search(array,target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
a = list(map(int,input().split()))

a.sort()

m = int(input())
b = list(map(int,input().split()))

for i in b:
    result = binary_search(a,i,0,n-1)
    if result != None:
        print('yes', end =' ')
    else:
        print('no', end=' ')
    