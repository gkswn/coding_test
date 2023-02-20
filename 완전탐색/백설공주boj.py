from itertools import combinations
import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\coding_test\\완전탐색\\input.txt")

array = [int(input()) for _ in range(9)]

board = list(combinations(array, 7))

for i in range(len(board)):
    if sum(board[i]) == 100:
        for j in range(7):
            print(board[i][j])