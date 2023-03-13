'''
[설명]
반지름 1~N 원판이 크기가 작아지는 순으로 바닥에 놓여있음
원판의 중심 동일
원판의 반지름이 i는 i번째 원판
원판에는 M개의 정수
i번째 원판에 적힌 j번째 수의 위치는 (i, j)
- 수의 위치 규칙
    - (i, 1)은 (i, 2), (i, M)과 인접
    - (i, M)은 (i, M-1), (i, 1)과 인접
    - (i, j)는 (i, j-1), (i, j+1)과 인접 (2 ≤ j ≤ M-1) -> 인접 조건: 동일 원판의 양옆 순번
    - (1, j)는 (2, j)와 인접
    - (N, j)는 (N-1, j)와 인접
    - (i, j)는 (i-1, j), (i+1, j)와 인접 (2 ≤ i ≤ N-1) -> 인접 조건: 동일 순번의 위아래 원반
- 원판의 회전
    - 독립적. 단일 원판만 회전.
    - 원판을 회전시킬 때는 수의 위치를 기준
    - 회전시킨 후의 수의 위치는 회전시키기 전과 일치
    - i번째 회전할때 사용하는 변수는 xi, di, ki
    - 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전
    - di
        - 0인 경우는 시계 방향
        - 1인 경우는 반시계 방향
    - 수 find & delete
        - 수가 남아 있으면
            - 인접하면서 수가 같은 것을 모두 찾음
            - 수가 있는 경우
                - 원판에서 인접하면서 같은 수를 모두 제거
        - 없는 경우
            - 원판에 적힌 수의 평균
            - 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더함

[문제]
T번 회전시킨 후 원판에 적힌 수의 합
'''
'''
[알고리즘]
- idx_offset
    - 원판 개수만큼 생성
    - 선택된 원판 회전 후
    - 각 원판 별 숫자 비교시
    - 위치 값에 대한 offset을 따로 저장
    - 원판 값을 이동시키지 않고, idx shift 방식 적용
    - d==1 -> 반시계 - > 1 offset(1 앞의 것 참조), d==0 -> 시계 -> -1 offset(1 뒤의 것 참조)
- 인접 숫자 처리
    - 회전 감안하기
    - 옆 방향
        - (num_idx +1) % M
    - 위 방향
        - (num_idx+diff) % M
        - 원판별 회전 결과 적용한 idx_offset 리스트를 활용한 idx 차이 diff 계산 활용
'''
'''
[구조]
- arr 저장
- 원판 개수만큼 idx_offset 생성

- for T번 회전:
    - rotate((회전 대상 원판 배수, 방향, 회전칸))
    - if not_deleted 삭제 된게 없으면
        - update()

- rotate()
    for 배수 만큼 원판 idx 선정
        - d==1 -> 반시계 - > 1 offset, d==0 -> 시계 -> -1 offset

- delete()
    - 옆으로 인접 확인
    - for 원판 하나씩 선정
        - for 원판 위 숫자 하나씩 선정
            - if 삭제된 숫자 idx. 제외.
            - 다음 숫자 idx 선정. 단, 회전 감안해 (num_idx+1) % M 
            - if 옆으로 인접 숫자와 동일할 경우
                - del_list에 추가 (circle_idx, num_idx)
                - del_list에 추가 (circle_idx, nxt)
    
    - 위로 인접 확인
    - for 원판 하나씩 선정. 0~N-2까지, 마지막판 제외.
        - diff = 기준 원판과 다음 원판의 idx offset(shift) 차이
        - for 원판 내 숫자:
            - if 삭제된 숫자 idx. 제외.
            - 다음 원판 idx 선정. 단, 회전 감안해 (num_idx+diff) % M
            - if 위아래로 인접 숫자와 동일할 경우
                - del_list에 추가 (circle_idx, num_idx)
                - del_list에 추가 (circle_idx+1, nxt)

    - for del_list: 삭제
    
    - return 삭제된 숫자 개수


- update():
    - cnt = 초기 전체 숫자 개수 - 삭제되어 0이 된 숫자 개수
    - if 차이 없음: 종료.
    - avg = 남은 숫자 평균값
    - for 원판 순서대로
        for 숫자 순서대로
            if 0 이면: 무시.
            if 평균보다 크면: 1 --
            elif 평균보다 작으면: 1 ++
'''


import sys
input = sys.stdin.readline

def rotate(x, d, k): # xi의 배수인 원판(2 ≤ xi ≤ N), di방향(0 ≤ di ≤ 1), ki칸 회전(1 ≤ ki < M)
    for idx in range(x-1, N, x):
        idx_offset[idx] += (1 if d else -1) * k # d==1 -> 반시계 - > 1 offset, d==0 -> 시계 -> -1 offset


def delete():
    del_list = []
    for circle_idx, circle in enumerate(arr): # circle_idx == 원판 idx
        for num_idx in range(M): # num_idx == 원판 위 숫자 idx
            if not circle[num_idx]: # 삭제된 숫자 제외
                continue
            nxt = (num_idx+1) % M # idx M -> 0 처리
            if circle[num_idx] == circle[nxt]: # 옆으로 인접 숫자, 동일할 경우
                del_list.append((circle_idx, num_idx))
                del_list.append((circle_idx, nxt))

    for circle_idx in range(N-1): # 원판 개수 N. 0~N-2까지, 마지막판 제외
        diff = idx_offset[circle_idx + 1] - idx_offset[circle_idx] # 회전 감안한 idx 적용을 위한 diff 계산
        for num_idx in range(M):
            if not arr[circle_idx][num_idx]: # 삭제된 숫자 제외
                continue
            nxt = (num_idx+diff) % M # idx M -> 0 처리
            if arr[circle_idx][num_idx] == arr[circle_idx+1][nxt]: # 위아래로 인접 숫자, 동일할 경우
                del_list.append((circle_idx, num_idx))
                del_list.append((circle_idx+1, nxt))

    for circle_idx, num_idx in del_list: # 인접하며, 같은 수 삭제
        arr[circle_idx][num_idx] = 0

    return len(del_list)


def update():
    cnt = N*M - sum((nums.count(0) for nums in arr)) # 초기 전체 숫자 개수 - 삭제되어 0이 된 숫자 개수
    if not cnt: # 차이 없으면 종료.
        return
    avg = sum(map(sum, arr)) / cnt # 남은 숫자 평균값
    for circle_idx in range(N):
        for num_idx in range(M):
            num = arr[circle_idx][num_idx]
            if not num: # 0 이면 무시
                continue
            if num > avg: # 평균보다 큰 수에서 1을 빼고,
                arr[circle_idx][num_idx] -= 1
            elif num < avg: # 작은 수에는 1을 더한다.
                arr[circle_idx][num_idx] += 1


# init
N, M, T = map(int, input().split()) # 원판 1~N개, 원판 위 정수 M개, 회전 T번
arr = [list(map(int, input().split())) for _ in range(N)]
idx_offset = [0] * N # 원판 개수만큼 생성

# main
for _ in range(T):
    rotate(*map(int, input().split())) # xi의 배수인 원판(2 ≤ xi ≤ N), di방향(0 ≤ di ≤ 1), ki칸 회전(1 ≤ ki < M)
    if not delete(): # 삭제 된게 없으면.
        update()

print(sum(map(sum, arr)))
