# 1
'''
pipe_info = ((),
             ((0, 2), (1, 3)),
             ((0, 2), (1, 3)),
             ((2, 3), (3, 0), (0, 1), (1, 2)),
             ((2, 3), (3, 0), (0, 1), (1, 2)),
             ((2, 3), (3, 0), (0, 1), (1, 2)),
             ((2, 3), (3, 0), (0, 1), (1, 2))
             )
  
dir_list = (0, 1, 2, 3)
  
dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)
  
def bfs():
    global dij
    queue = [(0, 0, 1, 0, [])]
    while queue:
        r, c, cnt, dir_from, visit = queue.pop(0)
        c_pos = r*N+c
        if c_pos in visit: continue
        pipe = board[r][c]
        if not pipe: continue
        if cnt >= dij[dir_from][r][c]: continue
        if r == N-1 and c == N-1:
            for pipe_dir in pipe_info[pipe]:
                if (dir_from in pipe_dir) and (2 in pipe_dir):
                    dij[dir_from][r][c] = cnt
                    break
            continue
        dij[dir_from][r][c] = cnt
        visit = [*visit, c_pos]
        for pipe_dir in pipe_info[pipe]:
            if dir_from in pipe_dir:
                for p_dir in pipe_dir:
                    if p_dir == dir_from: continue
                    pr, pc = r+dr[p_dir], c+dc[p_dir]
                    if (0 <= pr <= N-1) and (0 <= pc <= N-1):
                        queue.append((pr, pc, cnt+1, dir_list[p_dir-2], visit))
  
  
def bfs2():
    global dij2
    queue = [(N-1, N-1, 1, 2, [])]
    while queue:
        r, c, cnt, dir_from, visit = queue.pop(0)
        c_pos = r*N+c
        if c_pos in visit: continue
        pipe = board[r][c]
        if not pipe: continue
        if cnt >= dij2[dir_from][r][c]: continue
        if r == 0 and c == 0:
            for pipe_dir in pipe_info[pipe]:
                if (dir_from in pipe_dir) and (0 in pipe_dir):
                    dij2[dir_from][r][c] = cnt
                    break
            continue
        dij2[dir_from][r][c] = cnt
        visit = [*visit, c_pos]
        for pipe_dir in pipe_info[pipe]:
            if dir_from in pipe_dir:
                for p_dir in pipe_dir:
                    if p_dir == dir_from: continue
                    pr, pc = r+dr[p_dir], c+dc[p_dir]
                    if (0 <= pr <= N-1) and (0 <= pc <= N-1):
                        queue.append((pr, pc, cnt+1, dir_list[p_dir-2], visit))
  
  
T = int(input())
switch = 1
for test_case in range(1, T+1):
    N = int(input())
    board = tuple(tuple(map(int,input().split())) for _ in range(N))
    dij = [[[float("Inf")]*N for _ in range(N)] for x in range(4)]
    bfs()
    ans = float("Inf")
    for i in range(4):
        if dij[i][N-1][N-1] < ans: ans = dij[i][N-1][N-1]
    dij2 = [[[float("Inf")]*N for _ in range(N)] for x in range(4)]
    bfs2()
    ans2 = float("Inf")
    for i in range(4):
        if dij2[i][0][0] < ans2: ans2 = dij2[i][0][0]
    print(f"#{test_case} {min([ans, ans2])}")

# 2
directs = [[0,1],[1,0],[0,-1],[-1,0]]
def solver(y,x,d,move,ey,ex):
    global answer
    # 도착점에 도착하면 min값 Update
    if [y,x] == [ey,ex]:        
        answer = min(answer,move-2)
        return   
    # move가 answer 보다 크면, or 이미 현재 위치에 최소 move가 있으면 or 파이프가 비었으면 break
    if (x < 0 or y < 0 or x > N+1 or y > N-1) or (move > answer) or (dvisit[d][y][x] < move) or (tmap[y][x] == 0) or (tvisit[y][x] == 1):
        return
    dy,dx = directs[d]
    pipe = tmap[y][x]
     
    dvisit[d][y][x] = move
    tvisit[y][x] = 1
    if pipe < 3:
        solver(y + dy,x + dx,d,move+1,ey,ex)
    else:
        for i in [1,-1]:
            nd = ( d + i + 4 )%4
            dy, dx = directs[nd]
            solver(y + dy,x + dx,nd,move+1,ey,ex)
    tvisit[y][x] = 0
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    answer = N*N
    tmap = [[0]+list(map(int,input().split()))+[0] for _ in range(N)]
    tmap[N-1][N+1] = 1
    tmap[0][0] = 1
    dvisit = [[[N*N]*(N+2) for _ in range(N)] for _ in range(4)]
    tvisit = [[0]*(N+2) for _ in range(N)]
    solver(N-1,N+1,2,1,0,0)
    tmp = answer
    dvisit = [[[N*N]*(N+2) for _ in range(N)] for _ in range(4)]
    tvisit = [[0]*(N+2) for _ in range(N)]
    solver(0,0,0,1,N-1,N+1)
    answer = min(tmp,answer)
    print("#%d %d"%(test_case,answer))
'''

# 3
def recur(point, endpoint, direction, move):
    global ans
    if point == endpoint:
        ans = min(ans, move-2)
        return
     
    if (point[1]<0 or point[0]<0 or point[0]>N-1 or point[1]>N+1)\
        or (ans < move) \
        or (mem[direction][point[0]][point[1]] < move) \
        or (visited[point[0]][point[1]]==1) \
        or (pipemap[point[0]][point[1]] == 0):
            return
     
    pipe = pipemap[point[0]][point[1]]
    mem[direction][point[0]][point[1]] = move
    visited[point[0]][point[1]] = 1
     
    if pipe < 3:
        dy, dx = directions[direction]
        recur((point[0]+dy, point[1]+dx), endpoint, direction, move+1)
 
    else:
        for i in [1, -1]:
            ndirection = (direction + i +4) % 4
            dy, dx = directions[ndirection]
            recur((point[0]+dy, point[1]+dx), endpoint, ndirection, move+1)
                             
    visited[point[0]][point[1]] =0
 
         
for tc in range(1, int(input())+1):
    directions = [(0,1), (1,0), (0,-1), (-1, 0)]
    N = int(input())
    ans = N*N
    pipemap = [[0]+list(map(int, input().split()))+[0] for _ in range(N)]
    pipemap[0][0], pipemap[N-1][N+1] = 1, 1
 
    visited = [[0]*(N+2) for _ in range(N)]
    mem = [[[N*N]*(N+2) for _ in range(N)] for _ in range(len(directions))]
    recur((0,0), (N-1, N+1), 0, 1)
    tmp = ans
     
    visited = [[0]*(N+2) for _ in range(N)]
    mem = [[[N*N]*(N+2) for _ in range(N)] for _ in range(len(directions))]
    recur((N-1, N+1), (0,0), 2, 1)
    ans = min(ans, tmp)
    print(f'#{tc} {ans}')
