''' my idea

class stack():

def save_memory():

def preprocessing():



def intpret():

sm, sc, si = 메모리(배열) 크기, 코드 크기, 입력 크기
progrem_codes = input()
input_codes = input()
save_memory(input_codes):

'''
'''
"무한루프"
- 특정 시점부터 탈출하지 않는 가장 안쪽 루프
- [[]] 이런 식으로 루프가 중첩된 경우
    - 가장 바깥쪽 루프는 안쪽 루프에 갇혀 영원히 탈출할 수 없음
    - 정확한 무한루프는 안쪽 루프가 해당
    - 단순 구현 + 50,000,000 범위 안에 갇힌 위치 알아내기
- 무한 루프의 위치 찾기
    - (5천만 * 2배) 명령어 실행
    - 무한 루프 빠짐
    - 5천만 개의 명령어 실행 횟수 내에 들어온 가장 바깥쪽 루프 선택
    - ①[아직 무한 루프 아님 ②[뭔가 실행 ③[뭔가 실행2]  뭔가 실행3] 무한 루프 때문에 여기로 다시 못 나옴]
    - ①-②-③ 중에 5천만 누적 횟수 안에 들어온 가장 첫번째는 ②
'''

import sys

input = sys.stdin.readline


def preprocess():
    global s_c
    stack = []
    for i in range(s_c):
        if program[i] == '[': # 시작 저장
            stack.append(i)
        if program[i] == ']': # 끝 저장
            j = stack.pop()
            jmptable[i] = j
            jmptable[j] = i


def interpreter():
    global pointer, ip, input_idx, min_ip, max_ip
    if program[ip] == '-':
        memory[pointer] = (memory[pointer] - 1) % 256
    elif program[ip] == '+':
        memory[pointer] = (memory[pointer] + 1) % 256
    elif program[ip] == '<':
        pointer = (pointer - 1) % s_m
    elif program[ip] == '>':
        pointer = (pointer + 1) % s_m
    elif program[ip] == '[':
        if memory[pointer] == 0:
            ip = jmptable[ip]
    elif program[ip] == ']':
        if memory[pointer] != 0:
            ip = jmptable[ip]
    elif program[ip] == ',':
        memory[pointer] = ord(inputs[input_idx]) if input_idx < s_i else 255 # EOF인 경우 255 저장
        input_idx += 1

    ip += 1
    if times > 50000000:
        min_ip = min(min_ip, ip)
        max_ip = max(max_ip, ip)

    return pointer, ip, input_idx


T = int(input())

for _ in range(T):
    s_m, s_c, s_i = map(int, input().split()) # memory_size, program_size, input_size
    program = input().strip() # strip으로 저장해야 시간내 처리 가능
    inputs = input().strip()
    memory = [0] * s_m
    jmptable = [-1] * s_c
    preprocess()

    pointer, ip, input_idx = 0, 0, 0
    times = 0
    min_ip = max_ip = 0

    while ip < s_c: # progrem 종료까지 확인
        if times == 50000000:
            min_ip = max_ip = ip
        if times >= 50000000*2:
            print("Loops", min_ip - 1, max_ip)
            break

        times += 1
        pointer, ip, input_idx = interpreter()
    if ip == s_c: # 정상 종료 기준
        print("Terminates")