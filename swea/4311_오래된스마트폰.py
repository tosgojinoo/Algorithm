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
 
 
def main():
    T = int(input())
 
    for t in range(1, T + 1):
        N, O, M   = map(int, input().split())
        digits    = list(map(int, input().split()))
        operators = list(map(int, input().split()))
        W         = int(input())
 
        sol = solution(N, O, M, digits, operators, W)
 
        print('#' + str(t) + ' ' + str(sol))
 
 
if __name__ == '__main__':
    main()

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
            if 0 <= n_n <= 999 and n_c < M and n_c < result and n_c < checked[n_n]:
                checked[n_n] = n_c
                DFS(str(n_n), n_c)
 
T = int(input())
for test_case in range(1, T+1):
    N, O, M = map(int, input().split())
 
    can_touch = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    W = int(input())
 
    touch_list = []
    comb('')
 
    checked = [M]*1000
 
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
 
#####################
# 알고 있어야 할 것
# set에서 추가시 add이다.


