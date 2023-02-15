import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt", "r")

data = input()
row = int(data[1])
column = int(ord(data[0]))-int(ord('a'))+1

move = [(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
result = 0

for  mov in move:
    nrow = row + mov[0]
    ncol = column +mov[1]
    if nrow >=1 and nrow <=8 and ncol>=1 and ncol<=8:
        result +=1

print(result)