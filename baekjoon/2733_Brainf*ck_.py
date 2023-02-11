class Stack(list):
    def push(self, data):
        self.append(data)

    def empty(self):
        return len(self) == 0


def preprocess(cmds):
    code = ""
    ops = ['<', '>', '+', '-', '[', ']', '.']
    for line in cmds:
        o = ""

        for c in line:
            if c == "%":
                break
            if c in ops:
                o += c
        code += o
    return code


def interpret(code):
    out = ""
    mem = [0 for _ in range(MEM_SIZE)]
    ptr = 0
    jmptable = {}
    stack = Stack()
    for i in range(len(code)):
        if code[i] == "[":
            stack.push(i)
        elif code[i] == "]":
            if stack.empty():
                return None

            st = stack.pop()
            jmptable[st] = i
            jmptable[i] = st

    if not stack.empty():
        return None

    ip = 0
    while ip < len(code):
        cmd = code[ip]
        if cmd == ">":
            ptr = (ptr + 1) % MEM_SIZE
        elif cmd == "<":
            ptr = (ptr - 1) % MEM_SIZE
        elif cmd == "+":
            mem[ptr] = (mem[ptr] + 1) % 256
        elif cmd == "-":
            mem[ptr] = (mem[ptr] - 1) % 256
        elif cmd == ".":
            out += chr(mem[ptr])
        elif cmd == "[":
            if mem[ptr] == 0:
                ip = jmptable[ip] - 1
        elif cmd == "]":
            if mem[ptr] != 0:
                ip = jmptable[ip] - 1

        ip += 1
    return out


MEM_SIZE = 32768
for i in range(int(input())):
    cmds = []
    while True:
        cm = input()
        if "end" in cm:
            break
        cmds.append(cm)

    code = preprocess(cmds)
    result = interpret(code)

    print(f"PROGRAM #{(i + 1)}:")
    if result == None:
        print("COMPILE ERROR")
    else:
        print(result)
