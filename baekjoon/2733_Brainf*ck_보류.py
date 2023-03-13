class Stack(list):
    def push(self, data):
        self.append(data)

    def empty(self):
        return len(self) == 0


def preprocess(program): # 주석 삭제 및 연결
    code = ""
    ops = ['<', '>', '+', '-', '[', ']', '.']
    for line in program:
        tmp = ""
        for character in line:
            if character == "%":
                break
            if character in ops:
                tmp += character
        code += tmp
    return code


def interpret(code):
    jmptable = {} # 짝이 되는 '[]'의 위치 기록
    stack = Stack()
    for i in range(len(code)):
        if code[i] == "[": # 시작점
            stack.push(i)
        elif code[i] == "]": # 종료점
            if stack.empty(): # 비정상 감지. 무조건 짝을 이뤄야함.
                return

            code_idx = stack.pop()
            jmptable[code_idx] = i # code 의 시작/끝 표기
            jmptable[i] = code_idx

    if not stack.empty(): # 비정상 감지
        return

    memory = [0 for _ in range(MEM_SIZE)]
    out = ""
    pointer = 0
    ip = 0 # instrtuction pointer
    while ip < len(code):
        cmd = code[ip]
        if cmd == ">":
            pointer = (pointer + 1) % MEM_SIZE
        elif cmd == "<":
            pointer = (pointer - 1) % MEM_SIZE
        elif cmd == "+":
            memory[pointer] = (memory[pointer] + 1) % 256
        elif cmd == "-":
            memory[pointer] = (memory[pointer] - 1) % 256
        elif cmd == ".":
            out += chr(memory[pointer])
        elif cmd == "[":
            if memory[pointer] == 0: # 포인터가 가리키는 값이 0이면, 짝이 되는 ']'로 이동
                ip = jmptable[ip] - 1
        elif cmd == "]":
            if memory[pointer] != 0: # 포인터가 가리키는 값이 0이 아니면, 짝이 되는 '['로 이동
                ip = jmptable[ip] - 1

        ip += 1
    return out


MEM_SIZE = 32768 # pointer 값
for i in range(int(input())):
    program = []
    while True:
        cmd = input()
        if "end" in cmd:
            break
        program.append(cmd)

    code = preprocess(program) # 주석 '%' 삭제. 하나로 연결.
    result = interpret(code)

    print(f"PROGRAM #{(i + 1)}:")
    if result == None:
        print("COMPILE ERROR")
    else:
        print(result)
