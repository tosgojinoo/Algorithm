'''
[설명]
가로 A, 세로 B.-> idx 1부터 시작. y(B)는 반대방향이므로, direction에서 남북을 반대로 적용.
로봇들이 N 개. M 개의 명령.
로봇 초기 위치. x 좌표 왼쪽부터, y 좌표 아래쪽부터 순서.
NWES 중 하나의 방향
로봇 수행 명령 -> 허용 방향 3가지 -> +-90전환을 위한 changedir 구성
1. L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
2. R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
3. F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.
잘못된 명령
1. Robot X crashes into the wall: X번 로봇이 벽에 충돌하는 경우이다. 즉, 주어진 땅의 밖으로 벗어나는 경우가 된다. -> 범위 밖 감지
2. Robot X crashes into robot Y: X번 로봇이 움직이다가 Y번 로봇에 충돌하는 경우이다. -> 복수개 로봇의 동일 위치 감지

[문제]
'''
'''
[알고리즘]
- arr 구성 x
    - 노드별 추적이기 때문에, 주위 정보 필요 없음
    - memory로 처리 가능
- 로봇별 위치 dict (memory)
    - robotInfo[idx] = [y, x, dirInfo[d]]
    - {로봇 idx: 위치 & 방향}
- 위치별 로봇 dict (memory)
    - posInfo[(y, x)] = idx
    - {위치 : 로봇 idx}
- 방향 정보
    - 숫자 전환용 dict
        - 'N': 0
    - direction 용 ㅣㅑㄴㅅ
- 허용 방향 3가지
    - +-90전환을 위한 changedir 구성
    - "L": (2, 3, 1, 0) | 0->2, 1->3, 2->1, 3->0
'''
'''
[구조]
- 초기값 입력
- memory 구성
    - robot_info dict
    - pos_info dict
- for M
    - moveRobot(idx, cmd, cnt)  # (로봇 번호, 명령어(L, R, F), 반복 횟수)
        - if 회전 명령
            - L 또는 R 방향으로 90도로 cnt번 회전
            - cnt %= 4 # 4로 나눈 나머지 만큼만 적용
            - changeDir -> ndirection 계산 -> robot_info에 저장
        - else 직진 명령
            - direction 방향으로 cnt 칸 만큼 이동
            - memory dict 의 해당값들을 삭제 -> 변경 -> 추가
            - 해당값 삭제
            - (변경) for cnt
                - if 범위 밖
                    - print("Robot", idx, "crashes into the wall")
                    - exit()
                - if 로봇 충돌
                    - print("Robot", idx, "crashes into robot", posInfo[(ny, nx)])
                    - exit()
            - 신규값 추가
'''

from sys import stdin

input = stdin.readline

# 상, 하, 좌, 우 = 0, 1, 2, 3
dy = (1, -1, 0, 0) # y축이 거꾸로 되어 있음을 반영.
dx = (0, 0, -1, 1)
dirInfo = {
    "N": 0,
    "S": 1,
    "W": 2,
    "E": 3
}
changeDir = {
    "L": (2, 3, 1, 0), # 0->2, 1->3, 2->1, 3->0
    "R": (3, 2, 0, 1), # 0->3, 1->2, 2->0, 3->1
}


# 로봇 이동 함수 - (번호, 명령어, 반복 횟수) 정보 인자로 받음
def moveRobot(idx, cmd, cnt):
    global robotInfo, posInfo
    y, x, direction = robotInfo[idx]  # 현재 로봇 위치, 방향

    # 회전 명령 - L 또는 R 방향으로 90도로 cnt번 회전
    if cmd in "LR":
        cnt %= 4  # 4번 돌면 제자리 이므로 4로 나눈 나머지를 취함
        for _ in range(cnt):
            direction = changeDir[cmd][direction]
        ndirection = direction
        robotInfo[idx][2] = ndirection  # 새로운 방향 등록

    # 직진 명령 - direction 방향으로 cnt 칸 만큼 이동
    else:
        # 위치 이동할 것이기 때문에, 삭제 -> 변경 -> 추가
        # 삭제
        del robotInfo[idx]  # 해당 로봇 정보 삭제
        del posInfo[(y, x)]  # 해당 위치 정보 삭제
        # 변경
        for _ in range(cnt):
            ny = y + dy[direction]
            nx = x + dx[direction]

            if not (0 <= ny < B and 0 <= nx < A):  # 격자 밖으로 나가면
                print("Robot", idx, "crashes into the wall")
                exit()

            elif (ny, nx) in posInfo.keys():  # 놓여 있는 로봇과 충돌
                print("Robot", idx, "crashes into robot", posInfo[(ny, nx)])
                exit()
            y, x = ny, nx
        # 추가
        robotInfo[idx] = [y, x, direction]  # 이동한 로봇 정보 새로 등록
        posInfo[(y, x)] = idx  # 이동한 위치 정보 새로 등록


# main
A, B = map(int, input().split()) # 가로 A, 세로 B. idx 1부터 시작.
N, M = map(int, input().split()) # 로봇들이 N 개. M 개의 명령.

robotInfo = dict()  # 로봇별 정보 저장
posInfo = dict()  # 위치별 정보 저장
for idx in range(1, N + 1):
    x, y, d = list(input().split()) # 로봇 초기 위치, 방향
    y = int(y) - 1 # (0,0) 기준 반영
    x = int(x) - 1
    robotInfo[idx] = [y, x, dirInfo[d]] # 로봇 번호 : (현재 로봇 위치, 방향) 정보 저장
    posInfo[(y, x)] = idx # 해당 위치에 현재 있는 로봇 번호 저장

for _ in range(M):
    idx, cmd, cnt = list(input().split()) # 로봇, 명령의 종류, 명령의 반복 회수
    moveRobot(int(idx), cmd, int(cnt))  # (로봇 번호, 명령어(L, R, F), 반복 횟수)

print("OK")