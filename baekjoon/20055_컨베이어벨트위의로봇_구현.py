'''
로봇 업데이트는 idx 역순으로 해야함.
arr[idx] 내구도가 0일 경우 로봇이 못 올라가므로, 하나씩 해야함.
'''

n, k = map(int, input().split()) # 컨베이어 칸수 N, 내구도 0 제한 칸수 K
arr = list(map(int, input().split())) # 내구도
robot = [0]*n
step = 0
cnt = 0

while cnt < k: # 제한 칸수 이하일 때까지
    step += 1
    # rotateBelt()
    arr[1:], arr[0] = arr[0:-1], arr[-1]
    robot[1:], robot[0] = robot[0:-1], 0

    # unrideRobot()
    robot[-1] = 0 # 마지막 컨베이어 로봇 제거.
    # moveRobot()
    for i in range(n - 1, -1, -1):
        if i < n - 1 and robot[i]: # 마지막 이전까지 컨베이어. 로봇 있다면.
            if not robot[i + 1] and arr[i + 1]: # 로봇이 없고, 내구도 남음.
                robot[i], robot[i + 1] = 0, 1 # 이동
                arr[i + 1] -= 1 # 내구도 감소
                if not arr[i + 1]: # 내구도 0이면.
                    cnt += 1

    # rideRobot()
    if arr[0]: # 내구도 남아 있으면
        robot[0] = 1 # 첫 컨테이너에 올릴 신규 로봇
        arr[0] -= 1 # 내구도 감소
        if not arr[0]: # 내구도 0
            cnt += 1

print(step)

