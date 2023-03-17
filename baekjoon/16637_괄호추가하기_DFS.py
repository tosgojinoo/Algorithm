'''
[설명]
길이가 N
수식은 0보다 크거나 같고, 9보다 작거나 같은 정수
연산자(+, -, ×)
연산자 우선순위는 모두 동일
수식을 계산할 때는 왼쪽에서부터 순서대로 계산

수식에 괄호를 추가하면, 괄호 안에 들어있는 식은 먼저 계산
괄호 안에는 연산자가 하나
중첩된 괄호는 사용 불가

추가하는 괄호 개수의 제한은 없음
추가하지 않아도 됨
문자열은 정수로 시작
연산자와 정수가 번갈아가면서 나옴
연산자는 +, -, * 중 하나
여기서 *는 곱하기 연산을 나타내는 × 연산
항상 올바른 수식만 주어지기 때문에, N은 홀수

[문제]
괄호를 적절히 추가해서 얻을 수 있는 결과의 최댓값 -> 경우의 수 DFS
정답은 2^31보다 작고, -2^31보다 크다.
'''
'''
[알고리즘]
- DFS
    - 괄호 내 수식은 단 한개만 가능 => bitmask 불필요
    - (op+숫자) 묶어가며 계산
    - case는 2개
        - 괄호 없이 계산
            - ixd + 2
            - a + b
            - (a + b) + c
            - a + (b + c) + d
        - 괄호 우선 계산
            - idx + 4
            - a + (b + c)
            - a + b + (c + d)
            - (a + b) + (c + d) == e + (c + d)
    - DFS(계산 완료 idx, 계산 결과)
            
'''
'''
[구조]
- arr 저장
- DFS(0, int(arr[0]))
- print(result)


- DFS(idx, value):
    # 마지막 자리일 경우
    - if idx == N - 1: 
        result = max(result, value)
        return
    
    # 괄호 없이 계산
    # a + b
    - if idx + 2 < N: 
        - DFS(idx + 2, operation(value, arr[idx + 1], int(arr[idx + 2])))
    
    # 괄호를 넣을 경우 계산
    # a + (b + c) 
    - if idx + 4 < N: 
        - DFS(idx + 4, operation(value, arr[idx + 1], operation(int(arr[idx + 2]), arr[idx + 3], int(arr[idx + 4]))))

- operation(num1, operator, num2):

'''


import sys

def operation(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2

def DFS(idx, value):
    global result

    if idx == N - 1: # 마지막 자리일 경우
        result = max(result, value)
        return

    if idx + 2 < N: # 괄호 없이 계산
        # print(f'[{idx + 2}] ({value}  {arr[idx + 1]}  {int(arr[idx + 2])})')
        DFS(idx + 2, operation(value, arr[idx + 1], int(arr[idx + 2])))

    if idx + 4 < N: # 괄호를 넣을 경우 계산
        # print(f'[{idx + 4}] {value}  {arr[idx + 1]}  ({int(arr[idx + 2])}  {arr[idx + 3]}  {int(arr[idx + 4])})')
        DFS(idx + 4, operation(value, arr[idx + 1], operation(int(arr[idx + 2]), arr[idx + 3], int(arr[idx + 4]))))

N = int(input())
arr = input()
result = -1 * sys.maxsize
DFS(0, int(arr[0]))
print(result)