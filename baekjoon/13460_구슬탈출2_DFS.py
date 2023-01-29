# DFS, backtrack, bruteforce
# BFS 대비 시간 10~20배 정도

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def backtrack(inboard, inred, inblue, ind=0):
    global result, cnt, delta
    # if result == 1:
    #     return
    if ind == 10:
        return
    else:
        for i in range(4):
            tmp_board = [inboard[j][:] for j in range(N)]
            tmp_red = inred[:]
            tmp_blue = inblue[:]
            # direction 0:상,1:하, 2:좌, 3:우
            move_check = True
            while move_check:
                # 구슬 이동 없으면 break
                if tmp_red == [-1,-1] and tmp_blue == [-1,-1]:
                    break
                move_check = False
                rx, ry = tmp_red
                bx, by = tmp_blue
                drx = rx + delta[i][0]
                dry = ry + delta[i][1]
                dbx = bx + delta[i][0]
                dby = by + delta[i][1]
                # 벽, 구슬을 지나가면안됨
                # 구슬이 구멍에 닿으면 제거
                if tmp_board[drx][dry] == '.':
                    tmp_board[drx][dry] = 'R'
                    tmp_board[rx][ry] = '.'
                    tmp_red = [drx, dry]
                    move_check = True
                elif tmp_board[drx][dry] == 'O':
                    tmp_board[rx][ry] = '.'
                    tmp_red = [-1, -1]
                    move_check = True

                if tmp_board[dbx][dby] == '.':
                    tmp_board[dbx][dby] = 'B'
                    tmp_board[bx][by] = '.'
                    tmp_blue = [dbx, dby]
                    move_check = True
                elif tmp_board[dbx][dby] == 'O':
                    tmp_board[bx][by] = '.'
                    tmp_blue = [-1, -1]
                    move_check = True
            # if red만 없으면 return 1
            if tmp_red == [-1, -1] and tmp_blue != [-1, -1]:
                result = 1
                cnt = min(cnt, ind + 1)
            ####
            backtrack(tmp_board, tmp_red, tmp_blue, ind + 1)
    return


N, M = map(int, input().split())
# board 에서 구슬위치를 바꿔주어야하므로 list 나눠서 받음
board = []
red = [-1, -1]
blue = [-1, -1]
for i in range(N):
    tmp = list(input())
    board.append(tmp)
    for j in range(M):
        if tmp[j] == 'B':
            blue = [i, j]
        elif tmp[j] == 'R':
            red = [i, j]

result, cnt = 0, 10
backtrack(board, red, blue)
if result == 0:
    cnt = -1
print(cnt)