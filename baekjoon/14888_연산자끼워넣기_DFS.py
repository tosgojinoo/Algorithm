# DFS, back tracking, 시뮬레이션
# memory 에 operator 저장 후 DFS에 같이 넘기기
# DFS depth는 수열의 순서

import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9

def DFS(depth, total, operators):
    global maximum, minimum
    plus, minus, multiply, divide = operators

    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        DFS(depth + 1, total + num[depth], [plus - 1, minus, multiply, divide])
    if minus:
        DFS(depth + 1, total - num[depth], [plus, minus - 1, multiply, divide])
    if multiply:
        DFS(depth + 1, total * num[depth], [plus, minus, multiply - 1, divide])
    if divide:
        DFS(depth + 1, int(total / num[depth]), [plus, minus, multiply, divide - 1])


DFS(1, num[0], operators)
print(maximum)
print(minimum)


'''참고
import sys
sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

maxResult = -1000000000
minResult = 1000000000


def backTracking(curResult, idx):
    if idx == N:
        global maxResult, minResult
        maxResult = max(maxResult, curResult)
        minResult = min(minResult, curResult)
        return
    li = [curResult+A[idx], curResult-A[idx], curResult*A[idx], int(curResult/A[idx])]
    for i, nextResult in enumerate(li):
        if operator[i]:
            operator[i] -= 1
            backTracking(nextResult, idx+1)
            operator[i] += 1


backTracking(A[0], 1)
print(maxResult)
print(minResult)
'''