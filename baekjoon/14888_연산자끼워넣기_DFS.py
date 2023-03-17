'''
[설명]
N개의 수
수열 A1, A2, ..., AN
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 
주어진 수의 순서를 변경 x 

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
나눗셈은 정수 나눗셈으로 몫만
음수를 양수로 나눌 때는 C++14의 기준
양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것 

만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 
덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

[문제]
1. 만들 수 있는 식의 결과의 최댓값 -> 경우의 수 DFS
2. 최솟값

'''
'''
[알고리즘]
- operators
    - 연산자 개수 저장 memory
    
- DFS(idx, total, operators)
    - 변수
        - idx: 수식 내 순번
        - total: 누적 계산값
        - operators: 연산자 개수
    - 연산자 하나 선택 > 계산값, 해당 연산자 개수 감소 후 DFS > idx 증가 > idx 끝까지 반복
'''
'''
[구조]      
- nums = list(map(int, input().split())) # 주어진 숫자들
- operators = list(map(int, input().split()))  # +, -, *, //

- maximum = -1e9
- minimum = 1e9

- DFS(1, nums[0], operators)
- print(maximum)
- print(minimum)


- DFS(idx, total, operators):
    - plus, minus, multiply, divide = operators

    - if idx == N:
        - maximum = max(total, maximum)
        - minimum = min(total, minimum)
        - return

    - if plus:
        - DFS(idx + 1, total + nums[idx], [plus - 1, minus, multiply, divide])
    - if minus:
        - DFS(idx + 1, total - nums[idx], [plus, minus - 1, multiply, divide])
    - if multiply:
        - DFS(idx + 1, total * nums[idx], [plus, minus, multiply - 1, divide])
    - if divide:
        - DFS(idx + 1, int(total / nums[idx]), [plus, minus, multiply, divide - 1])     
'''


import sys

input = sys.stdin.readline

def DFS(idx, total, operators):
    global maximum, minimum
    plus, minus, multiply, divide = operators

    if idx == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        DFS(idx + 1, total + nums[idx], [plus - 1, minus, multiply, divide])
    if minus:
        DFS(idx + 1, total - nums[idx], [plus, minus - 1, multiply, divide])
    if multiply:
        DFS(idx + 1, total * nums[idx], [plus, minus, multiply - 1, divide])
    if divide:
        DFS(idx + 1, int(total / nums[idx]), [plus, minus, multiply, divide - 1])


N = int(input()) # 수의 개수
nums = list(map(int, input().split())) # 주어진 숫자들
operators = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9

DFS(1, nums[0], operators)
print(maximum)
print(minimum)
