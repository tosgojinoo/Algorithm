'''
[설명]
3×3×3개의 작은 정육면체
퍼즐을 풀려면 각 면에 있는 아홉 개의 작은 정육면체의 색이 동일
각 면을 양방향으로 90도 만큼 돌릴 수 있음
루빅스 큐브가 모두 풀린 상태에서 시작
윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색.
흰색은 w, 노란색은 y, 빨간색은 r, 오렌지색은 o, 초록색은 g, 파란색은 b.

[문제]
이때, 모두 돌린 다음에 가장 윗 면의 색상을 구하라
'''
'''
[알고리즘]
- 6면
    - idx 0 ~ 5. 리스트 구성.
    - [[], [], [], [], [], []]
    - 각 idx에 색 3개씩 3묶음 삽입. 3x3.
    - 순서는 무관. 편하게 한 면을 idx 0 기준으로 삼고, 순서대로 지정 및 기억.
- cmd 관리
    - (direction(면방향), cnt(+/-)) 쌍 묶음으로 저장
    - 구조
        - 앞에서 부터 하나씩 꺼내 사용. 모두 사용할 때까지 while.
        - while list:
            - a, b = list.pop(0)
    - cnt
        - '+' : 1번 회전
        - '-' : 3번 회전 (반대로 계산)
- 면 기준으로 +/- 90도 회전하면, 면 내부 위치변화(moveDimension) + 면 외부 위치변화(move)
- move()
    - direction 확인 (U, D, F, B, L, R)
    - 맞닿은 면 외부 이동 계산
    - moveDimension
    - 예)
        - 위 회전
            - 위: +/- 90도 배열 변경
            - 아래: 변화 없음
        - 앞, 뒤, 왼, 오른: (앞->오른, 오른->뒤, 뒤->왼, 왼->앞)
- moveDimension()
    - 면 내부 이동 계산
'''
'''
[구조]
- cmd 저장
- arr 구성
    - arr[면 idx][0~2][0~2]
- while cmd:
    - direction, cnt = cmd.pop(0)
    - cnt '+' -> 1, '-' -> 3
    - cnt 만큼 move(arr, direction)
- move()
    - 면 확인
    - 맞 닿은 면 이동
    - moveDimension()
- moveDimension()
    - 면 내 90도 이동 계산

'''
"""
    [0]  [4]  [5]
    RRR  BBB  OOO
    RRR  BBB  OOO
    RRR  BBB  OOO
    [1]
    YYY
    YYY
    YYY
    [2]
    WWW
    WWW
    WWW
    [3]
    GGG 
    GGG 
    GGG 
"""


def moveDimension(arr, index):
    for _ in range(2):
        temp = arr[index][0][0]
        arr[index][0][0] = arr[index][1][0]
        arr[index][1][0] = arr[index][2][0]
        arr[index][2][0] = arr[index][2][1]
        arr[index][2][1] = arr[index][2][2]
        arr[index][2][2] = arr[index][1][2]
        arr[index][1][2] = arr[index][0][2]
        arr[index][0][2] = arr[index][0][1]
        arr[index][0][1] = temp


def move(arr, direction):
    if direction == 'U':
        temp = arr[0][0]
        arr[0][0] = arr[4][0]
        arr[4][0] = arr[5][0]
        arr[5][0] = arr[3][0]
        arr[3][0] = temp
        moveDimension(arr, 2)

    elif direction == 'D':
        temp = arr[0][2]
        arr[0][2] = arr[3][2]
        arr[3][2] = arr[5][2]
        arr[5][2] = arr[4][2]
        arr[4][2] = temp
        moveDimension(arr, 1)

    elif direction == 'F':
        temp = arr[2][2]
        arr[2][2] = [arr[3][2][2],
                     arr[3][1][2],
                     arr[3][0][2]]
        arr[3][0][2], arr[3][1][2], arr[3][2][2] = arr[1][0]
        arr[1][0] = [arr[4][2][0],
                     arr[4][1][0],
                     arr[4][0][0]]
        arr[4][0][0], arr[4][1][0], arr[4][2][0] = temp
        moveDimension(arr, 0)

    elif direction == 'B':
        temp = arr[2][0]
        arr[2][0] = [arr[4][0][2],
                     arr[4][1][2],
                     arr[4][2][2]]
        arr[4][2][2], arr[4][1][2], arr[4][0][2] = arr[1][2]
        arr[1][2] = [arr[3][0][0],
                     arr[3][1][0],
                     arr[3][2][0]]
        arr[3][2][0], arr[3][1][0], arr[3][0][0] = temp
        moveDimension(arr, 5)

    elif direction == 'L':
        temp = [arr[0][0][0],
                arr[0][1][0],
                arr[0][2][0]]
        arr[0][0][0], arr[0][1][0], arr[0][2][0] = arr[2][0][0], arr[2][1][0], arr[2][2][0]
        arr[2][0][0], arr[2][1][0], arr[2][2][0] = arr[5][2][2], arr[5][1][2], arr[5][0][2]
        arr[5][0][2], arr[5][1][2], arr[5][2][2] = arr[1][2][0], arr[1][1][0], arr[1][0][0]
        arr[1][0][0], arr[1][1][0], arr[1][2][0] = temp
        moveDimension(arr, 3)

    elif direction == 'R':
        temp = [arr[0][0][2],
                arr[0][1][2],
                arr[0][2][2]]
        arr[0][0][2], arr[0][1][2], arr[0][2][2] = arr[1][0][2], arr[1][1][2], arr[1][2][2]
        arr[1][0][2], arr[1][1][2], arr[1][2][2] = arr[5][2][0], arr[5][1][0], arr[5][0][0]
        arr[5][0][0], arr[5][1][0], arr[5][2][0] = arr[2][2][2], arr[2][1][2], arr[2][0][2]
        arr[2][0][2], arr[2][1][2], arr[2][2][2] = temp
        moveDimension(arr, 4)

for _ in range(int(input())): # test case 수
    input() # 돌린 횟수 == cmd 개수. 생략 가능.
    cmd = list(map(str, input().split())) # 띄어쓰기로 구분하면, (direction, count) 한묶음이 됨.
    arr = [[] for _ in range(6)]
    for _ in range(3): # 초기화
        arr[0].append(['r', 'r', 'r'])
        arr[1].append(['y', 'y', 'y'])
        arr[2].append(['w', 'w', 'w'])
        arr[3].append(['g', 'g', 'g'])
        arr[4].append(['b', 'b', 'b'])
        arr[5].append(['o', 'o', 'o'])

    # 실행
    while cmd:
        direction, count = cmd.pop(0)
        if count == '+':
            count = 1
        else:
            count = 3 # '-' == '+' * 3
        for _ in range(count):
            move(arr, direction)

    # 출력
    for i in range(3):
        for j in range(3):
            print(arr[2][i][j], end="")
        print()