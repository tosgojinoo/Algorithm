# 명령어 D, S, L, R
# 0 이상 10,000 미만의 십진수를 저장
# n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4

# D: 2*n // 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지 저장(2n mod 10000)
# S: n-1 // n이 0 이라면 9999 저장
# L: n의 각 자릿수를 왼편으로 회전 // d2, d3, d4, d1
# R: n의 각 자릿수를 오른편으로 회전 // d4, d1, d2, d3

# q 이용
# 최소한 명령어 => BFS
# 문자열 숫자 변환 => int("0001")

# [순서]
# 1. 입력
# 2. for DSLR
# 2-1. 각각을 처리할 함수를 따로 둘 것인가?
# 3. 변환 결과 + 명령어 나열(string으로 전달), q에 저장

# [종료]
# 1. q.popleft() == B
# 1-1. return 명령어 나열

# [주의]
# 최소이므로, DFS 비효율적
# 결과는 항상 int로 변환 후 확인
# ***** L변환시, x의 자리수가 4자리가 안될 경우, 0으로 체워야함 (123 -> 0123 -> 1230)
# pypy3, sys.stdin.readline 만 가능
# *** str 무거움, 처리 방법
# 1) 4자리 입력값 및 'DSLR' 처리를 문자가 아닌 숫자로 적용
# 2) 'order'저장을 문자가 아닌 8진수로 하기(https://www.acmicpc.net/source/43426207)

# [체크]
# visited x => * 메모리 초과 & 동일 숫자 재방문 이슈 때문에 사용

from collections import deque
import sys
input = sys.stdin.readline

# def checker(num):
#     num = str(num)
#     for i in range(4-len(num)):
#         num = '0'+ num
#     return num

def BFS():
    global visited
    q = deque([(A, "")]) # tuple in list 로 구성
    visited[A] = 1
    while q:
        x, orders = list(q.popleft())
        if x == B:
            print(orders)
            return
        for order in ['D', 'S', 'L', 'R']:
            if order == 'D':
                nx = (x*2) % 10000 # 조건문 처리시, 지연 발생
            elif order == 'S':
                nx = (x-1) % 10000 # * 'S' 만 해당, 문자 주의 # 조건문 처리시, 지연 발생
            elif order == 'L':
                nx = (x*10 + x//1000) % 10000 # 10000 이하 숫자만 남음 # str 슬라이스로 처리, 지연 발생
            elif order == 'R':
                nx = x//10 + (x%10)*1000 # str 슬라이스로 처리시, 지연 발생

            if visited[nx] == 0:
                visited[nx] = 1
                q.append((nx, orders + order)) # order 누적 주의

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    visited = [0] * (10**5+1)
    BFS()