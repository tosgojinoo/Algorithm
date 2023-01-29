# transpose
my_list_transpose = [x for x in zip(*my_list)]

# 모든 약수
def divisor(T):
    a = []
    for i in range(1, T+1):
        if T % i == 0:
            a.append(i)
    return a


# 대소문자
if T.isupper():
    print(f'{T} 는 대문자 입니다.')


# 가위바위보
Man1 = input()
Man2 = input()
    
ref =  ["가위", "바위", "보"] 

# 실행 시간 : 0.08975s 
if Man1 == Man2:
    print(f'Result : Draw')
else:
    if ref.index(Man1) == 0:
        if ref.index(Man2) == 1:
            print(f'Result : Man1 Win!')
        else:
            print(f'Result : Man2 Win!')
    elif ref.index(Man1) == 1:
        if ref.index(Man2) == 0:
            print(f'Result : Man1 Win!')
        else:
            print(f'Result : Man2 Win!')
    else:
        if ref.index(Man2) == 1:
            print(f'Result : Man1 Win!')
        else:
            print(f'Result : Man2 Win!')

# 실행 시간 : 0.08729s
if ref.index(Man1) < ref.index(Man2):
    if ref.index(Man1) == 0 and ref.index(Man2) == 2:
        print(f'Result : Man1 Win!')
    else:
        print(f'Result : Man2 Win!')
if ref.index(Man1) > ref.index(Man2):
    if ref.index(Man1) == 2 and ref.index(Man2) == 0:
        print(f'Result : Man2 Win!')
    else:
        print(f'Result : Man1 Win!')

if Man1 == Man2:
    print(f'Result : Draw')



# 대소문자 스위칭
if T.isalpha():
    if T.isupper():
        print(f'{T}(ASCII: {ord(T)}) => {T.lower()}(ASCII: {ord(T.lower())})')
    else:
        print(f'{T}(ASCII: {ord(T)}) => {T.upper()}(ASCII: {ord(T.upper())})')
else:
    print(f'{T}')


# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자
ans = []
for i in range(1, 200+1):
    if i % 7 == 0 and i % 5 !=0:
        ans.append(i)
print(*ans, sep = ',') # unpack 연산자인 *로 []를 제거


# 100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자
ans = []
for i in range(100, 300+1):
    dec100 = int(i / 100)
    dec10 = int((i-dec100*100)/10)
    dec1 = i-dec100*100-dec10*10
    if dec100 % 2 == 0 and dec10 % 2 == 0 and dec1 % 2 == 0:
        ans.append(i)

print(*ans, sep=',') 


# 21: 60 이상일 때 합격 메시지를 출력하고, 60미만일 때 불합격
result = [88, 30, 61, 55, 95]
num = 1

for r in result:
    if r >= 60:
        print(f'{num}번 학생은 {r}점으로 합격입니다.')
    else:
        print(f'{num}번 학생은 {r}점으로 불합격입니다.')
        num += 1


# 26: 혈액형
blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
ans = {}
keys = set(blood)
for b in set(blood):
    ans[b] = blood.count(b) 


# 27: pop
while len(scores) > 0:
    if scores[-1] >= 80:
        result += scores[-1]
    scores.pop() 


# 29: stars
start = 7
now = start
space = 0

while now > 0:
    print(f'{" "*space}{"*"*now}{" "*space}')
    space += 1
    now = start - space * 2 


# 30: 0~9가 몇 번 사용
# 1
decimal = []
result = {}

while int(T) > 0:
    decimal.append(int(T[0]))
    if len(T) ==1:
        break
    else:
        T = T[1:]

for i in range(9+1):
    result[i] = decimal.count(i)

print('0 1 2 3 4 5 6 7 8 9')
print(*list(result.values()), sep=' ')

# 2
lst = [0] * 10

while i > 0:
    lst[i % 10] += 1
    i = i // 10

print('0 1 2 3 4 5 6 7 8 9')
print(*lst, sep=' ') # print(' '.join(map(str, lst)))


# 32: 10 > 2진수
binary = []

while T >0:
    binary.append(T % 2)
    T = T // 2 
    
print(*reversed(binary), sep='')


# 34: 회문
T == T[::-1]


# 36: 가위바위보
def fight(attack1, attack2):
    ref = ['가위', '바위', '보']
    if attack1 == attack2:
        return 'same'
    if ref.index(attack1) > ref.index(attack2):
        if ref.index(attack1) == 2 and ref.index(attack2) == 0:
            return 'lose'
        else:
            return 'win'
    else:
        if ref.index(attack1) == 0 and ref.index(attack2) == 2:
            return 'win'
        else:
            return 'lose'


# 36: 소수인지 판단
def prime(num):
    divisor = num-1
    if num == 1:
        result = '가 아닙니다.'
    elif num == 2:
        result = '입니다.'
    else:
        while divisor > 1:
            if num % divisor == 0:
                result = '가 아닙니다.'
                break
            else:
                result = '입니다.'
            divisor -= 1
    return result 


# 37: 피보나치 수열
def fibonacci(num):
    fib = [1, 1]
    while len(fib) <= num-1:
        fib.append(fib[-2] + fib[-1])
    return fib


# 46: map, lambda
score = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
ref =  ['D', 'C', 'B', 'A']
print(sum(list(map(lambda x: score.count(x) * (ref.index(x)+1), ref))))


# 51: map, filter, lambda
print(list(map(lambda x: x**2, filter(lambda x: x%2==0, lst))))


# 53: 딕셔너리 객체의 키와 값 정보를 출력
keys = 'abcdef'
idx = 0
result = {}
for key in keys:
    result[key] = idx
    idx += 1
# print(result)

for key, value in result.items():
    print(f'{key}: {value}')


# 5: 구구단
result = []
for i in range(2, 9+1):
        # and 를 논리곱으로 생각하기
    tmp = [ i*j for j in range(1, 9+1) if i*j % 3 and i*j % 7 ] 
    result.append(tmp) 


# 7: 약수 출력
def divisors(num):
    divisor = num
    result = []
    while divisor > 0:
        if num % divisor == 0:
            result.append(divisor)
        divisor -= 1
    return list(reversed(result)) 

def divisors(num):
    result = [divisor for divisor in range(1, num+1) if num % divisor == 0]
    return result


# 13: 단어 분류
dicBase = (('가','깋'), ('나','닣'), ('다','딯'), ('라','맇'), ('마','밓'), ('바','빟'), ('사','싷'),('아','잏'), ('자','짛'), ('차','칳'), ('카','킿'), ('타','팋'), ('파','핗'), ('하','힣'))
inputWord = ['막', '부모님', '비용', '비행기', '원래', '처리', '최초', '꼴', '좀', '들다', '싶다', 
                '수출', '계시다', '다', '뒤', '듣다', '함께', '아이', '무척', '보이다', '가지다', '그',
                '자르다', '데리다', '마리', '개', '정도', '옳다', '놀이','뜨겁다']

print([[w for w in inputWord if ord(b[0]) <= ord(w[0]) <= ord(b[1])] for b in dicBase])


# 16: 2차원 배열 구조를 만들기
shp = tuple(map(int, T.split(', ')))
print([[c*r for c in range(shp[1])] for r in range(shp[0])]) 


# 17: 사전순 정렬
word_pack.sort()


# 22: 0을 갖는 2*3*4 형태의 3차원 배열
[[[0 for d3 in range(4)] for d2 in range(3)] for d1 in range(2)] 


# 30: 리스트의 원소를 키로 하고, 그 원소의 length를 값으로 갖는 딕셔너리, 원소 공백 제거
fruit = ['   apple    ','banana','  melon']
fruit = [(''.join([w for w in word if w != ' '])) for word in fruit]
print({f:len(f) for f in fruit}) 


# 32: 숫자와 문자 구별
LETTERS = 0
DIGITS = 0
for i in T:
    if ord('0') <= ord(i) <= ord('9'):
        DIGITS += 1
    elif ord('a') <= ord(i) <= ord('z'):
        LETTERS += 1


# 40: 대문자
'a'.upper() 


# 44: 객체지향
class Student():
    def __init__(self, language, english, math):
        self.__language = int(language)
        self.__english= int(english)
        self.__math= int(math)
    
    @property
    def total(self):
        print(f'국어, 영어, 수학의 총점: {sum([self.__language, self.__english, self.__math])}')
        
T=input()
T = T.split(', ') 
s = Student(*T)
s.total


# 45: 정적 메서드(보통 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용)
class Korean():
    def __init__(self, naitonality):
        self.__nationality = naitonality
        print(self.__nationality)
        
    @staticmethod
    def printNationality(naitonality):
        print(naitonality)
        
ref = Korean("대한민국")
ref
ref.printNationality("대한민국")


# 46: super()
class Student():
    def __init__(self, name):
        self.name = name
        print("이름: 홍길동")
        
class GraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.__major = major
        print(f'이름: {self.name}, 전공: {self.__major}')
        
s = GraduateStudent('이순신', '컴퓨터') 


# A도시 전기버스 운행
T = int(input())

# T만큼 테스트 케이스 반복
for tc in range(1, T+1):
# K : 한번 충전으로 최대한 이동할 수 있는 정류장 수
# N : 종점 정류장
# M : 충전기가 설치된 정류장 개수
K, N, M = list(map(int, input().split()))

# 충천지가 설치된 정류장 리스트 입력
charge_station = list(map(int, input().split()))
# 충전 횟수 count와 현재 위치 current 변수 초기화
count = current = 0

# 종점에 도착할 때까지 반복
while current + K < N:
    # K 범위 안에서 현 위치를 조정하면서 이동
    for step in range(K, 0, -1):
        # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
        if (current + step) in charge_station:
            # 현재 위치를 변경
            current += step
            # 충전 횟수 +1
            count += 1
            # for 문을 종료
            break
    # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 count를 0으로 하고 while문을 종료
    else:
        count = 0
        break

# 결과 출력
print('#{} {}'.format(tc, count))

# 오답
def Charge_check(k, m, now):
    m_targets = []
    for m_target in reversed(m[m.index(now):m.index(now)+k]):
        for k_shift in range(k, -1, -1):
            if now + k_shift == m_target:
                m_targets.append(m_target)
    if len(m_targets) > 1:
        result = max(m_targets)
    else:
        result = 0
    return result

T = int(input())
for t in range(T):
    ref = [int(x) for x in input().split(' ')]
    K, N, M = ref[0], ref[1], ref[2]
    m = [0] + [int(x) for x in input().split(' ')] + [N]
    now, charging = 0, []
    for i in range(0, N):
        if i == now:
            now = Charge_check(K, m, now)
            charging.append(now)
    if max(charging) < N:
        result = 0
    else:
        result = len(charging) -1
    
# print(f'#{t+1} {result}')
print('#{} {}'.format(t+1, result))


# **숫자 카드**
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = [int(i) for i in input()]
    #print(ai)
    count = {}
    for i in range(0, 10):
        count[i] = ai.count(i)
    result = sorted(sorted(count.items(), key=lambda x: x[0], reverse=True),key=lambda x: x[1], reverse=True)[0]
    print(f'#{tc} {result[0]} {result[1]}')


# 색칠하기
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]
    base = [[0 for _ in range(10)] for _ in range(10)]
    #print(m)

    for k in range(n):
        for i in range(10):
            for j in range(10):
                if (m[k][0] <= i <= m[k][2]) and (m[k][1] <= j <= m[k][3]):
                    base[i][j] += m[k][4]
    result = len([(i, j) for i in range(10) for j in range(10) if base[i][j] == 3])
    print(f'#{tc} {result}')

# 다른 방법
for tc in range(1, T+1):
    case = int(input())
    #색상 1, 2의 위치를 저장하는 리스트, 내부값은 셋이다.
    position = [set(), set()]
    #케이스만큼 반복
    for i in range(case):
        x1, y1, x2, y2, color = map(int, input().split())
        #x, y를 돌면서 set에 넣는다.
        for a in range(x1, x2+1):
            for b in range(y1, y2+1):
                position[color-1].add((a, b))
#교집합을 이용하여 겹치는 부분만 꺼낸다.
result = position[0] & position[1]
#겹치는 만큼 출력
print('#{} {}'.format(t+1, len(result)))


# 부분집합의 합
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    # print(N, K)
    arr = list(range(1, 12+1))
    n = len(arr)
    result = []
    for i in range(1<<n):
        result_sub = []
        for j in range(n):
            if i&(1<<j):
                result_sub.append(arr[j])
        if len(result_sub) == N and sum(result_sub) == K:
            result.append(result_sub)
    print(f'#{tc} {len(result)}')


# 이진탐색
def binarySearch(a, low, high, key, count):
    if low > high:
        return -1
    else:
        middle = (low + high)//2
        if key == a[middle-1]:
            return count+1
        elif key < a[middle-1]:
            return binarySearch(a, low, middle, key, count+1)
        elif key > a[middle-1]:
            return binarySearch(a, middle, high, key, count+1)

T = int(input())

for tc in range(1, T+1):
    # 책의 전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb
    P, Pa, Pb = list(map(int, input().split()))
    countPa = binarySearch(range(1, P+1), 1, P, Pa, 0)
    countPb = binarySearch(range(1, P+1), 1, P, Pb, 0)
    if countPa > countPb:
        print(f'#{tc} B')
    elif countPa < countPb:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')


# 특별한 정렬
def minmax(lst, i):
    if i > len(lst)-1:
        return lst
    else:
        index_max = lst[i:].index(max(lst[i:]))+i
        lst[i], lst[index_max] = lst[index_max], lst[i]
        index_min = lst[i:].index(min(lst[i:]))+i
        lst[i+1], lst[index_min] = lst[index_min], lst[i+1]
        return minmax(lst, i+2)

T = int(input())
for tc in range(1, T+1):
    N, lst = int(input()), list(map(int, input().split()))
    print(f'#{tc} {" ".join(map(str, minmax(lst, 0)[:10]))}')


# **문자열 비교**


T = int(input())

for t_idx in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{t_idx} 1')
    else:
        print(f'#{t_idx} 0')


# 회문


# 시간초과: 부분집합 구하기 방법 안됨, window활용한 부분집합 구하기 적용

# case1
T = int(input())
for tc in range(1, T + 1):
    def rev_str():
        status = 0
        N,M = map(int, input().split())
        db = [list(input()) for _ in range(N)]
        for i in range(N):
            for j in range(N-M+1):
                if db[i][j:j+M] == db[i][j:j+M][::-1]: # row 방향 회문 판별
                    print(f"#{tc} {''.join(db[i][j:j+M])}")
                    status = 1
        if status == 0:
            db = list(zip(*db))
            for i in range(N):
                for j in range(N-M+1):
                    if db[i][j:j+M] == db[i][j:j+M][::-1]: 
                        print(f"#{tc} {''.join(db[i][j:j+M])}")
    
rev_str()

# case2
def windowSubset(lst, condition):
    result = []
    for i in range(len(lst)-condition+1):
        result.append(''.join(lst[i:i+condition]))
    return result

def palindrome(string):
    if len(string)>1:
        if string == string[::-1]: return True
    return False

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    db = [list(input()) for _ in range(N)]
    result = []
    for data in db:
        data = windowSubset(data, M) 
        if len(data) >0:
            result += [r for r in data if palindrome(r)]
    for data in list(zip(*db)):
        data = windowSubset(data, M) 
        if len(data) >0:
            result += [r for r in data if palindrome(r)]

    print(f"#{tc} {result[0]}")



# 글자수
T = int(input())
for tc in range(1,T+1):
    str1, str2 = input(), input()
    str1 = list(str1)
    ref = dict(zip(str1, [0]*len(str2)))
    for key, _ in ref.items():
        ref[key] = list(str2).count(key)
    ref = sorted(ref.items(), key=lambda x:x[1], reverse=True)
    print(f'#{tc} {ref[0][1]}')


# 종이붙이기
# 재귀
def fun1(N):
    if N <2:
        return 1
    return fun1(N-2)*2 + fun1(N-1)*1

# iretative
def fun2(N):
    # 10 <= N <= 300
    result = [0]*30
    result[0] = 1
    result[1] = 1
    for i in range(2,N+1):
        result[i] = result[i-1] + result[i-2]*2
    return result[N]

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {fun1(int(int(input())/10))}')


# **괄호검사**
T = int(input())
ref = {
'{' : '}',
'[' : ']',
'(' : ')',
}
for tc in range(1, T+1):
    check_list, result, string = [], 1, input()
    for s in string:
        if s in ref.keys():
            check_list.append(s)
        elif s in ref.values():
            if len(check_list) > 0:
                if s == ref[check_list[-1]]:
                    check_list.pop(-1)
                else: result = 0 
            else: result = 0 
                
    if len(check_list)>0: result = 0
    print(f'#{tc} {result}')


# 그래프 경로:
# V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보
# node: [[], [4, 3], [3, 5], [], [6], [], []]
# stack: [1], visited: [0, 1, 0, 0, 0, 0, 0]
# stack: [1, 4], visited: [0, 1, 0, 1, 1, 0, 0]
def search_path(node_num, goal):
    stack.append(node_num)
    visited[node_num] =1
    while stack:
        if node_num == goal:
            return 1
        else:
            for i in node[node_num]:
                if not visited[i]:
                    visited[i] = 1
                    stack.append(i)
            node_num = stack.pop()
    return 0

for tc in range(1, int(input())+1):
    # V개 이내의 노드, E개의 간선
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    stack = []
    for _ in range(E):
        start, end = map(int, input().split())
        node[start].append(end)
    S, G = map(int, input().split())
    print(f'#{tc} {search_path(S, G)}')


# **반복문자 지우기**
# case best
def routine(string):
    ref = {}
    for key in set(list(string)):
        ref[key] = string.count(key+key)
        if ref[key] >0 :
            del_idx = string.index(key+key)
            string = list(string)
            del string[del_idx+1]
            del string[del_idx]
            string = ''.join(string)
    if set(ref.values()) == {0}: return string
    else: return routine(string)

for tc in range(1, int(input())+1):
    string = input()
    print(f'#{tc} {len(routine(string))}')

# case2
def routine(lst):
    result = []
    del_i = False
    del_i_count = 0
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1] and not del_i: 
            result.append(lst[i])
        elif del_i: 
            del_i = False
            del_i_count += 1
        else: 
            del_i = True
            del_i_count += 1
        if i == len(lst)-2 and not del_i: 
            result.append(lst[-1])
    if len(result) >1 and del_i_count > 0:
        return routine(result)
    else:
        return result
    
for tc in range(1, int(input())+1):
    lst = list(input())
    # print(''.join(routine(lst)))
    print(f'#{tc} {len(routine(lst))}')


# Forth
def calc(num1, num2, sign):
    if sign == '/':
        return int(num1)//int(num2)
    elif sign == '*':
        return int(num1)*int(num2)
    elif sign == '+':
        return int(num1)+int(num2)
    elif sign == '-':
        return int(num1)-int(num2)

def cal_total(lst):
    idx = 0
    stack = []
    for r in lst:
        if r == '.': 
            if len(stack)==1: return stack.pop() 
            else: return 'error'
        elif r.isdigit():
            stack.append(r)
        else:
            if len(stack)<2: return 'error'
            else:
                e_num, s_num = stack.pop(-1), stack.pop(-1)
                if str(e_num).isalpha() or str(s_num).isalpha(): return 'error'
                stack.append(calc(s_num, e_num, r))
        idx +=1

for tc in range(1, int(input())+1):
    print(f'#{tc} {cal_total(input().split())}')


# 미로
# DFS, delta 탐색
def dfs(y, x):
    global res
    data[y][x] = 1
    for d in range(4):
        xf = dx[d] + x
        yf = dy[d] + y
        if (0<= xf < N) and (0 <= yf < N):
            if data[yf][xf] == 0: dfs(yf, xf)
            if data[yf][xf] == 3:
                res = 1
                return

for tc in range(1, int(input())+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x, y = j, i

res = 0
dfs(y, x)

print("#%d %d"%(tc, res))

# DFS, stack
def miro():
    while stack:
        y, x = stack.pop()
        arr[y][x] = -1      # 지나간 길 표시
        for i in range(4):  # 네 방향 탐색
            ni = y + di[i]
            nj = x + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 3:    # 도착점 찾으면 1 return
                    return 1
                elif arr[ni][nj] == 0:  # 갈 수 있는 곳을 전부 stack에 담는다.
                    stack.append((ni, nj))
    return 0    # 도착점 못 찾으면 0 return

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]   # 미로
    di = (0, 1, 0, -1)
    dj = (1, 0, -1, 0)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 시작점 찾기
                stack = [(i, j)]
                break
    print(f'#{tc} {miro()}')

# 참고용
def rotate_2d(list_2d):
    n, m = len(list_2d), len(list_2d[0])  # 행, 열 길이
    new = [[0] * n for _ in range(m)]
    # 조건
    i=1
    for r in list_2d:
        if 2 in r: start_node = (i, r.index(2))
        if 3 in r: end_node = (i, r.index(3))            
        i += 1
    direction = (start_node[0]-end_node[0], start_node[1]-end_node[1])
    # main
    for i in range(n):
        for j in range(m):
            # 90도 회전
            if direction[1] == n-1: new[j][n-i-1] = list_2d[i][j]
            #180도 회전
            if direction[0] == -(n-1): new[m-j-1][n-i-1] = list_2d[i][j]
            #270도 회전
            if direction[1] == -(n-1): new[m-j-1][i] = list_2d[i][j]
    if direction[0] == n-1: 
        new = list_2d
        return new


# **토너먼트 카드게임**
# 참조
def game(i, j):
    # 종료조건..점점 줄어들기 때문에 자신과 같아지면 i 출력
    if i == j:
        return i
    # 게임을 시키는 범위.
    # 범위를 둘로 나눠서 재귀를 돌림..
    aidx = game(i, (i+j)//2)
    bidx = game((i+j)//2+1, j)

    # 구해진 인덱스에 해당하는 값들끼리 가위바위보 후 최종적으로 인덱스(=번호)리턴.
    # winner(aidx,bidx)
    if arr[aidx] == 1: # 가위
        if arr[bidx] == 2: return bidx
        elif arr[bidx] == 3: return aidx
        elif arr[bidx] == 1: return aidx
    if arr[aidx] == 2: # 바위
        if arr[bidx] == 1: return aidx
        elif arr[bidx] == 3: return bidx
        elif arr[bidx] == 2: return aidx
    if arr[aidx] == 3: # 보
        if arr[bidx] == 1: return bidx
        elif arr[bidx] == 2: return aidx
        elif arr[bidx] == 3: return aidx

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 인덱스 0을 고려하기 위해 더해주고 출력.
    arr = [0] + list(map(int,input().split()))
    print('#{}'.format(tc), end=' ')
    print(game(1, N))

# 내꺼 
def result_fight(lst):
    if lst[0][0] == lst[1][0]: return lst[0]
    if int(lst[0][0]) + int(lst[1][0])== 3: win = '2'
    elif int(lst[0][0]) + int(lst[1][0])== 4: win = '1'
    elif int(lst[0][0]) + int(lst[1][0]) == 5: win = '3'
    return [x for x in lst if win in x][0]

def divide(lst):
    if len(lst) == 1: return lst[0]
    mid = (len(lst)-1)//2+1
    l_group = divide(lst[:mid])
    r_group = divide(lst[mid:])
    return result_fight([l_group, r_group])

for tc in range(1, int(input())+1):
    N = int(input())
    ref = input().split()
    # index 묶음 구성
    idx = 0
    for r in ref:
        ref[idx] = (r, idx+1)
        idx += 1
    print(f'#{tc} {divide(ref)[1]}')


# **배열 최소 합**
def recur(cur, ssum):
    global min_sum
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            ssum += arr[cur][i]
            if min_sum > ssum:
                if cur == N-1: min_sum = ssum
                else: recur(cur+1, ssum)
            visited[i] = 0
            ssum -= arr[cur][i]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_sum = 10*N
    recur(0, 0)
    print(f'#{tc} {min_sum}')


# 회전
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    templist = list(map(int, input().split()))

queue = []
for i in range(N):
    queue.append(templist[i])

for j in range(M):
    temp = queue.pop(0)
    queue.append(temp)

print('#%d %d' % (test_case, queue[0]))


# 미로의 거리   
def IsSafe(y,x):
    return 0 <= y < N and 0<= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def BFS(start_y, start_x):
    global D_result
    Q.append((start_y, start_x))
    visited.append((start_y, start_x))

    while Q:
        start_y, start_x = Q.pop(0)
        for dir in range(4):
            NewY = start_y + dy[dir]
            NewX = start_x + dx[dir]
            if IsSafe(NewY, NewX) and (NewY, NewX) not in visited:
                Q.append((NewY, NewX))
                visited.append((NewY, NewX))
                Distance[NewY][NewX] = Distance[start_y][start_x] +1
                if Maze[NewY][NewX] == 3:
                    D_result = Distance[NewY][NewX] -1
                    return

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

D_result = 0
Q = []
Distance = [[0]*N for _ in range(N)]
BFS(start_y, start_x)
print(f'#{tc} {D_result}')


# 피자 굽기
TC=int(input())
for tc in range(1, TC+1):
    N, M=map(int, input().split())		# 화덕 크기, 피자 개수
    Data=list(map(int, input().split()))		# 치즈
    Q=[]
    for i in range(N):					# 화덕의 크기만큼 피자 올리기
        Q.append([Data[i], i])

    i=0
    while len(Q) != 1 :
        Q[0][0] //=2			# 치즈가 익음
        if Q[0][0] == 0 :
            if N+i < M :  # 화로크기 + i < 피자 개수
                Q.pop(0)      
                Q.append([Data[N+i], N+i])    # 그 다음 피자 넣기
                i+=1
            elif N+i >= M :               # 넣을 피자 없음  
                Q.pop(0)
        else:
            Q.append(Q.pop(0))          # 피자 넣기

print(f"#{tc} {Q[0][1]+1}")


# 노드의 거리
def bfs(S, G):
    q = [S]
    visited[S] = 1
    while q:
        v = q.pop(0)
        for i in g[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                q.append(i)

            if i == G:
                return visited[i] - 1
    return 0

T = int(input())
for tc in range(1, T+1):
    # V 노드 개수, E 간선 정보 개수
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    
    # 간선 연결 정보
    g = [[]] * (V+1)
    for _ in range(E):
        i, j = map(int, input().split())
        g[i].append(j)
        g[j].append(i)

    S, G = map(int, input().split())
    answer = bfs(S, G)
    print('#{} {}'.format(tc, answer))
