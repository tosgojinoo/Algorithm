import sys
input = sys.stdin.readline


def rotate_clock(arr):
    temp = arr[7]
    arr[1:] = arr[:-1] # 시계방향이므로 1칸씩 뒤로 이동
    arr[0] = temp

def rotate_ban_clock(arr):
    temp = arr[0]
    arr[:-1] = arr[1:] # 반시계방향이므로 1칸씩 앞으로 이동
    arr[7] = temp

def DFS(num, dir):
    global visited
    if not visited[num]:
        visited[num] = 1
        left = arr[num][6] # 9시 방향
        right = arr[num][2] # 3시 방향
        if dir == 1: # 시계 방향
            rotate_clock(arr[num])
        else:
            rotate_ban_clock(arr[num])
        if num-1 >= 0 and left != arr[num-1][2]: # 왼쪽 있는지 확인. 왼쪽 톱니의 3시 방향의 극 확인.
            DFS(num - 1, -dir) # 반대방향
        if num+1 <= 3 and right != arr[num+1][6]: # 오른쪽 있는지 확인. 오른쪽쪽 톱니의 9시 방향의 극 확인.
            DFS(num + 1, -dir) # 반대방향


arr = [list(input().rstrip()) for _ in range(4)] # 톱니배열
k = int(input()) # 회전 횟수
data = []

for _ in range(k):
    num, dir = map(int, input().split()) # 톱니바퀴 번호, 방향
    visited = [0] * 4
    DFS(num - 1, dir) # 톱니가 1부터 시작함.

cnt = 0
for i in range(4):
    if arr[i][0] == '1': # 12시방향의 극만 확인 후 점수 계산
        cnt += (2**i)
print(cnt)