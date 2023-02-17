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
    cnt += len(n2) + 1 # op cnt + n2 cnt
    if op == 1: return int(n1) + int(n2), cnt
    if op == 2: return int(n1) - int(n2), cnt
    if op == 3: return int(n1) * int(n2), cnt
    if op == 4: return int(n1) // int(n2), cnt


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




'''
# backtracking
INF = 10 ** 9
def solution(N, O, M, digits, operators, W):
    """ 솔루션
 
    :param N:         숫자 수
    :param O:         연산 수
    :param M:         최대 터치 수
    :param digits:    숫자 목록
    :param operators: 연산 목록
    :param W:         대상 수
    :return: 최소 터치 수
    """
    # 숫자 도달 터치 수 초기화
    num_touchs = [INF] * 1000
 
    # 연산 없이 가능한 수 설정
    nums = list()
    q    = list(digits)
 
    while len(q) > 0:
        curr_num = q.pop(0)
 
        num_touchs[curr_num] = len(str(curr_num))
        nums.append(curr_num)
 
        if curr_num > 0:
            for d in digits:
                next_num = curr_num * 10 + d
 
                if 0 <= next_num < 1000:
                    q.append(next_num)
 
    # 연산 없이 숫자 입력으로 가능하다면 반환
    if num_touchs[W] != INF:
        return num_touchs[W]
 
    # 백트래킹
    queue = list(nums)
 
    while len(queue) > 0:
        #
        curr_num = queue.pop(0)
 
        if curr_num == W:
            break
 
        #
        for n in nums:
            next_touch = num_touchs[curr_num] + 1 + num_touchs[n]
 
            if next_touch < M:
                for o in operators:
                    if   o == 1:
                        next_num = curr_num +  n
                    elif o == 2:
                        next_num = curr_num -  n
                    elif o == 3:
                        next_num = curr_num *  n
                    elif o == 4 and n != 0:
                        next_num = curr_num // n
                    else:
                        next_num = -1
 
                    if 0 <= next_num < 1000:
                        if next_touch < num_touchs[next_num]:
                            num_touchs[next_num] = next_touch
 
                            queue.append(next_num)
 
    #
    if num_touchs[W] == INF:
        return -1
 
    return num_touchs[W] + 1
 
 
T = int(input())

for t in range(1, T + 1):
    N, O, M   = map(int, input().split())
    digits    = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W         = int(input())

    sol = solution(N, O, M, digits, operators, W)

    print('#' + str(t) + ' ' + str(sol))
 



# recur 0
def calc(num, num2, oper):  # 하나의 연산자를 이용한 계산 하나
    if oper == 1:  # 덧셈
        num += num2
    elif oper == 2:  # 뺄셈
        num -= num2
    elif oper == 3:  # 곱셈
        num *= num2
    else:  # 나눗셈
        if num2 == 0:  # 나눌 수 없는 경우
            return -1
        num //= num2
    if 0 <= num < 1000:  # 세자리까지 가능(음수 X)
        return num
    else:  # 범위를 넘어서는 경우
        return -1
 
 
def recur(cur, x):  # 숫자버튼으로 만들 수 있는 수(세 자리 이하)
    if cur == 3:
        return
    for num in num_keys:
        nxt_num = x * 10 + num
        if visited[nxt_num] <= cur + 1:  # 0으로 시작하는 경우를 처리!
            continue
        visited[nxt_num] = cur + 1  # 클릭 횟수를 배열에 담는다.
        que.append(nxt_num)  # 큐에 담는다.
        nums.append(nxt_num)  # 숫자들을 담아준다.
        recur(cur + 1, nxt_num)
 
 
t = int(input())
for tc in range(1, t + 1):
    n, o, m = map(
        int, input().split()
    )  # n: 터치가능한 숫자들의 개수, o: 터치가능한 연산자들의 개수, m: 최대 터치 횟수
    num_keys = list(map(int, input().split()))  # 사용 가능한 숫자들 0 ~ 9
    opers = list(map(int, input().split()))  # 사용 가능한 연산자들 +는 1, -는 2, *은 3, /는 4
    nums = []
    w = int(input())  # 원하는 출력 값
    INF = m + 1  # m은 최대 20이니 더 큰 값을 넣어준다.
    visited = [INF for _ in range(1000)]
    que = []
    recur(0, 0)  # 숫자로만 구성할 수 있는 세자리 이하 수들을 담아준다.
 
    if visited[w] < INF:  # 숫자로만 구성할 수 있으면 출력하고 종료
        print(f"#{tc} {visited[w]}")
        continue
 
    while que:
        v = que.pop(0)
        for num in nums:
            click_cnt = visited[v] + len(str(num)) + 1
            if click_cnt + 1 > m:  # 클릭 횟수가 m을 초과한 경우('='하나 포함)
                continue
            for oper in opers:
                nxt = calc(v, num, oper)
                if nxt == -1:  # 예외사항 처리
                    continue
                if visited[nxt] <= click_cnt:  # 클릭 횟수가 같거나 커지면 패스
                    continue
                visited[nxt] = click_cnt  # 클릭 횟수가 더 작으면 업데이트
                que.append(nxt)
 
    if visited[w] < INF:  # 숫자로만 구성할 수 있으면 출력하고 종료
        print(f"#{tc} {visited[w] + 1}")  # '='도 누르는 횟수 포함
    else:
        print(f"#{tc} -1")


# recur 1
def cal(num1, num2, op):
    if op == '1':
        return num1 + num2
    elif op == '2':
        return num1 - num2
    elif op == '3':
        return num1 * num2
    elif op == '4':
        return num1 // num2
    return -1
 
def solve(cur, cnt, eq):
    global ans
    if not (0 <= cur < 1000): return
    if memo[cur] <= cnt: return
    memo[cur] = cnt
    if cnt + eq >= ans: return
    if cur == W: ans = cnt + eq
    for l, num in num_list:
        for op in ops:
            solve(cal(cur, num, op), cnt + l + 1, 1)
 
 
def create(nums):
    num_list = []
    for i in nums:
        if i == 0: continue
        num_list.append((1, i))
    for i in nums:
        if i == 0: continue
        for j in nums:
            num_list.append((2, i * 10 + j))
    for i in nums:
        if i == 0: continue
        for j in nums:
            for k in nums:
                num_list.append((3, i * 100 + 10 * j + k))
    return num_list
 
 
for tc in range(1, 1 + int(input())):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    ops = input().split()
    W = int(input())
    num_list = create(nums)
    memo = [M] * 1000
    ans = M + 1
    for l, num in num_list:
        solve(num, l, 0)
    if ans == M + 1: ans = -1
    if W == 0 and 0 in nums:
        ans = 1
    elif W == 0 and '2' in ops:
        ans = 3
    print(f"#{tc} {ans}")


# recur 2
def calc(q, n, op):
    rtn = 0
    if op == 1: rtn = q + n
    elif op == 2: rtn = q - n
    elif op == 3: rtn = q * n
    elif op == 4:
        if n == 0:
            return -1
        rtn = q // n
    if 0<= rtn < 1000: return rtn
    else: return -1
     
def recur(cur, x):
    if cur == 3: return
    for n in num_list:
        next = x * 10 + n
        if visit[next] <= cur + 1:
            continue
        visit[next] = cur + 1
        que.append(next)
        nums.append(next)
        recur(cur+1, next)    
 
T = int(input())
for t in range(1, T+1):
    N, O, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    #1: 더하기, 2: 빼기, 3: 곱하기, 4: 나누기
    oper = list(map(int, input().split()))
    goal = int(input())
    nums = []    
         
    INF = M+1
    visit = [INF] * 1000
    que = []
    recur(0, 0)
         
    if visit[goal] < INF:
        print(f'#{t} {visit[goal]}')
        continue
     
    while que:
        q = que.pop(0)
        for n in nums:
            click = visit[q] + len(str(n)) + 1
            if click + 1 > M:
                continue
            for op in oper:
                next = calc(q, n, op)
                if next == -1:
                    continue
                if visit[next] <= click:
                    continue
                visit[next] = click
                que.append(next)
             
    if visit[goal] < INF:
        print(f'#{t} {visit[goal] + 1}')
    else:
        print(f'#{t} -1')



# dfs 1
def comb(num):
    if len(num) == 3:
        return
    for i in range(N):
        touch_list.append(num+str(can_touch[i]))
        if num+str(can_touch[i]) != '0':
            comb(num+str(can_touch[i]))
 
def calc(op, n1, n2, c):
 
    c += len(n2)+1
 
    if op == 1:
        return int(n1)+int(n2), c
    if op == 2:
        return int(n1)-int(n2), c
    if op == 3:
        return int(n1)*int(n2), c
    if op == 4:
        return int(n1)//int(n2), c
 
 
 
def DFS(n, cnt):
    global result
 
    if int(n) == W:
        if n in touch_list:
            result = min(result, cnt)
        else:
            result = min(result, cnt+1)
        return
 
    for num in touch_list:
        if num == '0':
            continue
        for o in operators:
            n_n, n_c = calc(o, n, num, cnt)
            if 0 <= n_n <= 999 and n_c < M and n_c < result and n_c < visited[n_n]:
                visited[n_n] = n_c
                DFS(str(n_n), n_c)
 
T = int(input())
for test_case in range(1, T+1):
    N, O, M = map(int, input().split())
 
    can_touch = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input())
 
    touch_list = []
    comb('')
 
    visited = [M]*1000
 
    result = 21
    for num in touch_list:
        DFS(num, len(num))
 
    if result == 21:
        result = -1
 
    print('#%d %d'%(test_case, result))



# dfs 2
def cal(op, n, num):
    if 1 is op:
        return n + num
    if 2 is op:
        return n - num
    if 3 is op:
        return n * num
    if 4 is op:
        return n // num # 나눗셈의 몫 구하기
 
def product(n):
    products.add(n)
    for num in nums:
        new_num = int(str(n) + str(num))
        if len(str(new_num)) < 4 and new_num not in products:
            product(new_num)
 
def dfs(n):
 
    if n == 0:
        return
 
    for num in nums:
        if num == 0:
            continue
 
        for op in OP:
            new_num = cal(op, n, num)
            if 0 <= new_num < 1000 and \
                    candidate_n[n] + candidate_n[num] + 1 < M and \
                    (candidate_n[new_num] == 0 or (candidate_n[n] + candidate_n[num] + 1 < candidate_n[new_num])):
                candidate_n[new_num] = candidate_n[n] + candidate_n[num] + 1
                dfs(new_num)
 
T = int(input())
for test_case in range(1, T + 1):
 
    N, O, M = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    OP = list(map(int, input().split()))
    W = int(input())
 
    candidate_n = [0] * 1000
    products = set()
    result = 0
 
    for num in nums:
        product(num)
 
    products = sorted(list(products))
 
    nums = []
 
    for num in products:
        candidate_n[num] = len(str(num))
        nums.append(num)
 
    # 가지고 있는 것으로도 만들 수 있다면
    if candidate_n[W] > 0:
        result = candidate_n[W]
    else:
        for num in nums:
            dfs(num)
        result = candidate_n[W] + 1 if candidate_n[W] > 0 else -1
 
    print(f'#{test_case} {result}')
'''


