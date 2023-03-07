import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

n,m = map(int,input().split())
arr = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start>=end:
        mid = (start+end)//2
        

print(n,m)
print(arr)