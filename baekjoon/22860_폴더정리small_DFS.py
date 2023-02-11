''' my idea
N, M = 폴더 총 개수, 파일 총 개수
P 상위폴더, F 파일/폴더이름, C 폴더1/파일0
Q = 쿼리 개수
return 폴더 하위에 있는 파일의 종류의 개수와 총 개수
'''

import sys
sys.setrecursionlimit(10**6)

def DFS(name):
    files = [] # only file names under one foler

    if name not in doc: # 없는 파일/폴더명 일 경우
        cnt[name] = [0, 0]
        return files

    for lowers in doc[name]:
        nname, status = lowers
        if status == '0': # 파일일 경우
            files.append(nname) # 파일명 저장
        else:
            files = DFS(nname) + files

    cnt[name] = [len(set(files)), len(files)] # {folder name: [비중복 file 개수, 전체 파일 개수]}

    return files

doc = {} # {upper folder: [lower, status for file of folder]}
cnt = {} # {folder name: [비중복 file 개수, 전체 파일 개수]} <= 출력 대상

N, M = map(int, input().split())

for _ in range(N + M):
    upper, lower, status = input().split()
    if upper not in doc:
        doc[upper] = []
    doc[upper].append([lower, status])

DFS('main')

query = int(input())
for _ in range(query):
    path = input().split('/')
    c1, c2 = cnt[path[-1]]
    print(c1, c2)
