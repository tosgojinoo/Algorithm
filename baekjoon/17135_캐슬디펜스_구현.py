'''
[설명]
N×M인 격자판
각 칸에 포함된 적의 수는 최대 하나
N번행의 바로 아래(N+1번 행)의 모든 칸에는 성
- 궁수
    - 궁수 3명을 배치 -> 다른 제한 없으므로, combinations(arr, 3)
    - 궁수는 성이 있는 칸에 배치
    - 하나의 칸에는 최대 1명의 궁수
    - 각각의 턴마다 궁수는 적 하나를 공격
    - 모든 궁수는 동시에 공격
    - 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적
    - 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적
    - 같은 적이 여러 궁수에게 공격 -> 턴 종료 시 한번에 처리
    - 공격받은 적은 게임에서 제외
- 적
    - 궁수의 공격이 끝나면, 적이 이동
    - 적은 아래로 한 칸 이동
    - 성이 있는 칸으로 이동한 경우에는 게임에서 제외
    - 모든 적이 격자판에서 제외되면 게임이 끝
두 위치의 거리는 |r1-r2| + |c1-c2|
0은 빈 칸, 1은 적이 있는 칸

[문제]
궁수의 공격으로 제거할 수 있는 적의 최대 수
'''
'''
[알고리즘]
- 궁수 배치 combinations()
- 적 있는지 확인 is_empty
    - while is_empty
        - attack()
        - move()
- attach
    - 궁수 좌표 3개 중 한개 선택
        - 전체 적 탐색하며 거리 계산
            - 적 거리가 사거리 D 이하면 대상 추가
        - 모든 탐색이 끝나고, 대상 중에 (거리 > 왼쪽 좌표) 정렬 후 idx 0만 공격 대상에 추가
    - 공격 대상 사망 처리
        - 중복 공격 고려한 사망 cnt 
'''
'''
[구조]
- arr 저장
- for combinations(range(M), 3)
    - tmp = arr.copy()
    - while not is_empty():  # 적이 있는 동안 계속 반복
        - cnt += attack(case)
        - move()
    - result = max(result, cnt)

- combinations(arr, r)

- is_empty(): 
    - sum(arr) > 0 # 적 있는지 확인

- attack():
    - for m_pose in case: # case = 좌표 3개
        - target = list()
        - for 전체 탐색
            - if 적 이면
                - 거리 계산
                - if 적 거리가 사거리 D 이하
                    - 대상 추가. (거리, x, y)
        - sorted(대상을 거리 가깝고 > 왼쪽 기준)
        - if 대상 있으면
            - 대상 중 첫번째를 제거 대상에 추가
    - for 제거 대상
        - 좌표만 받아옴
        - if 적이면 (반복 사망 처리 방지를 위해 한번더 확인)
            - 적 사망 처리
            - 사망 숫자 추가
    - return 사망 숫자

-  move(): 
    - for 아래에서 위로 역순
        - 적 아래로 좌표 이동
    - [0] * M 추가
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
        if tmp[i][j] == 1: # 반복 사망 처리 방지
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