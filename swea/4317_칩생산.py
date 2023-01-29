def is_valid(y, x):
    global wafer
    return 0 == wafer[y][x] == wafer[y][x+1] == wafer[y+1][x+1] == wafer[y+1][x]

def set_chip(y, x, value):
    global wafer
    wafer[y][x] = wafer[y][x+1] = wafer[y+1][x+1] = wafer[y+1][x] = value
    return

def dfs(y, x, num_of_chips):
    global answer, H, W, wafer, mem
    if y >= H-1:
        y, x = 0, x+1 

    if x == W-1:
        answer = max(answer, num_of_chips)
        return

    if y == 0:
        bit = sum(1<<i for i in range(H) if wafer[i][x] == 1)
        if mem[bit][x] >= num_of_chips: return
        mem[bit][x] = num_of_chips
    
    if is_valid(y, x):
        set_chip(y, x, 1)
        dfs(y+2, x, num_of_chips+1)
        set_chip(y, x, 0)
    dfs(y+1, x, num_of_chips)
    return
  
            
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    wafer = []
    for _ in range(H):
        wafer.append(list(map(int, input().split())))
    mem = [[-1] * W for _ in range(1 << H)]
    answer = 0
    dfs(0,0,0) # num_of_chips == level_now
    print(f"#{tc} {answer}")
