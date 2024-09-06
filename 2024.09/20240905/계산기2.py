import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = input()
    dictionary = {'+':1, '*':2}
    operator = []
    dap = ''
    for i in arr:
        if i.isdigit():
            dap += i
        elif i == '+' and len(operator) == 0 or i == '*' and len(operator) == 0 :
            operator.append(i)
        elif i == '+' and len(operator) != 0 and operator[-1] != '*' or i == '*' and len(operator) != 0 :
            operator.append(i) 
        elif i == '+' and operator[-1] == '*':
            for j in range(len(operator)):
                dap += operator[len(operator) -j -1]
            for j in range(len(operator)):
                operator.pop()
            operator.append(i)
    if len(operator) >= 0:
        for i in range(len(operator)):
            dap += operator[len(operator) - i -1 ]
    stack = []
    for i in dap:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+': 
            stack.append(stack[-2] +stack[-1])
            stack.pop(-2)
            stack.pop(-2)
        elif i == '*':
            stack.append(stack[-2] * stack[-1])
            stack.pop(-2)
            stack.pop(-2)
    print(f'#{tc}', *stack)

