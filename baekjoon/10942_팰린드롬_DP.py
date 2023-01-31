# palindrome, 좌우 대칭 수열

# S, E 는 index
# palindrome: a == a[::-1] => 시간제한 문제
# DP memory로 모든 경우의 수에 대한 table 생성 후 검색 출력
# DP 계산시, E와 gap을 감안한 루프 적용

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

DP = [[0] * N for _ in range(N)]
# palindrome 모든 경우 계산
# 우선 1, 2자리 경우만 계산
for S in range(N):
    # 1자리 경우 무조건 1
    DP[S][S] = 1
    # 2자리인데 동일할 경우 1
    if S < N - 1 and arr[S] == arr[S+1]:
        DP[S][S+1] = 1

# 나머지 계산
for E in range(1, N): # 위 삼각형 생성, E부터 시작, E가 N까지 가기 때문
    for gap in range(1, E+1): # ***** gap을 적용한 루프가 핵심
        if arr[E] == arr[E-gap] and DP[E-gap+1][E-1] == 1:
            DP[E-gap][E] = 1


# 답변
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if S == E:
        print(1)
    else:
        print(1 if DP[S-1][E-1]==1 else 0)
