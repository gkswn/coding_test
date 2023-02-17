import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\정렬\\input.txt")

list = list(map(int, input().split()))

list.sort()

print(list[2])