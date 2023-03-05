import sys
input = sys.stdin.readline


def next_loc(route, idx, stride):
    loc = arr_idx[route][idx]
    # 루트 변경
    if loc in (5, 10, 15): # 파란색 화살표 지점
        return loc // 5, stride # route, nidx
    # 도착 지점
    nidx = idx + stride
    if nidx >= len(arr_idx[route]): # 종료지점 도착
        return -1, 0 # route, nidx
    # 다음 지점
    return route, nidx


def DFS(score, depth):
    global route, idx_list, loc_list, ans

    if depth == 10: # 10번 이동하면 종료
        ans = max(ans, score)
        return

    for horse_idx in range(min(depth+1, 4)): # 0~3회까지는 회차와 움직일 수 있는 horse가 동일. 이후부터는 4로 통일.
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


stride_list = list(map(int, input().split()))
arr_score = [2*i for i in range(21)] + [13, 16, 19] + [22, 24] + [28, 27, 26] + [25, 30, 35] # 게임판 score
route_list, idx_list, loc_list = [0] * 4, [0] * 4, [0] * 4 # visited_memory 구성
arr_idx = [
    [i for i in range(21)], # route 0
    [5, 21, 22, 23, 29, 30, 31, 20], # route 1
    [10, 24, 25, 29, 30, 31, 20], # route 2
    [15, 26, 27, 28, 29, 30, 31, 20] # route 3
] # 파란색 방향 감안한 루트

ans = 0
DFS(0, 0)
print(ans)
