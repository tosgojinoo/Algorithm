'''
[설명]
두 개의 인접한 돌다리, <악마의 돌다리> <천사의 돌다리>
각 칸의 문자는 해당 돌에 새겨진 문자를 나타냄.
두 다리에 새겨진 각 문자는 {R, I, N, G, S} 중 하나
순서대로 밟고 지나가야할 문자들 조건
다리를 건널 때 다음의 제한 조건
1. 왼쪽(출발지역)에서 오른쪽(도착지역)으로 다리를 지나가야 하며,
반드시 마법의 두루마리에 적힌 문자열의 순서대로 모두 밟고 지나가야 한다.
2. 반드시 <악마의 돌다리>와 <천사의 돌다리>를 번갈아가면서 돌을 밟아야 한다. -> 번갈아가며 전진
단, 출발은 어떤 돌다리에서 시작해도 된다. -> 각각의 case 계산
3. 반드시 한 칸 이상 오른쪽으로 전진해야하며, 건너뛰는 칸의 수에는 상관이 없다. -> 이미 밟은 idx 초과만 다음 허용.

[문제]
문자열의 순서대로 다리를 건너갈 수 있는 방법의 수
방법이 없으면 0 출력
'''
'''
[알고리즘]
- 입력 및 모든 memory
    - 맨 앞에 padding 필요. 
    - 2개씩 확인하기 때문(본인과 그 이전)
    - 본인 key와 동일한 값을 찾음, 이후 이전 key와 동일한 옆 돌다리의 값을 찾음
- DP
    - 현 돌다리 지점과 동일한 key값과 이전 key값은 모두 조건 만족하는 누적 방법의 수 저장
    - 예) DP[3] == key[1~3] + key[1~5] 조건 만족 경우의 수 누적 합(key[0] =='' padding)  
    - DP[돌다리 길이][먼저 시작한 돌다리 flag]
- 돌다리 배열을 뒤에서 부터 탐색
    - 배열은 뒤에서부터, 키는 앞에서부터 맞춰감
    - 배열을 앞에서부터 탐색하면 경로가 0이되어(DP저장 안됨) 뒤에 존재하는 경로도 0이 되기 때문

'''
'''
[구조]
- memory 구성
    - key, angel, devil
    - 맨 앞 '' padding
- DP[돌다리 flag][idx]
- for key (0 ~ 끝)
    for idx_limit(탐색 기준) (끝 ~ 0)
        solve(angle 우선)
        solve(devil 우선)

- solve
    - first 돌다리, second 돌다리 설정
    - if key와 일치하는 first 돌다리 내 위치 idx_limit 확인
        - for idx_limit 보다 작은 idx 중
            - if 옆 돌다리에서 key의 이전값을 찾는다면
                - tmp에 DP[옆 돌다리][idx_before] 추가
        - DP[현 돌다리][idx_limit]에 tmp 저장(이전 모든 경우의 누적값). 경우가 없다면 0.
        - if key_idx가 마지막
            - ans에 추가
'''

def solve(first, flag):
    global ans
    tmp = 0
    if first == devil:
        second = angel
    else:
        second = devil
    if first[idx_limit] == key[key_idx]: # key와 일치하는 돌다리 위치 확인
        for idx_before in range(idx_limit-1, -1, -1): # idx_limit 이전부터 0까지 차례대로 확인
            if second[idx_before] == key[key_idx-1]: # key의 이전값을 옆 돌다리에서 확인
                tmp += DP[flag][idx_before]
        DP[not flag][idx_limit] = tmp
        if key_idx == len(key)-1:
            ans += tmp


key = [''] + list(input()) # 맨 앞에 padding 필요. 2개씩 확인하기 때문(본인과 그 이전).
angel = [''] + list(input())
devil = [''] + list(input())
DP = [[0 for _ in range(len(angel))] for _ in range(2)] # 시작하는 돌다리 case 별로 구분
DP[0][0], DP[1][0] = 1, 1
ans = 0

for key_idx in range(1, len(key)):
    for idx_limit in range(len(devil)-1, -1, -1): # 탐색 제한 idx 설정
        solve(angel, 1) # angel 먼저 시작 경우. 상대의 DP를 지칭하는 flag.
        solve(devil, 0) # devil 먼저 시작 경우

print(ans)