'''
[설명]
지나갈 수 있는 길이 몇 개 있는지 -> checker (직선 탐색이므로 BFS/DFS 불필요)
- 탐색 조건
    - 길이란 한 행 또는 한 열 전부를 나타냄
    - 한쪽 끝에서 다른쪽 끝까지 지나가는 것
    - 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 함
    - 경사로를 놓아서 지나갈 수 있는 길 만들기
- 경사로 조건
    - 경사로는 높이가 항상 1이며, 길이는 L
    - 경사로는 낮은 칸과 높은 칸을 연결
    - 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접함
    - 낮은 칸과 높은 칸의 높이 차이는 1
    - 경사로를 놓을 낮은 칸의 높이는 모두 동일
    - L개의 칸이 연속
- 경사로 불가 조건
    - 경사로를 놓은 곳에 또 경사로를 놓는 경우 (겹쳐 놓기)
    - 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
    - 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우 (기울임, 바닥과 접하지 않음) -> buffer 변수로 누적 확인
    - 경사로를 놓다가 범위를 벗어나는 경우 -> 높이가 낮을 경우 경사로 놓기에 충분한 공간 확보 여부 판단 -> buffer에 빚(debt) 개념

[문제]
지나갈 수 있는 길의 개수 출력
'''
'''
[알고리즘]
- 행/열 방향 직선으로만 길 선택 가능
    - BFS/DFS 불필요
    - 직선으로 탐색
    - for 행/열 개수 만큼
        - 행방향 우선 check() -> 열방향 check()
    - check 통과 누적량 출력 
- check()
    - idx 0 pass
    - buffer: 동일 높이 구간 누적 cnt)
    - height: 이전 idx의 높이와 비교
    - 이전 idx와 높이 비교 결과에 따라, buffer 처리 or return 0(불가 판정)
    - 단, buffer에 잔여 빚이 있을 경우, 불가 판정. 경사로를 놓기 위해 필요한 공간을 충분히 확보하는데 실패.
'''
'''
[구조]
- arr 저장
- for 행 방향 in arr
    - 조건 만족하는 row_sum = check()

- for 열 방향 in zip(*arr)
    - 조건 만족하는 col_sum = check()
- check()
    - idx 0 pass
    - buffer: 동일 높이 구간 누적 cnt)
    - height: 이전 idx의 높이와 비교
    - 높이 비교
        - 이전과 동일
            - buffer ++
        - 이전보다 1 높음
            - buffer가 경사로 길이 L보다 크면, 통과. buffer 1로 초기화
        - 이전보다 1 낮음
            - buffer에 -L 만큼 빚 얹어주기. 전부 차감해야 통과. 아니면 불가 판정
'''


def check(lst):
    buffer = 1
    for idx, height in enumerate(lst):
        if idx == 0:
            continue
        if height == lst[idx-1]: # 바로 이전과 높이 동일
            buffer += 1
        elif height == lst[idx-1] + 1: # 이전 보다 높이 +1
            if buffer < L:
                return 0
            buffer = 1 # 경사로 놓고, 초기화
        elif height == lst[idx-1] - 1: # 이전 대비 높이 -1
            if buffer < 0: # 이 조건에 진입했을 땐, 이미 debt이 없는 상태여야함. 있다는 것은, 경사로 밑면이 충분히 확보되지 않았다는 것.
                return 0
            buffer = -L + 1 # 경사로 길이 만큼 debt
        else: # 높이차가 +/-1 초과하면, 아웃
            return 0

    if buffer < 0: # 잔여 debt 이 있을 경우, 아웃
        return 0

    return 1


# 크기 N (2 ≤ N ≤ 100)
# 경사로 길이 L (1 ≤ L ≤ N)
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

row_sum = 0
for lst in arr:
    row_sum += check(lst)

col_sum = 0
for lst in zip(*arr):
    col_sum += check(lst)
print(row_sum + col_sum)