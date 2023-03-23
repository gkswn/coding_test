import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\이진탐색\\input.txt")

t= int(input())
for _ in range(t):
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int,input().split()))
    A.sort(), B.sort()

    cnt = 0
    pair = 0
    for i in range(len(A)):
        while True:
            if cnt == m or A[i] <= B[cnt]:
                pair += cnt
                break
            else:
                cnt += 1
    
    print(pair)