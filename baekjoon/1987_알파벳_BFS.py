# 조건:
# 1) 상하좌우로 인접한 네 칸 중의 한 칸으로
# 2) 이전과 다른 알파벳으로만 이동 가능

# 중요
# 1) queue를 set으로 설정하여 중복 제거하지 않으면 시간 초과(deque 불가)
# 2) memory를 list로 구성하면 시간 초과

# 조건은, 일단 분리해서 생각하고, 합칠수 있으면 나중에 합치기

# 시간: python3 > pypy3 (1/6)

def BFS():
    global result
    q = set([(0, 0, arr[0][0])]) # 시작: 좌측 상단 칸 (1행 1열)

    while q:
        y, x, memory = q.pop()
        result = max(result, len(memory))

        for i in range(4):
            ny, nx = y+dxy[i][0], x+dxy[i][1]
            if 0<=ny<R and 0<=nx<C and arr[ny][nx] not in memory:
                q.add((ny, nx, memory+arr[ny][nx]))


R, C = map(int, input().split()) # 세로 R칸, 가로 C (1 ≤ R,C ≤ 20)
arr = [list(input()) for _ in range(R)]
dxy = [(1,0), (-1,0), (0,1), (0,-1)]

result = 1
BFS()
print(result)
