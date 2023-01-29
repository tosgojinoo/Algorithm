# 이동1: x-1, x+1 (1초)
# 이동2: 2*x (0초)
# visited & cnt 방식
# visited 는 '정적'

# [적용]
# visited 초기값은 0, update 과정에서 큰 값이 들어갈 수 있음 => 초기값 -1로 해야함

# [수정]
# 1) q.appendleft() 사용해서 우선순위를 높여야함, 이동시간이 0이므로 이전 스텝과 동일한 우선순위
# 1-1) 가중치가 다른 bfs 문제의 경우, 큐를 여러개 만들어서 풀거나, deque & appendleft로 구현
# 2) visited 초기값 0 가능, visited[start]=1로 시작
#

from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    q = deque([N])
    visited[N] = 1 # 시작시 visited[2x]에 대한 구분을 위해 1을 init으로 설정, 출력에서 1 제외
    while q:
        x = q.popleft()
        if x==K:
            print(visited[x]-1)
            return
        for nx in [x-1, x+1, 2*x]:
            if 0<=nx<=10**5 and visited[nx]==0:
                if nx == 2*x:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x]+1
                    q.append(nx)

N, K = map(int, input().split())
visited = [0]*(10**5+1)
BFS()