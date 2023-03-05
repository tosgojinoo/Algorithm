# def moveRobot()
#   - L, R, F 처리
#   - 처리 후 위치와 문제 발생 여부 반환

# *** 반복 횟수에 따른 방향 처리
# 반복 횟수가 짝수인 경우 L/R은 방향 동일 => case 통일
# 반복 횟수가 홀수인 경우 L/R은 서로 반대 방향 => case 분리

# arr 생성. 로봇 위치에 idx 기록. => arr 맵 사용 대신, posInfo dict.
# direction = N 배열. memory. 현재 방향 저장 -> x => robotInfo 에 {로봇 idx: 위치 & 방향} 저장
# commands = N 배열. set & append로 구성. -> x => posInfo 에 {위치 : 로봇 idx} 저장

from sys import stdin

input = stdin.readline

# 상, 하, 좌, 우 = 0, 1, 2, 3
dy = (-1, 1, 0, 0)
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
        cnt %= 4  # 4번 돌면 제자리이므로 4로 나눈 나머지를 취함
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

            elif (ny, nx) in posInfo.keys():  # 놓여있는 로봇과 충돌하면
                print("Robot", idx, "crashes into robot", posInfo[(ny, nx)])
                exit()
            y, x = ny, nx
        # 추가
        robotInfo[idx] = [y, x, direction]  # 이동한 로봇 정보 새로 등록
        posInfo[(y, x)] = idx  # 이동한 위치 정보 새로 등록


# main
A, B = map(int, input().split())
N, M = map(int, input().split())

robotInfo = dict()  # 로봇별 정보 저장
posInfo = dict()  # 위치별 정보 저장
for idx in range(1, N + 1):
    x, y, d = list(input().split())
    y = B - int(y) # y는 반대로 적용
    x = int(x) - 1 # (0,0) 기준 반영
    robotInfo[idx] = [y, x, dirInfo[d]]  # 로봇 번호 : (현재 로봇 위치, 방향) 정보 저장
    posInfo[(y, x)] = idx  # 해당 위치에 현재 있는 로봇 번호 저장

for _ in range(M):
    idx, cmd, cnt = list(input().split())
    moveRobot(int(idx), cmd, int(cnt))  # (로봇 번호, 명령어(L, R, F), 반복 횟수)

print("OK")