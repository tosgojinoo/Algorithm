# - 타순 리스트 select
# - 중복 검사 리스트 visited
# - 1번 타자는 4번 타순으로 이미 정해져있기 때문에 
#     - select[3] = 0, c[3] = 1
# - DFS. 모든 타순에 대한 점수 계산
# - 타석에 들어갈 선수를 알려주는 변수 start
# - 점수 저장 score
# - 매 이닝마다 아웃카운트 out, 루에 있는지 확인할 변수 b1~b3를 초기화
# - 아웃카운트가 3이 될 때까지 타순 연속
# - 만약 타석에 들어간 선수가 할 행동이 0 이면 out 증가
# - 1~4이면 각 숫자에 맞게 점수를 증가. b1~b3 갱신
# - start를 증가시키고 9로 나눈 나머지로 갱신
# - 모든 이닝이 끝나면 최대값 갱신

import sys

input = sys.stdin.readline

def DFS(cnt):
    global ans
    if cnt == 9: # 타순 모두 입력 시
        hit_start, score = 0, 0
        for inning in arr:
            out, b1, b2, b3 = 0, 0, 0, 0
            while out <= 2: # 3 아웃 종료
                status = select[hit_start] # 이닝별 타순 기록
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

                hit_start += 1
                hit_start %= 9 # 9번 -> 1번 타자 순회

        ans = max(ans, score)
        return

    for i in range(9): # 타순 경우의 수 생성
        if visited[i]:
            continue
        visited[i] = 1
        select[i] = cnt # 타순 입력
        DFS(cnt + 1)
        visited[i] = 0
        select[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
select = [0 for _ in range(9)]
visited = [0 for _ in range(9)]
select[3], visited[3] = 0, 1
ans = 0
DFS(1)
print(ans)
