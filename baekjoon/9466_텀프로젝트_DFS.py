# 한팀만도 가능
# 한명이 한명 선택, 자기자신 선택 가능
# cycle이 생성되면 한팀 완성


# [순서]
# arr[idx] == idx 인 경우 => 자기자신을 선택한 경우를 먼저 제외 (불필요)
# DFS
# 1) 지목된 사람이 자기자신 지목한 경우 => 종료 (불필요)
# 2) cycle이 형성되지 않은 경우 => 종료
# 3) ***** 중간에 내부 cycle이 생기는 경우 처리

# [출력]
# 어느 곳에도 속하지 않은 학생들의 수

# [제한]
# 복수 cycle 생성시 최외곽 cycle만 인정하는가? 아님 cycle 된 팀만 인정하는가? > 1:1이므로 복수 cycle 생성x
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x):
    global cycle, result
    visited[x] = 1
    cycle.append(x) # 사이클 가능 여부 확인1

    if visited[arr[x]] == 1: # 이전 방문한 곳으로 돌아온 것 확인
        if arr[x] in cycle: # 사이클 가능 여부 확인2
            result += cycle[cycle.index(arr[x]):] # 사이클이 완성되는 되는 구간부터만 저장
    else:
        DFS(arr[x])


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [False] + list(map(int, input().split()))
    visited = [1] + [0] * N
    result = []
    # 팀 완성되면 출력
    for i in range(1, N+1):
        if visited[i] == 0:
            cycle = []
            DFS(i)

    print(N-len(result)) # cycle 형성한 팀원 제외한 수
