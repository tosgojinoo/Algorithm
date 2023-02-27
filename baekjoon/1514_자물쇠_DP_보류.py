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
N = int(input())
S = list(map(int, list(input())))
T = list(map(int, list(input())))
turn = [0, 1, 1, 1, 2, 2, 2, 1, 1, 1]

DP = [[[-1] * 10 for _ in range(10)] for _ in range(N + 1)]


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


print(go(0, 0, 0))