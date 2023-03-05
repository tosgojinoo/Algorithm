'''
[설명]
N×M 배열,
왼쪽, 오른쪽, 아래쪽 이동, 위쪽 불가 -> 아래로만 전전하는 방식 -> (max(좌 or 위)+현재) vs (max(위 or 우)+현재) 비교 후 저장
재방문 불가
각 지역의 탐사 가치
(1, 1) -> (N, M) 이동

[문제]
탐사 지역 가치 최대합
'''
'''
[알고리즘]
- DP
    - (위로) 재탐색 없음
    - 상향식 -> for 루프 사용
- 재방문 & 위방향 불가(단방향)
    - (max(좌 or 위)+현재) vs (max(위 or 우)+현재) 비교 후 저장
'''
'''
[구조]
- arr 입력
- r_tmp, l_tmp 
    - 왼쪽에서부터의 DP값, 오른쪽에서부터의 DP값 저장
- ans 
    - 현재 행 DP값 저장
    - 이전 행 DP값 참조
- 첫 행 오른쪽으로 누적값 저장
- for 행 루프
    - 다음 행 입력
    - 오른쪽 이동 init. 위 + 자신(맨 왼쪽). 맨 왼쪽에서 바로 내려 왔을 때.
    - 왼쪽 이동 init. 위 + 자신(맨 오른쪽). 맨 오른쪽에서 바로 내려 왔을 때.
    - for (1~M-1) 열 루프
        - max(위에서 온 것 vs 왼쪽에서 온 것) + 현재값
        - max(위에서 온 것 vs 오른쪽에서 온 것) + 현재값
    - for (0~M-1) 열 루프
        - 왼쪽에서 시작 vs 오른쪽에서 시작. 비교하여 각 지점에서 큰 값 저장.
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # N x M. idx 1 시작.
arr = list(map(int, input().split())) # 첫줄 입력
rtemp = [0]*M # 열 개수와 동일
ltemp = [0]*M # 열 개수와 동일
ans = [0]*M # 열 개수와 동일
ans[0] = arr[0]

for i in range(1, M):
    ans[i] = arr[i] + ans[i-1] # 오른쪽으로 누적값 저장. 첫 줄은 무조건 오른쪽으로 이동.

for _ in range(N - 1):
    arr = list(map(int, input().split())) # 다음 행 입력
    rtemp[0] = ans[0] + arr[0] # 오른쪽 이동 init. 위 + 자신(맨 왼쪽). 맨 왼쪽에서 바로 내려 왔을 때.
    ltemp[-1] = ans[-1] + arr[-1] # 왼쪽 이동 init. 위 + 자신(맨 오른쪽). 맨 오른쪽에서 바로 내려 왔을 때.
    for i in range(1, M):
        rtemp[i] = max(ans[i], rtemp[i-1]) + arr[i] # max(위에서 온 것 vs 왼쪽에서 온 것) + 현재값
        ltemp[-i-1] = max(ans[-i-1], ltemp[-i]) + arr[-i-1] # max(위에서 온 것 vs 오른쪽에서 온 것) + 현재값
    for i in range(M):
        ans[i] = max(rtemp[i], ltemp[i]) # 왼쪽에서 시작 vs 오른쪽에서 시작. 비교하여 각 지점에서 큰 값 저장.
print(ans[M-1])
