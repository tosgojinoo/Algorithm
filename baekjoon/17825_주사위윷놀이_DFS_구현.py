'''
[설명]
시작 칸에 말 4개 -> BFS or DFS -> 도착이 필수고, 최소가 아닌 최대값이므로, DFS
도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동 중지

- 이동
    - 게임판에 그려진 화살표의 방향대로만 이동
    - 말이 파란색 칸에서 이동을 시작. 파란색 화살표. -> arr_idx 관리. 파란색 방향 고려한 route 0~3 구성
    - 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작. 빨간색 화살표. -> 기본 route 0
        -> (visited memory 3단계) 필요. route idx, route 내 idx, arr 전체 기준 idx
- 턴
    - 10개의 턴
    - 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴림
    - 도착 칸에 있지 않은 말을 하나 골라, 주사위에 나온 수만큼 이동
    - 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없음
    - 이동을 마치는 칸이 도착 칸이면 고를 수 있음
    - 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가 -> arr_score 관리

[문제]
점수의 최댓값
'''
'''
[알고리즘]
- arr_idx
    - 지점을 특정할 수 있는 arr 구성해야함
    - 처음부터 끝까지 파란색 간선 제외하고 갈 경우. route 0 == list(range(21)). 
    - 시작 포함 총 21개 노드. 게임판 score와 다름.
    - route 1~3은 파란색으로 빠져 진행할 경우 노드 배열.
    - arr_idx = [[route 0], [route 1], [route 2], [route 3]]
    - DFS 때문에, 2차원 arr이므로, 루트 가리키는 r_idx, 루트 내 위치 가리키는 c_idx, 전체 맵 기준 idx 관리 필요. (visited memory 3단계)
- arr_score
    - arr_idx의 순서에 따른 값을 idx로 갖는 score 저장 리스트 구성 
- visited_memory
    - 말과 idx를 공유함
    - 각각 [0] * 4
    - route_list, idx_list, loc_list # 말 개별, 선택 루트 idx. 루트 내 idx. 전체 맵 내 idx. (visited memory 3단계)
    - (visited memory 3단계) 를 통해 DFS 전후 세팅/원복.
- DFS
    - 말 선택 제한  
        - range(min(depth+1, 4))
        - 0~3회까지는 회차와 움직일 수 있는 horse 개수가 동일. 이후는 4로 통일.
    - DFS 전후로, route/colume/arr idx (visited memory 3단계)로 세팅/원복 필요.
'''
'''
[구조]
- arr_idx = [[route 0], [route 1], [route 2], [route 3]] 파란색 방향 감안한 루트
- arr_score = 게임판 score. arr_idx를 따름.
- route_list, idx_list, loc_list. visited_memory 구성.
- DFS(0, 0)

- DFS(score, depth):
    - if depth. 10번 이동:
        - max score 저장 및 종료
    - for range(min(depth+1, 4)) 말 선택: 
        - horse가 위치한 route 번호, 전체 맵 내 idx 번호.
        - if 도착한 말: (도착은 route_idx == 0-1) 무시
        - arr_idx[rt][idx] 위치 확인
        - next_loc(rt, idx, stride_list[depth]) 다음 위치 계산
        - 다음 위치 확인
        - if 다음 위치가 종료지점 아니고, 다른 말과 겹치면: 무시
        - visited memory 저장. route_list[horse_idx], idx_list[horse_idx], loc_list[horse_idx] = nrt, nidx, nloc
        - if 종점이면: 
            - 점수 추가 없이 DFS(score, depth+1) 
        - else 종점 아니면:
            - 점수 추가 후 DFS(score + arr_score[nloc], depth+1) 
        - visited memory 원복. route_list[horse_idx], idx_list[horse_idx], loc_list[horse_idx] = rt, idx, loc 
        
- next_loc(route, idx, stride):
    - arr 내 위치 idx 확인
    - if 파란색 화살표 지점: 
        - return loc // 5, stride # route, nidx. 루트 변경
    - if 현위치 + 주사위 == 종료지점:
        - return route == -1, nidx == 0
    - 아니면, return route_idx, idx_in_route 

'''


import sys
input = sys.stdin.readline


def next_loc(route, idx, stride):
    loc = arr_idx[route][idx]
    # 루트 변경
    if loc in (5, 10, 15): # 파란색 화살표 지점
        return loc // 5, stride # route, nidx
    # 종료 지점
    nidx = idx + stride
    if nidx >= len(arr_idx[route]): # 종료지점 도착
        return -1, 0 # route, nidx
    # 아니면, 다음 지점
    return route, nidx


def DFS(score, depth):
    global route, idx_list, loc_list, ans

    if depth == 10: # 10번 이동하면 종료
        ans = max(ans, score)
        return

    for horse_idx in range(min(depth+1, 4)): # 0~3회까지는 회차와 움직일 수 있는 horse 개수가 동일. 이후부터는 4로 통일.
        rt, idx = route_list[horse_idx], idx_list[horse_idx] # horse가 위치한 route 번호, 전체 맵 내 idx 번호.
        if rt == -1: # 도착한 말
            continue
        loc = arr_idx[rt][idx] # 위치 확인
        nrt, nidx = next_loc(rt, idx, stride_list[depth]) # 다음 위치 계산
        nloc = arr_idx[nrt][nidx] # 다음 위치
        if (nrt != -1) and (nloc in loc_list): # 종료지점 아니고, 다른 말과 겹치면.
            continue
        route_list[horse_idx], idx_list[horse_idx], loc_list[horse_idx] = nrt, nidx, nloc # visited memory 체크
        if nrt == -1: # 종점이면.
            DFS(score, depth+1) # 점수 추가 없이 진행
        else: # 종점 아니면.
            DFS(score + arr_score[nloc], depth+1) # 점수 추가 후 진행
        route_list[horse_idx], idx_list[horse_idx], loc_list[horse_idx] = rt, idx, loc # visited memory 원복


stride_list = list(map(int, input().split())) # 주사위로 이동하는 수 배열
route_list, idx_list, loc_list = [0] * 4, [0] * 4, [0] * 4 # visited_memory 구성
arr_idx = [
    [i for i in range(21)], # route 0
    [5, 21, 22, 23, 29, 30, 31, 20], # route 1
    [10, 24, 25, 29, 30, 31, 20], # route 2
    [15, 26, 27, 28, 29, 30, 31, 20] # route 3
] # 파란색 방향 감안한 루트
arr_score = [2*i for i in range(21)] + [13, 16, 19] + [22, 24] + [28, 27, 26] + [25, 30, 35] # 게임판 score

ans = 0
DFS(0, 0)
print(ans)
