from collections import defaultdict

def DFS(name):
    global collection
    global count
    if name in folder:
        for nname in folder[name]:
            if nname in file:
                collection.update(file[nname])
                count += len(file[nname])
            if nname in folder:
                DFS(nname)


answer = []
N, M = map(int, input().split())
file = defaultdict(set)
folder = defaultdict(set)
for _ in range(N + M):
    upper, lower, isFolder = input().split()
    if int(isFolder) > 0:
        folder[upper].add(lower)
    else:
        file[upper].add(lower)

move = []
K = int(input())
for _ in range(K):
    before, after = input().split()
    before = before.split('/')[-1]
    after = after.split('/')[-1]
    move.append([before, after])

for before, after in move:
    if not before in folder:
        pass
    elif not after in folder:
        folder[after] = folder[before]
        del folder[before]
    else:
        folder[after].update(folder[before])
        del folder[before]
    if not before in file:
        pass
    elif not after in file:
        file[after] = file[before]
        del file[before]
    else:
        file[after].update(file[before])
        del file[before]

query = []
Q = int(input())
for _ in range(Q):
    a = input()
    a = a.split('/')[-1]
    query.append(a)

for name in query:
    count = 0
    collection = {0}

    if name in file: # 파일일 경우만 해당
        count = len(file[name])
        collection.update(file[name])

    DFS(name)
    print(len(collection) - 1, end = ' ')
    print(count)