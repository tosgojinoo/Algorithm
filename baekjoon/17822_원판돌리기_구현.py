import sys
input = sys.stdin.readline

def rotate(x, d, k): # xi의 배수인 원판(2 ≤ xi ≤ N), di방향(0 ≤ di ≤ 1), ki칸 회전(1 ≤ ki < M)
    for i in range(x-1, N, x):
        idx_offset[i] += (1 if d else -1) * k # d==1 -> 반시계 - > 1 offset, d==0 -> 시계 -> -1 offset


def delete():
    del_list = []
    for circle_idx, circle in enumerate(arr): # circle_idx == 원판 idx
        for num_idx in range(M): # num_idx == 원판 위 숫자 idx
            if not circle[num_idx]: # 삭제된 숫자 제외
                continue
            nxt = (num_idx+1) % M # idx M -> 0 처리
            if circle[num_idx] == circle[nxt]: # 옆으로 인접 숫자, 동일할 경우
                del_list.append((circle_idx, num_idx))
                del_list.append((circle_idx, nxt))

    for circle_idx in range(N-1): # 원판 개수 N. 0~N-2까지, 마지막판 제외
        diff = idx_offset[circle_idx + 1] - idx_offset[circle_idx] # 회전 감안한 idx 적용을 위한 diff 계산
        for num_idx in range(M):
            if not arr[circle_idx][num_idx]: # 삭제된 숫자 제외
                continue
            nxt = (num_idx+diff) % M # idx M -> 0 처리
            if arr[circle_idx][num_idx] == arr[circle_idx+1][nxt]: # 위아래로 인접 숫자, 동일할 경우
                del_list.append((circle_idx, num_idx))
                del_list.append((circle_idx+1, nxt))

    for circle_idx, num_idx in del_list: # 인접하며, 같은 수 삭제
        arr[circle_idx][num_idx] = 0

    return len(del_list)


def update():
    cnt = N*M - sum((nums.count(0) for nums in arr)) # 초기 전체 숫자 개수 - 삭제되어 0이 된 숫자 개수
    if not cnt: # 차이 없으면 종료.
        return
    avg = sum(map(sum, arr)) / cnt # 남은 숫자 평균값
    for i in range(N):
        for j in range(M):
            b = arr[i][j]
            if not b:
                continue
            if b > avg: # 평균보다 큰 수에서 1을 빼고,
                arr[i][j] -= 1
            elif b < avg: # 작은 수에는 1을 더한다.
                arr[i][j] += 1


# init
N, M, T = map(int, input().split()) # 원판 1~N개, 원판 위 정수 M개, 회전 T번
arr = [list(map(int, input().split())) for _ in range(N)]
idx_offset = [0] * N # 원판 개수만큼 생성

# main
for _ in range(T):
    rotate(*map(int, input().split())) # xi의 배수인 원판(2 ≤ xi ≤ N), di방향(0 ≤ di ≤ 1), ki칸 회전(1 ≤ ki < M)
    if not delete(): # 삭제 된게 없으면.
        update()

print(sum(map(sum, arr)))
