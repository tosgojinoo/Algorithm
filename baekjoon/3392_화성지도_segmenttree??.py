###############################################
# segment tree
###############################################
def update(node, start, end, left, right, val):
    if end < left or start > right: return
    if left <= start and end <= right:
        cnt[node] += val # start +1, end -1
    else:
        mid = start + (end-start)//2
        update(node*2, start, mid, left, right, val)
        update(node*2+1, mid+1, end, left, right, val)
        # cnt = 0 # default value

    if cnt[node] > 0:
        seg[node] = end - start + 1
    else:
        # leaf node 는 합도 0 # if s == e 처리 해주면 seg, cnt 크기 *2 안 필요
        seg[node] = seg[node*2] + seg[node*2+1]

seg = [0] * 30001*2*4 # the total number of points in section not including overlap
cnt = [0] * 30001*2*4 # the total number of points in section, including overlap, 0 = no point, >1 = points exist

###############################################
# input & sort
###############################################
my_map = []
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    my_map.append((x1, y1, y2-1, 1)) # start
    my_map.append((x2, y1, y2-1, -1)) # end

my_map.sort() # sort based on x

###############################################
# sweep by using segment tree
###############################################
ans = 0

# first x
x, y1, y2, val = my_map[0]
update(1, 0, 30000, y1, y2, val) # val = start or end

# from second x
for i in range(1, N*2):
    x_diff = my_map[i][0] - my_map[i-1][0]
    ans += x_diff * seg[1] # the total number of points
    update(1, 0, 30000, my_map[i][1], my_map[i][2], my_map[i][3])

print(ans)