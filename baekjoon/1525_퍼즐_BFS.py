# ***** 0을 이동시킨다고 생각
# ***** visited = {배열 상태: cnt}

from collections import deque

# 퍼즐을 문자열 123456780로 정렬
arr = ""
for i in range(3):
    arr += "".join(list(input().split()))

visited = {arr: 0} # {배열 상태: cnt}
q = deque([arr])

# 상하좌우로 0(빈칸)을 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS():
    while q:
        arr = q.popleft()
        cnt = visited[arr]
        z_idx = arr.index('0')  # 0(빈칸)의 위치

        if arr == '123456780':
            return cnt

        x = z_idx // 3  # 2차원 배열로 변환
        y = z_idx % 3
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2 and 0 <= ny <= 2:  # 제한 조건: 범위 내
                # nx, ny를 다시 문자열의 index로 변환
                nz_idx = nx * 3 + ny
                arr_list = list(arr)  # 원소 스와핑을 위해 문자열을 리스트로 바꾸자
                arr_list[z_idx], arr_list[nz_idx] = arr_list[nz_idx], arr_list[z_idx]
                new_arr = "".join(arr_list)  # dict. key로 전환

                # 방문하지 않았다면
                if visited.get(new_arr, 0) == 0: # get: dict.에 key가 있을 경우 value, 없으면 0 출력
                    visited[new_arr] = cnt
                    q.append(new_arr)

    return -1


print(BFS())