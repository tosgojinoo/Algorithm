'''
[설명]
자물쇠는 동그란 디스크 N개로 구성
각 디스크에는 숫자가 0부터 9까지 숫자 표시
0과 9는 인접

한 번 자물쇠를 돌릴 때, 최대 세 칸을 시계 방향 또는 반시계 방향으로 돌릴 수 있다.
최대 세 개의 인접한 디스크를 한 번에 돌릴 수 있다.

[문제]
최소 몇 번을 돌려야 풀 수 있는지
'''
'''
[알고리즘]
- turn
    - 
- DP
    - init -1
    - 10 x 10 x N (nums, state, 원판수)  ??

i   0                   
a   0
b   0

555
444
464

'''
'''
[구조]
- N = int(input()) # 비밀번호의 길이 (자물쇠의 크기) N
- S = list(map(int, list(input()))) # 현재 자물쇠의 상태 예)555
- T = list(map(int, list(input()))) # 비밀번호 예)464
turn = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1]
DP = [[[-1] * 10 for _ in range(10)] for _ in range(N)]
print(go(0, 0, 0))

- go(idx, a, b): 원판 idx, 다음칸이 영향을 받는 회전 수(t1), 다음 다음 칸이 영향을 받는 회전수(t2)
    - if idx == N: 원판은 N-1 까지
        - return 0  
    - if DP[idx][a][b] != -1:
        # idx-1 원판을 돌려, idx-1 원판이 (init num +) a번,  idx 원판이 (init num +) b번 돌아 간 경우 
        # 비밀번호로 맞추기 위한 최소 횟수
        return DP[idx][a][b]
    cur = (S[idx] + a) % 10
    ans = float('inf')
    for j in range(10):
        for k in range(10):
            one = (T[idx] - cur - j - k) % 10
            ret = turn[j] + turn[k] + turn[one] + go(idx + 1, (b + j + k) % 10, k)
            ans = min(ret, ans)
    DP[idx][a][b] = ans
    return ans

'''

'''
BFS
bitmask: 3개, 2개, 1개 돌리는 case
DP = [ ] * 9 * N
'''
'''
https://fullalgorithmpanic.blogspot.com/2016/11/boj-1514.html
'''

import sys

sys.setrecursionlimit(10 ** 5)

def go(i, a, b):
    if i == N:
        return 0
    if DP[i][a][b] != -1:
        return DP[i][a][b] # i번째를 돌릴 것이고, i-1까지의 돌림에 의해서 i번째가 a번, i+1번째가 b번돌아 간 경우 비밀번호로 맞추기 위한 최소 횟수
    cur = (S[i] + a) % 10
    ans = float('inf')
    for j in range(10):
        for k in range(10):
            one = (T[i] - cur - j - k) % 10
            ret = turn[j] + turn[k] + turn[one] + go(i + 1, (b + j + k) % 10, k)
            ans = min(ret, ans)
    DP[i][a][b] = ans
    return ans


N = int(input()) # 비밀번호의 길이 (자물쇠의 크기) N
S = list(map(int, list(input()))) # 현재 자물쇠의 상태
T = list(map(int, list(input()))) #  비밀번호

turn = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1]
DP = [[[-1] * 10 for _ in range(10)] for _ in range(N)]
print(go(0, 0, 0))


