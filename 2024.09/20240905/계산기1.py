import sys
sys.stdin = open('input2.txt')

arr = input()
dap = ''
stack =[]
for i in arr:
    if i.isdigit():
        dap +=i
    elif i == '+':
        stack.append(i)
    