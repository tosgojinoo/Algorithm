def comb(num):
    if len(num) == 3:
        return
    for i in range(N):
        touch_list.append(num+str(can_touch[i]))
        if num+str(can_touch[i]) != '0':
            comb(num+str(can_touch[i]))

 
def calc(op, n1, n2, cnt):
    cnt += len(n2)+1
    if op == 1: return int(n1)+int(n2), cnt
    if op == 2: return int(n1)-int(n2), cnt
    if op == 3: return int(n1)*int(n2), cnt
    if op == 4: return int(n1)//int(n2), cnt
 
def DFS(num, cnt):
    global result
 
    if int(num) == W:
        if num in touch_list: result = min(result, cnt)
        else: result = min(result, cnt+1)
        return
 
    for choice_num in touch_list:
        if choice_num == '0': continue
        for choice_o in operators:
            new_num, new_cnt = calc(choice_o, num, choice_num, cnt)
            if 0 <= new_num <= 999 and new_cnt < M and new_cnt < result and new_cnt < checked[new_num]:
                checked[new_num] = new_cnt
                DFS(str(new_num), new_cnt)
 
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
