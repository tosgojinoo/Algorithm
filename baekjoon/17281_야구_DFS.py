'''
[설명]
⚾는 9명
하나의 이닝은 공격과 수비
총 N이닝
한 이닝에 3아웃이 발생하면 이닝이 종료
두 팀이 공격과 수비를 서로 변경

두 팀은 경기가 시작하기 전까지 타순(타자가 타석에 서는 순서)을 정함
경기 중에는 타순을 변경 불가
9번 타자까지 공을 쳤는데 3아웃이 발생하지 않은 상태면 이닝은 끝나지 않고, 1번 타자가 다시 타석에 선다.
타순은 이닝이 변경되어도 순서를 유지해야 한다.

공격은 투수가 던진 공을 타석에 있는 타자가 치는 것이다.
공격 팀의 선수가 1루, 2루, 3루를 거쳐서 홈에 도착하면 1점을 득점한다.
타자가 홈에 도착하지 못하고 1루, 2루, 3루 중 하나에 머물러있을 수 있다.
루에 있는 선수를 주자라고 한다.
이닝이 시작될 때는 주자는 없다.

- 타자가 공을 쳐서 얻을 수 있는 결과는
    - 안타, 2루타, 3루타, 홈런, 아웃
    - 1 - 안타: 타자와 모든 주자가 한 루씩 진루
    - 2 - 2루타: 타자와 모든 주자가 두 루씩 진루
    - 3 - 3루타: 타자와 모든 주자가 세 루씩 진루
    - 4 - 홈런: 타자와 모든 주자가 홈까지 진루
    - 0 - 아웃: 모든 주자는 진루하지 못하고, 공격 팀에 아웃이 하나 증가

한 야구팀의 감독 아인타는 타순을 정함 -> (4번타자 제외) 제한 없고, 최대 점수 -> 경우의 수 DFS
아인타 팀의 선수는 총 9명
1번부터 9번까지 번호
아인타는 자신이 가장 좋아하는 선수인 1번 선수를 4번 타자로 미리 결정
이제 다른 선수의 타순을 모두 결정
각 이닝에는 아웃을 기록하는 타자가 적어도 한 명 존재

[문제]
아인타팀이 얻을 수 있는 최대 점수
'''
'''
[알고리즘]
- select
    - 타순 리스트
- 1번 타자는 4번 타순으로 이미 정해져있기 때문에 
    - select[3] = 0, visited[3] = 1
- DFS
    - 타순 경우의 수 생성 > score 계산 > 최대값 출력
    - hit_player 
        - 타석에 들어갈 선수
    - out, b1, b2, b3
        - out & 베이스 변수
        - 0으로 초기화
        - 결과별 업데이트
    - while out <= 2:
        - hit_player %= 9 
        - 3 아웃 될때까지 타자 계속 순회

'''
'''
[구조]
- arr = 9개 선수의 N 이닝별 결과
- select = 타순 리스트

- select[3], visited[3] = 0, 1
- DFS(1) 0번은 4번 타자로 고정
- print(ans)

- DFS(player_idx):
    - if player_idx == 9: # 타순 모두 입력 시
        - hit_player, score = 0, 0
        - for arr:
            - out, b1, b2, b3 = 0, 0, 0, 0 # 베이스 초기화
            - while out <= 2: 3 아웃 종료
                - status = select[hit_player] 
                - if 아웃: 
                    - out += 1
                - elif 1루타: 
                    - score += b3
                    - b1, b2, b3 = 1, b1, b2 # 타자, 주자 이동
                 -elif 2루타: 
                    - score += b2 + b3 # 2,3루 주자 베이스로
                    - b1, b2, b3 = 0, 1, b1 # 타자, 주자 이동
                - elif 3루타: 
                    - score += b1 + b2 + b3 # 1~3루 주자 베이스로
                    - b1, b2, b3 = 0, 0, 1 # 타자 3루로
                - else: 홈런
                    - score += b1 + b2 + b3 + 1 # 모든 주자 + 타자 베이스로
                    - b1, b2, b3 = 0, 0, 0

                - hit_player += 1
                - hit_player %= 9 # 9번 -> 1번 타자 순회

        ans = max(ans, score)
        return
    
    # 타순 경우의 수 생성
    - for order_idx in range(9): 
        - if 방문: 무시
        - visited[order_idx] = 방문 처리
        - select[order_idx] = player_idx 타순 입력
        - DFS(player_idx + 1) 지명 선수 idx 증가
        - visited[order_idx], select[order_idx] = 0 원복
'''

import sys

input = sys.stdin.readline

def DFS(player_idx):
    global ans
    if player_idx == 9: # 타순 모두 입력 시
        hit_player, score = 0, 0
        for inning in arr:
            out, b1, b2, b3 = 0, 0, 0, 0
            while out <= 2: # 3 아웃 종료
                status = select[hit_player] # 이닝별 타순 기록
                if inning[status] == 0:
                    out += 1
                elif inning[status] == 1: # 1루타
                    score += b3 # 3루 주자 베이스로
                    b1, b2, b3 = 1, b1, b2 # 타자 1루로
                elif inning[status] == 2: # 2루타
                    score += b2 + b3 # 2,3루 주자 베이스로
                    b1, b2, b3 = 0, 1, b1 # 타자, 주자 이동
                elif inning[status] == 3: # 3루타
                    score += b1 + b2 + b3 # 1~3루 주자 베이스로
                    b1, b2, b3 = 0, 0, 1 # 타자 3루로
                else:
                    score += b1 + b2 + b3 + 1 # 모든 주자 + 타자 베이스로
                    b1, b2, b3 = 0, 0, 0

                hit_player += 1
                hit_player %= 9 # 9번 -> 1번 타자 순회

        ans = max(ans, score)
        return

    for order_idx in range(9): # 타순 경우의 수 생성
        if visited[order_idx]:
            continue
        visited[order_idx] = 1
        select[order_idx] = player_idx # 타순 입력
        DFS(player_idx + 1)
        visited[order_idx] = 0
        select[order_idx] = 0


N = int(input()) # 이닝 수 N(2 ≤ N ≤ 50)
arr = [list(map(int, input().split())) for _ in range(N)]
select = [0 for _ in range(9)]
visited = [0 for _ in range(9)]
select[3], visited[3] = 0, 1
ans = 0
DFS(1)
print(ans)
