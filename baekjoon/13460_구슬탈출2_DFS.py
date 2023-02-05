# DFS, backtrack, bruteforce
# BFS 대비 시간 10~20배 정도

def DFS(ry, rx, by, bx, cnt):
    global result # 빨간 구슬 들어 갔을 때 cnt 저장

    if result <= cnt: # 종료조건: 기울이 회수 cnt가 최소값 아닐 경우
        return

    if cnt > 10: # 종료조건: 기울인 회수 cnt가 10번 초과
        return

    # 4방향으로 기울이기
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        flag = 0
        rny, rnx = ry + dy, rx + dx
        bny, bnx = by + dy, bx + dx

        if arr[rny][rnx] != '#' or arr[bny][bnx] != '#':
            # 기울였을 때 빨간 구슬 위치
            rdist = 0
            for mv in range(1, N+M): # 갈수 있을 때까지 이동. 계산량 감소 위해 max() 아닌 단순 N+M합 사용
                rny, rnx = ry + mv*dy, rx + mv*dx

                if arr[rny][rnx] == '#':
                    break # 이동 종료
                elif arr[rny][rnx] == 'O':
                    flag = 1 # 빨간 구슬 들어감
                    break # 이동 종료
                elif rny == by and rnx == bx:
                    continue # 파란구슬의 시작위치와 겹치는 구간이 있다면, 이동 미반영. (마지막에 만나서 이동 1회 불가한 것을 반영한 효과)
                else:
                    rdist += 1
            rny, rnx = ry + rdist*dy, rx + rdist*dx # 이동 결과 한번에 반영

            # 기울였을 때 파란 구슬 위치
            bdist = 0
            for mv in range(1, N+M):
                bny, bnx = by + mv*dy, bx + mv*dx

                if arr[bny][bnx] == '#':
                    break # 이동 종료
                elif arr[bny][bnx] == 'O':
                    flag = 2 # 파란 구슬 들어감
                    break # 이동 종료
                elif flag==0 and bny == ry and bnx == rx: # 파란/빨간 구슬 모두 들어가지 않고, 빨간 구슬의 시작지점을 파란 구슬이 지나간다면 이동 거리 1회 누락 반영
                    continue # 이동 반영 없이
                else:
                    bdist += 1

            if flag == 2: # 파란 구슬이 들어간 경우 실패
                continue # 다음 방향

            if flag == 1: # 빨간 구슬만 들어간 경우 성공
                result = cnt
                return # DFS 종료
            bny, bnx = by + bdist*dy, bx + bdist*dx # 이동 결과 한번에 반영

            if ry == rny and rx == rnx and by == bny and bx == bnx: # 처음 위치와 동일하면 제외
                continue # 다음 방향
            DFS(rny, rnx, bny, bnx, cnt+1)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# R, B 위치 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ry, rx = i, j
        elif arr[i][j] == 'B':
            by, bx = i, j

result = 11
DFS(ry, rx, by, bx, 1)

print(result if result != 11 else -1)
