# 참고, 정답
T = int(input())
N = int(input())
boxes = []
for i in range(N):
    box=list(map(int, input().split()))
    boxes.append([box[0],box[1],box[2],i])
    boxes.append([box[1],box[2],box[0],i])
    boxes.append([box[2],box[0],box[1],i])

boxes=sorted(boxes,key=lambda x: x[0]*x[1])

height=[box[2] for box in boxes]
visit=[[box[3]] for box in boxes]

for i in range(3*N):
    for j in range(i-1,-1,-1):
        if boxes[i][3] in visit[j]:
            continue
        if (boxes[i][0] >= boxes[j][0] and boxes[i][1] >= boxes[j][1]) or (boxes[i][0] >= boxes[j][1] and boxes[i][1] >= boxes[j][0]):
            if height[i] < boxes[i][2] + height[j]:
                height[i]=boxes[i][2] + height[j]
                visit[i]= visit[j]+ [boxes[i][3]]

answer=max(height)
print(f'{answer}')



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