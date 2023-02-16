def is_valid(y, x):
    global arr
    return 0 == arr[y][x] == arr[y][x+1] == arr[y+1][x+1] == arr[y+1][x]

def set_chip(y, x, value):
    global arr
    arr[y][x] = arr[y][x+1] = arr[y+1][x+1] = arr[y+1][x] = value
    return

def DFS(y, x, num_of_chips):
    global answer, H, W, arr, mem
    # y가 행의 끝에 도착
    if y >= H-1: # 2칸 필요하기 때문에 1칸 이전으로 제한 걸림
        y, x = 0, x+1 # 다음 열로 검색 이동
    # x가 열의 끝에 도착
    if x == W-1: # 다음 열로 넘어 왔는데, 제한을 넘게 되면 종료.(2칸 확보)
        answer = max(answer, num_of_chips)
        return
    # y가 해당 열의 시작점에 위치. memory setting.
    if y == 0: # 첫행에서의 처리
        bit = sum(1<<i for i in range(H) if arr[i][x] == 1) # mem 영역 선정을 위한 bitmask 계산. 해당 열의 masking 상태에 대한 case 확인. bit 합으로 패턴 확인.
        if mem[bit][x] >= num_of_chips: # 이전 case 대비 cnt 적음. 무시.
            return
        mem[bit][x] = num_of_chips # cnt 클 경우 저장.
    # 나머지, 중간 영역. 가능.
    if is_valid(y, x): # 칩 생산 가능 여부 확인
        set_chip(y, x, 1) # 칩 영역에 1 처리. visited 효과.
        DFS(y+2, x, num_of_chips+1) # 2칸 아래로 이동 후 DFS
        set_chip(y, x, 0) # visited 되돌림.
    # 나머지, 중간 영역. 불가능.
    DFS(y+1, x, num_of_chips) # 다음 행으로 이동 후 DFS
    return
  
            
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = []
    for _ in range(H):
        arr.append(list(map(int, input().split())))
    mem = [[-1] * W for _ in range(1 << H)] # 2**H개 case(한 열 내 H개 점의 패턴 형태)과 각 열에 해당하는 cnt 값 저장.
    answer = 0
    DFS(0,0,0) # num_of_chips == level_now
    print(f"#{tc} {answer}")
