# Brute Force
#   - blank_list에서 한개씩 1로 바꾸며, 모든 case에 대해 안전지대 계산 후 count_list에 저장
#   - max(count_list) 출력
# 최대 넓이 계산 -> BFS
from collections import deque

def BFS(replica): # 바이러스 전파시키는 BFS
    queue = deque()
    for virus in virus_list: # 초기 조건
        queue.append(virus)

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M: # 제한 조건
                continue

            if replica[nx][ny] == 0:
                queue.append((nx, ny))
                replica[nx][ny] = 2

    count = 0
    for r in replica: # 바이러스 전파 후 안전지대 카운팅
        count += r.count(0)
    return count


def make_wall():
    blank_length = len(blank_list)
    # blank_list에서 한개씩 1로 바꾸며, 모든 case에 대해 안전지대 계산
    for i in range(blank_length):
        for j in range(i + 1, blank_length):
            for k in range(j + 1, blank_length):
                replica = []
                for g in arr: # arr 복사본 생성
                    replica.append(g.copy())
                replica[blank_list[i][0]][blank_list[i][1]] = 1
                replica[blank_list[j][0]][blank_list[j][1]] = 1
                replica[blank_list[k][0]][blank_list[k][1]] = 1
                count_list.append(BFS(replica))

    return count_list


N, M = map(int, input().split())
arr = []
virus_list = [] # 바이러스
blank_list = [] # 빈칸
count_list = [] # 안전 지대

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 0:
            blank_list.append((i, j))
        elif arr[i][j] == 2: # virus
            virus_list.append((i, j))

make_wall()
print(max(count_list))