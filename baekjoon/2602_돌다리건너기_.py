'''
- 전의 키값의 dp가 저장되어 있으면 모든 dp의 값을 더해주고 없으면 경로가 존재하지 않으므로 0으로 초기화
  (배열을 뒤에서 탐색하는 이유, 앞부터 탐색하면 경로가 0이되어 뒤에 존재하는 경로도 0이 되기 때문)
- 마지막 키값에 도달했을때 총합 누적
'''
key = [''] + list(input()) # 2개씩 확인(본인과 그 이전). 맨 앞에 padding 필요.
angel = [''] + list(input())
devil = [''] + list(input())
DP = [[0 for _ in range(len(angel))] for _ in range(2)]
DP[0][0], DP[1][0] = 1, 1
ans = 0

def solve(first, flag):
    global ans
    tmp = 0
    if first == devil:
        second = angel
    else:
        second = devil
    if first[idx_limit] == key[key_idx]:
        for idx in range(idx_limit-1, -1, -1):
            if second[idx] == key[key_idx-1]: # 다음 한자리까지만 확인
                tmp += DP[flag][idx]
        DP[not flag][idx_limit] = tmp
        if key_idx == len(key)-1:
            ans += tmp


for key_idx in range(1, len(key)):
    for idx_limit in range(len(devil)-1, -1, -1):
        solve(angel, 1) # angel 먼저 시작 경우. 상대의 DP를 지칭하는 flag.
        solve(devil, 0) # devil 먼저 시작 경우

print(ans)