import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\input.txt")

case_num = int(input())
num_list = list(map(int,input().split()))

num_list.sort()

result = 0
temp = 0

for i in range(case_num):
    result += int(num_list[i]) * (case_num-i)


print(result)