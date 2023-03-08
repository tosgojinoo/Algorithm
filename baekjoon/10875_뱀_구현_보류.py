'''
[설명]
가로 길이와 세로 길이가 모두 2L + 1인 2차원 격자판
(x, y)로 표현
격자판의 가운데 칸의 좌표는 (0, 0)
맨 왼쪽 맨 아래 칸의 좌표는 (−L, −L)
맨 오른쪽 맨 위 칸의 좌표는 (L, L)
x좌표는 왼쪽에서 오른쪽으로 갈수록,
y좌표는 아래에서 위로 갈수록 증가
(0, 0) 칸에 한 마리의 뱀
처음에는 뱀의 크기가 격자판의 한 칸
뱀의 머리는 격자판의 오른쪽 -> 우/하/좌/상
1초에 한 칸씩 몸을 늘려나가며,
뱀의 머리는 그 방향의 칸으로 옮겨가게 된다.
1초가 지나고 나면 이 뱀은 몸을 한 칸 늘려서 (0, 0)과 (1, 0)의 두 칸을 차지 -> 계속 증가
(1, 0) 칸에 뱀의 머리
1초가 더 지나고 나면 (0, 0), (1, 0), (2, 0)의 세 칸을 차지
뱀의 머리는 (2, 0)
시계방향, 혹은 반시계방향으로 90도 회전 -> (d +/- 1) % 4
1번째 회전은 뱀이 출발한지 t1 초 후
i(i > 1)번째 회전은 i − 1번째 회전이 끝난 뒤 ti 초 후 -> t1 + ti
뱀은 ti 칸 만큼 몸을 늘린 후에 머리를 회전하며 머리를 회전하는 데에는 시간이 소요되지 않는다
만일 뱀의 머리가 격자판 밖으로 나가게 되면 -> 종료 조건
혹은 뱀의 머리가 자신의 몸에 부딪히게 되면 -> 종료 조건
뱀은 숨을 거두기 직전까지 몸을 계속 늘려나간다 -> 초당 1씩 증가
뱀이 머리를 회전하는 규칙, 즉 ti 와 그 방향에 대한 정보가 주어졌을 때 -> 입력 정보 commands
첫 번째 줄에 정수 L(1 ≤ L ≤ 108)
두 번째 줄에는 머리의 방향을 몇 번 회전할 것인지를 나타내는 정수 N(0 ≤ N ≤ 103)
다음 N 개의 줄에 뱀이 머리를 어떻게 회전하는지
i(1 ≤ i ≤ N)번째 줄에 정수 ti(1 ≤ ti ≤ 2 · 108)와 diri 가 차례로 주어지며
diri 는 문자 L, 또는 R 중 하나
뱀은 i = 1인 경우 출발,
그 외의 경우엔 i − 1번째 회전으로부터 ti 초 후에 diri 의 방향으로 머리를 회전
만일 diri 가 L 이라면 왼쪽 (반시계방향) -> if 'L'
R 이라면 오른쪽 (시계방향)으로 90도 회전 -> if 'R'


[문제]
뱀이 출발한지 몇 초 후에 숨을 거두는지
'''
'''
[알고리즘]
- arr
    - commmads가 별도 있고, 뱀의 성장 조건은 외부에 영향받지 않으며, arr에 뱀 외에는 없으므로 -> arr 미구성
    - 종료 조건용 외곽 제한 구역만 따로 관리
- vert/hori
    - 외곽 제한 관리용
    - (minX, maxX, y), (minY, maxY, x)
- dxy 제한
    - 우/하/좌/상
    - 오른쪽 시작, +/- 90도 회전
    
    
'''
'''
[구조]

'''



def solve():
    ans = 1
    flag = False # 충돌
    x, y, direction = L, L, 0 # 시작은 중앙, 오른쪽 방향. idx는 0부터 시작, 0에서 L번 이동이 중앙.
    for t, d in cmd:
        if direction % 2 == 0: # 수평 방향
            temp = float('inf')
            nx = x + dx[direction] * t
            minX, maxX = min(x, nx), max(x, nx) # x, nx 중 크고 작은 값 각각 저장
            for a, b, c in hori[:-1]: # (minY, maxY, x). [(0, N, -1), (0, N, N), (L, L, L)]
                if a <= y <= b and minX <= c <= maxX: # 크로스 여부 확인
                    flag = True
                    temp = min(abs(c - x) - 1, temp) # 충돌 전까지 이동 가능 거리
            if flag: # 충돌. 결과 출력
                return ans + temp
            else: # 충돌 x. 결과 누적.
                ans += t
                x = nx
                vert.append((minX, maxX, y)) # 직선의 위치(시작, 끝, 수평 위치) 저장
        else: # 수직 방향
            temp = float('inf')
            ny = y + dy[direction] * t
            minY, maxY = min(y, ny), max(y, ny)
            for a, b, c in vert[:-1]: # (minX, maxX, y). [(0, N, -1), (0, N, N)]
                if a <= x <= b and minY <= c <= maxY: # 크로스 여부 확인
                    flag = True
                    temp = min(abs(c - y) - 1, temp)
            if flag:
                return ans + temp
            else:
                ans += t
                y = ny
                hori.append((minY, maxY, x)) # 직선의 위치(시작, 끝, 수직 위치) 저장
        direction = (direction + d) % 4
    return ans

L = int(input())
N = 2 * L + 1 # 최대 폭
cmd = []
dirs = {'L':-1, 'R':1}
for _ in range(int(input())):
    t, d = input().split()
    cmd.append((int(t), dirs[d]))
cmd.append((N, 0))

vert = [(0, N, -1), (0, N, N)] # (minX, maxX, y)
hori = [(0, N, -1), (0, N, N), (L, L, L)] # (minY, maxY, x). (L, L, L) 은 무효값
dx = [1, 0, -1, 0] # 오, 하, 왼, 상
dy = [0, 1, 0, -1]

print(solve())