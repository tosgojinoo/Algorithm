'''
[설명]
N×M
(r, c)는 r행 c열
- 배열 A의 값: 각 행에 있는 모든 수의 합 중 최솟값
- 회전 연산
    - 세 정수 (r, c, s)
    - 정사각형을 시계 방향으로 한 칸씩 돌림
        - 가장 왼쪽 윗 칸이 (r-s, c-s)
        - 가장 오른쪽 아랫 칸이 (r+s, c+s)
    - 회전 연산이 두 개 이상이면, 연산을 수행한 순서에 따라 최종 배열이 다름

[문제]
배열 A의 값의 최솟값
회전 연산은 모두 한 번씩 사용해야 하며,
순서는 임의 -> 순열 permutation

'''
'''
[알고리즘]
- 경우의 수
    - 임의 순서 & 순서에 따른 결과 다름
    - 순열 permutation 적용
- 회전 (반시계 방향)
    - 회전 중심점 찾기
    - radius 값 설정
    - 왼쪽 상단점 계산 (회전 중심 r/c - radius)
    - 왼쪽 상단점 -> tmp 저장
    - 좌 > 하 > 우 > 상 순서대로 이동 처리
    - 해당 변의 시작지점 ~ 끝지점까지 한칸씩 이동 반복
    - dr++ > dc++ > dr-- > dc--  
'''
'''
[구조]
- arr_init 숫자 정보
- rcs = [(회전 연산의 정보 r, c, s)] # 회전 중심 (r,c), 이격 거리 s

- for permutation(rcs, 회전 연산 수 K):
    - arr = arr 복사

    - for 회전 연산수 K:
        - 조합 중 (r, c, s) 하나 선택
        - arr = rotate(arr, r, c, s)

    # 3. 각 행의 최소값 찾기
    result = min(result, evaluate(arr))

- print(result)

- permutation(arr, r):

- rotate(arr, r, c, s):
    - for radius in range(1, s + 1):
        - i/j = r/c - radius
        - tmp = arr[i][j] # 왼쪽 위 시작점
        
        # 왼쪽 맨 위부터 회전. (i, j) 번갈아가며 증가.
        # 왼쪽
        # (i,j) == 왼쪽 맨 위
        - while i < r + radius: 행 i = (r-radius ~ r+radius) 
            - arr[i][j] = arr[i + 1][j]
            - i += 1

        # 아래
        # (i,j) == 왼쪽 맨 아래
        - while j < c + radius: 열 j = (c-radius ~ c+radius) 
            - arr[i][j] = arr[i][j + 1]
            - j += 1

        # 오른쪽
        # (i,j) == 오른쪽 맨 아래
        - while i > r - radius: 행 i = (r+radius ~ r-radius) 
            - arr[i][j] = arr[i - 1][j]
            - i -= 1

        # 위
        # (i,j) == 오른쪽 맨 위
        - while j > c - radius: 열 j = (c+radius ~ c-radius) 
            - arr[i][j] = arr[i][j - 1]
            - j -= 1

        - arr[i][j + 1] = tmp

    - return arr

- evaluate(arr):
    - row_sums = 행별 합산
    - return min(row_sums)

'''

def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nxt in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + nxt

def rotate(arr, r, c, s):
    r = r - 1
    c = c - 1

    for radius in range(1, s + 1):
        i = r - radius
        j = c - radius
        tmp = arr[i][j] # 사작점

        # Left side
        while i < r + radius:
            arr[i][j] = arr[i + 1][j]
            i += 1

        # Lower side
        while j < c + radius:
            arr[i][j] = arr[i][j + 1]
            j += 1

        # Right side
        while i > r - radius:
            arr[i][j] = arr[i - 1][j]
            i -= 1

        # Upper side
        while j > c - radius:
            arr[i][j] = arr[i][j - 1]
            j -= 1

        arr[i][j + 1] = tmp

    return arr

def evaluate(arr):
    row_sums = [sum(row) for row in arr]
    return min(row_sums)


N, M, K = map(int, input().split()) # 배열 A의 크기 N, M, 회전 연산의 개수 K
arr_init = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)] # 회전 연산의 정보 r, c, s

result = 1e9

# 1. 회전 순서 정하기 (최대 6!=720)
for case in permutation(rcs, K):
    # 2. 회전
    arr = [arr_init[i][:] for i in range(N)] # 복사

    for i in range(K):
        r, c, s = case[i]
        arr = rotate(arr, r, c, s)

    # 3. 각 행의 최소값 찾기
    result = min(result, evaluate(arr))

print(result)