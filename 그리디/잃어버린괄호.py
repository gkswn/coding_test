import sys
sys.stdin = open("C:\\Users\\안한주\\Desktop\\파이썬 코테\\그리디\\input.txt")

formula = input()

plus = formula.find('-')

formula = list(formula)
formula.insert(plus+1,'(')
formula.insert(len(formula),')')

result = 0

for i in range(len(formula)):
    result += int(formula[i])


print(plus)
print(formula)
print(result)
