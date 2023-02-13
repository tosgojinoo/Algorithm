''' my idea
M 칸에 3명 병사 배치 경우의 수, 루프
attack(y,x)
- 사정거리 내
    - 우선 순위
        - 가장 가까운 적
        - 가장 왼쪽

main
for 3명 병사 경우의 수 in 5
- for turn in M
    - visited 초기화
    - for y,x in 3명 병사 경우의 수
        - attack(y,x)
'''

import sys

input = sys.stdin.readline
def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:  # 종료 조건
            yield [arr[i]]
        else:
            for nxt in combinations(arr[i + 1:], r - 1):
                yield [arr[i]] + nxt

def attack(case): # 거리 D이하. 적 중 가장 가까운. 가장 왼쪽.
    attack_list = list()
    cnt = 0
    for m_pose in case:
        target = list()
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 1: # 적 이면
                    now_d = abs(i - N) + abs(j - m_pose) # 거리: |r1-r2| + |c1-c2|
                    if limit >= now_d: # 적 거리가 사거리 안이면
                        target.append((now_d, i, j)) # 대상 추가. (거리, x, y)
        target.sort(key=(lambda x: (x[0], x[2]))) # 거리 가깝고 > 왼쪽 기준 정렬
        if target: # 대상 있으면
            attack_list.append(target[0]) # 대상 중 첫번째를 제거 대상에 추가

    for a in attack_list:
        _, i, j = a
        if tmp[i][j] == 1:
            tmp[i][j] = 0 # 적 사망 처리
            cnt += 1 # 사망 숫자 추가
    return cnt

def move(): # 적 아래로 이동
    for i in range(-1, -N, -1):
        tmp[i] = tmp[i - 1]

    tmp[0] = [0] * M

def is_empty(): # 적 확인
    if sum(map(sum, tmp)) > 0:
        return False
    return True

N, M, limit = map(int, input().split())  # 행, 열, 궁수의 공격 거리 제한
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

for case in combinations(range(M), 3):  # 1. 궁수 배치 - 모든 경우의 수 배치 3명
    tmp = []
    for i in range(N):
        tmp.append(arr[i].copy())
    cnt = 0
    while not is_empty():  # 적이 있는 동안 계속 반복
        cnt += attack(case)
        move()
    result = max(result, cnt)

print(result)