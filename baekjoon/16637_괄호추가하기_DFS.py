''' my idea
N = 수식 길이
visited[bitmask '('][bitmask ')']
stack = '(',')' pairing
max(visited)

'''
'''
괄호 내 수식은 단 한개만 가능 => bitmask 불필요
DFS로 2개씩 묶어가며 계산
'''

import sys

def operation(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2

def DFS(index, value):
    global result

    if index == N - 1: # 마지막 자리일 경우
        result = max(result, value)
        return

    if index + 2 < N: # 괄호 없이 계산
        print(f'[{index + 2}] ({value}  {input_seq[index + 1]}  {int(input_seq[index + 2])})')
        DFS(index + 2, operation(value, input_seq[index + 1], int(input_seq[index + 2])))

    if index + 4 < N: # 괄호를 넣을 경우 계산. index 2/4를 먼저 계산 후 index 0 or value와 계산
        print(f'[{index + 4}] {value}  {input_seq[index + 1]}  ({int(input_seq[index + 2])}  {input_seq[index + 3]}  {int(input_seq[index + 4])})')
        DFS(index + 4, operation(value, input_seq[index + 1], operation(int(input_seq[index + 2]), input_seq[index + 3], int(input_seq[index + 4]))))

N = int(input())
input_seq = input()
result = -1 * sys.maxsize
DFS(0, int(input_seq[0]))
print(result)