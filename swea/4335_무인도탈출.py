# 참고, 정답
for tc in range(int(input())):
    N = int(input())
    arr = []
    for i in range(N):
        box = list(map(int, input().split()))
        # 3방향 경우의 수 모두 선택
        arr.append([box[0], box[1], box[2], i])
        arr.append([box[1], box[2], box[0], i])
        arr.append([box[2], box[0], box[1], i])

    arr = sorted(arr, key=lambda x: x[0]*x[1]) # 앞 두 숫자로 구성한 넓이 작은 순으로 정렬
    DP = [box[2] for box in arr] # 높이 모음. 답까지 누적해 갈 것은 높이.
    visited = [[box[3]] for box in arr] # 선택한 이력 관리

    for i in range(3*N):
        for j in range(i-1, -1, -1): # i보다 작은 수 j. i==0은 자동 제외됨.
            if arr[i][3] in visited[j]: # 자기자신 or 이전에 선택된 경우, 무시
                continue
            if (arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1]) or (arr[i][0] >= arr[j][1] and arr[i][1] >= arr[j][0]): # i박스가 j박스 대비, 가로/세로 이상 or 가로<->세로 교환 후 비교도 이상
                if DP[i] < DP[j] + arr[i][2]: # i단일 + (j까지의 누적) 이 (i까지의 누적) 보다 클 경우
                    DP[i] = DP[j] + arr[i][2] # 추가
                    visited[i] = visited[j] + [arr[i][3]] # 선택된 경우의 수 모두 저장

    answer = max(DP)
    print(f'#{tc+1} {answer}')



# # 33/50 개만 정답
'''
def DFS(now, end): # limit 개수 이하 전부 뽑기, 순서 무시
    global picked, box_idxs, heights
    # 기본 조건
    if (now==end+1):
        result.append(sum(heights))
        return        
    else:
        if visited[now] == 0:
            visited[now]=1
            if len(picked) <1:
                picked.append(data[now])
                box_idxs = box_idxs + [data[now][-1]]
                heights[now] = heights[now] + data[now][2]
                DFS(now+1, end)
                picked = picked[:-1]
                box_idxs = box_idxs[:-1]
                heights[now] = heights[now] - data[now][2]
            else:
                if data[now][-1] not in box_idxs:
                    if (picked[-1][0] >= data[now][0] and picked[-1][1] >= data[now][1]) or (picked[-1][1] >= data[now][0] and picked[-1][0] >= data[now][1]):
                        # if heights[now] < heights[now] + data[now][2]():
                        picked.append(data[now])
                        box_idxs = box_idxs + [data[now][-1]]
                        heights[now] = heights[now] + data[now][2]
                        DFS(now+1, end)
                        picked = picked[:-1]
                        box_idxs = box_idxs[:-1]
                        heights[now] = heights[now] - data[now][2]
            DFS(now+1, end)
            visited[now]=0



T = int(input())
for tc in range(1, T+1):
    boxes = []
    N = int(input())
    for i in range(N):
        box=list(map(int, input().split()))
        boxes.append([box[0],box[1],box[2],i])
        boxes.append([box[1],box[2],box[0],i])
        boxes.append([box[2],box[0],box[1],i])

    data = sorted(boxes, key=lambda x:x[0]*x[1], reverse=True)
    visited = [0] * N*3
    box_idxs = []
    picked = []
    heights = [0] * N*3
    result = []
    DFS(0, len(data)-1)
    print(f'#{tc} {max(result)}')
'''