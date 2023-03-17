'''
[설명]
N명이고 신기하게도 N은 짝수
N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눔
번호를 1부터 N까지로 배정
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합
Sij는 Sji와 다를 수도 있음
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji

Sii는 항상 0
나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수

[문제]
스타트 팀과 링크 팀의 능력치의 차이의 최솟값 -> 경우의 수 DFS -> 최소 차이
'''
'''
[알고리즘]
- 차이의 최소값
    - 초기값을 최대(1e9)로 설정

- DFS
    - visited
        - 선택된 선수에 대해 따로 저장 x
        - visited로 판단
        - visited[player_idx] = 선정 여부
    - 탐색
        - 작은 player_idx 부터 오름차순 선택
        - depth(selected_cnt) == N//2 전체 인원 절반 되면 정산
    - 계산
        - arr[i][j] 는 arr[j][i]와 합산 할 필요 없음
        - i,j 전체 탐색하게 되면 자연스럽게 합산됨
'''
'''
[구조]
- visited N 명
- arr 능력치 저장
- min_diff = int(1e9)

- DFS(0, 0)
- print(min_diff)


- DFS(selected_cnt, player_idx):
    # 절반만 계산. [0,1,2]가 선택되면 나머지는 자동 다른팀
    - if selected_cnt == N//2: 
        power1, power2 = 0, 0
        - for 전체 탐색:
            # 2명씩 확인
            - if visited[i] and visited[j]: # 선정되면 포함 
                - power1 += arr[i][j]
            - elif not visited[i] and not visited[j]: # 아니면 다른팀
                - power2 += arr[i][j]
        - min_diff = min(min_diff, abs(power1-power2))
        - return

    - for range(player_idx, N):
        - if 미방문:
            - visited[i] 방문 처리
            - DFS(selected_cnt+1, i+1)
            - visited[i] 원복

'''


def DFS(selected_cnt, player_idx):
    global min_diff
    if selected_cnt == N//2: # 절반만 계산. [0,1,2]가 선택되면 나머지는 자동 다른팀
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 2명씩 확인. 선정되면 포함.
                    power1 += arr[i][j]
                elif not visited[i] and not visited[j]: # 아니면 다른팀
                    power2 += arr[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(player_idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(selected_cnt+1, i+1)
            visited[i] = False


N = int(input())

visited = [False for _ in range(N)] # N 명
arr = [list(map(int, input().split())) for _ in range(N)] # 능력치
min_diff = int(1e9)

DFS(0, 0)
print(min_diff)