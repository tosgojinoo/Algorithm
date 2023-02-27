'''
- 스마튼폰에 원하는 숫자 입력
- 어느 부분 터치 안됨
- 원하는 숫자를 직접 입력할 수 없는 경우 있음
- 계산기 -> 입력 가능한 숫자 입력 -> 연산 -> 원하는 숫자 생성
- 복사 붙이기
- 최소 터치 횟수 프로그램
- 계산 범위 0 ~ 999
- 계산 도중 음수 or 999 넘으면 에러
- 두자리 숫자는 연속해서 숫자 터치
- 연산은 순차적으로
- 나누기는 소수 이하 버림, 정수만 남김
- 0으로 나누기 안됨
- 0 ~ 9 까지 입력 가능
- 연산자 ‘+’, ‘-‘, ‘*’, ‘/’ 입력 가능
  => 1, 2, 3, 4
- '=' 항상 입력 가능
- 연산 결과 전 항상 '=' 입력, 원하는 수 직접 입력 가능시 불필요
- M을 넘을 경우 -1 출력

# [main]
1. T = total case
2. N, O, M = input()
    - 터치 가능한 숫자들 개수 N, 1 <= N <= 10
    - 터치 가능한 연산자들 개수 O, 1 <= O <= 4
    - 터치 가능 최대 횟수 M, 4<= M <= 20
3. can_touch = input()
    - 터치 가능한 숫자들
4. operators = input()
    - 터치 가능한 연산자들
5. W = input()
    - 원하는 숫자 W
6. touch_list = []
7. 숫자&연산자 조합 생성
    - comb('')
8. visited 생성
    - visited = [M]*1000
    - 모든 결과값의 경우의 수를 열거 (0~999)
    - 해당 index에 최대 입력 가능 횟수 M을 초기 세팅
    - index를 계산값으로 가질 경우 현재 입력 횟수와 이미 저장된 입력 횟수를 비교하여, 작을 경우만 추가 DFS
    - 동일 값에서 현재 계산 상태의 입력 횟수가 이전 보다 클 경우 진전의 의미가 없음(boundary condition)
9. result 생성
    - result = 21
    - 최대 입력이 20 이므로
10. for, 생성된 조합 touch_list 에서 하나씩 꺼내며 루프
    1) DFS(num, len(num))
11. result가 21이면 실패, result = -1

# [comb]
- comb(num)
- can_touch 로 입력 받은 숫자들의 조합
- 중복, 제한 개수(여기서는 3) 이하 전부 추출
1. if, 총 길이(len(num))가 3일 경우 종료
2. for, can_touch 개수만큼 루프
    1) touch_list에 (num+str(can_touch[i])) 추가
        - 이전 조합 + 이번에 추가하는 숫자
    2) if, 1)에서 추가한 것이 '0'이 아닐 경우
        - '0' 일 경우 이어짐 없이 종료

# [calc]
- calc(op, n1, n2, cnt)
- operator, 숫자 앞뒤 2개 받아 계산
1. 추가된 숫자 n2의 길이 + 1(operator 길이)을 현재 cnt에 추가
2. if, 각 operator 숫자에 따라 계산
3. return 계산 결과, cnt

# [dfs]
- dfs(num, cnt) # num
1. global result
2. if, int(num) 이 원하는 숫자 W 면
    1-1) if, num이 touch_list에 있으면
        a. result = min(result, cnt)
    1-2) 아니면, result = min(result, cnt+1)
    2) return
3. for, touch_list에서 num을 하나씩 빼서 루프
    1) if, num == '0' 이면 다음 루프
        - continue
    2) for, operators에서 하나씩 빼서 루프
        a. 연산
            - new_num, new_cnt = calc(choice_o, num, choice_num, cnt)
        b. if, 제한조건
            - 0 <= new_num <= 999 and
            - new_cnt < M and
            - new_cnt < result and
            - new_cnt < visited[new_num]
            a) visited에 new_cnt 저장
                - visited[new_num] = new_cnt
            b) DFS(str(new_num), new_cnt)
'''

def r_combination(num):
    if len(num) == R:
        return
    for nxt in can_touch:
        touch_list.append(num + str(nxt))
        if num + str(nxt) != '0': # 첫 선택이 0이 아닐 경우만
            r_combination(num + str(nxt))


def calc(op, n1, n2, cnt):
    cnt += len(n2) + 1
    if op == 1:
        return int(n1) + int(n2), cnt
    if op == 2:
        return int(n1) - int(n2), cnt
    if op == 3:
        return int(n1) * int(n2), cnt
    if op == 4:
        return int(n1) // int(n2), cnt


def DFS(num, cnt):
    global result

    if int(num) == W:
        if num in touch_list:
            result = min(result, cnt) # DFS 진입하자 마자 바로인 case
        else:
            result = min(result, cnt + 1) # '=' 추가 cnt
        return

    for choice_num in touch_list: # 루프 횟수 줄이기 위해 op 아닌 num 부터 선택
        if choice_num != '0':
            for choice_op in operators:
                nnum, ncnt = calc(choice_op, num, choice_num, cnt)
                if 0 <= nnum <= 999 and ncnt < M and ncnt < result and ncnt < visited[nnum]: # 숫자 범위 제한, 입력 cnt 제한, 이전 cnt 대비 작음, 동일 숫자의 이전 cnt 대비 작음
                    visited[nnum] = ncnt
                    DFS(str(nnum), ncnt)


T = int(input())
for test_case in range(1, T + 1):
    N, O, M = map(int, input().split()) # 터치 가능한 숫자 개수, 터치 가능한 연산자 개수, 터치 가능 회수

    can_touch = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input()) # 원하는 숫자

    touch_list = []
    R = 3 # 최대 3자리 숫자
    r_combination('') # touch_list에 case 저장

    visited = [M] * 1000 # idx: W의 대상, M: 누적 터치 cnt 저장을 위한 초기값
    result = 21 # 터치 최대 횟수 제한. 문제상 M의 조건.
    for num in touch_list:
        DFS(num, len(num)) # num, cnt

    if result == 21:
        result = -1

    print('#%d %d' % (test_case, result))
