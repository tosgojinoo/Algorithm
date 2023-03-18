[Brute force]
- 시작점 조건이 없어, 특정할 수 없음
- 재방문 x -> 아래/오른쪽 이동 경우만 계산 -> BFS/DFS 아니고 Brute force 
- 범위 탐색 -> 교환 -> 계산 -> 원복 (visited 미사용)

[DFS]
- 그룹 번호 매기기
  - visited 에 그룹 idx 표기



[BFS]
- queue
  - 기본적으로 deque 사용
    - queue.popleft()
  - 필요시 list queue 사용
    - queue.pop()
    - min(queue) + queue.remove(value)
- 추가 queue
  - while 루프에 사용되는 queue 외에, 정산시 계산 이력 활용 용도로 추가 deque 사용
  - 굳이 단일 queue 사용하지 말기
- 0-1 BFS
  - 가중치가 유리한 경우를 먼저 삽입(appenleft), 일반은 뒤에 삽입(append) 하는 BFS
- 최소 문열기(BOJ 9376)
  - visited
    - init -1
    - memory 기능 추가(문 여는 개수)
  - visited 들의 합이 최소가 되는 지점 찾기
    - 벽 제외
    - 문이라면 -2(3명중에 1명만 열면 되니 때문에 2인분 차감) 적용
- map 이동 탐색
- 최대 개수
  - 보통 "최대 경우의 수"는 DFS 처리하지만, 
  - "map 탐색 및 최대 결과물 확보" 의 경우, "BFS + (조건 변화시)visited 초기화" 방식 적용


[Dijkstra]
- 양방향(무방향) 그래프
- 모든 node를 갈 필요 없이, 최소 비용(시간)으로 목표 지점까지의 이동
- heapq
  - heapq.heappush(queue, [weight, 그외 변수들])
  - while queue:
    - heapq.heappop(queue)


[Kruskal]
- MST 계산
- edges 계산
  - 그룹(or node) 간 거리 계산 필요시
  - 가능한 모든 위치에서 거리 계산 조건에 따라 계산 후
  - edges 추가
    - (dist, country_idx, visited[ny][nx]) 
    - 거리 == weight


[memory]
- 필요한 경우 모든 케이스에 대해 관리
- dict 의 경우 tuple 을 key 적용 가능
- idx 활용
  - 경우의 수가 숫자인 경우
  - idx: 경우의 수, value: 매핑값 
- 우선순위 조건이 많음 & 배열 내용도 함께 참고해야할 때
  - tuple로 한번에 묶어 활용 가능
  - max(max_block, (len(queue), len(rainbow), i, j, queue)) 
- 인접한 빈칸 수에 따른 우선순위 적용
  - 계산 중에 매번 인접 빈칸 수를 계산하게 되면 계산량 증가
  - 빈칸 개수 초기값 설정
    - 각 모서리(2): if j in (0, (N - 1)) for i, j in (0, (N-1))
    - 나머지 가장자리(3): else arr[j][i], arr[j][i]
    - 내부(4)
  - 계산 진행하며 빈칸 줄어들때마다 갱신
- 중복 저장
  - 탐색 루프 정산시, 중복 저장량이 많으면 우선순위 증가로 활용
- buffer
  - 필요 조건 만족 시키기 위한 누적값 기준이 있을 경우(길이, 무게, 가격, 연료)
  - buffer에 쌓고, 해소가 필요한 시점에서 해소 여부 확인



[visited]
- 상태차원
  - 빨간/파란 구슬 위치 
  - rx x ry x bx x by
    - [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)] 
- visited + cnt 방식



[방향]
- 순서
  - 문제에서 정해진 순서 따르기
- dxy +/- 90도 회전
  - 회전할 경우 +/- 1이므로, 감안한 순서 설정.
  - 270도 == 90도 * 3
  - (direction +/- 1) % 4
- dxy 180 회전
  - (direction + 2)%4
- 현재 방향별, 다음 방향 매핑 리스트
  - idx: 현재 방향, value: 다음 방향
- 문제 내에 2종 dxy 필요시
  - 서로의 연관성 사전 분석
  - 필요에 따라, mapping list 구성
- 우선순위
  - BFS/DFS 탐색 시, 다음 좌표 선정에 우선순위 있을 경우
  - "for dxy in direction"에서 우선순위를 감안한 direction 구성
- arr +90도
  - transpose
  - list(*zip(*arr))
- arr -90도
  - transpose > reverse
  - reversed(list(map(list, zip(*arr))))
- arr +180도
  - (y, x) -> (-y, x) or (y, -x)
- arr 일부분 회전(90도)
  - N - 1 - 회전 전의 행 번호 (r 역순) -> dr = 회전 후의 열 번호
  - 회전 전의 열 번호 (c 정순) -> dc = 회전 후의 행 번호
  - arr[i + (s -1 -x)][j + y] -> arr_new[i + y][j + x]


[패턴]
- 체스판
  - (ny + nx) % 2
    - 기준점부터 짝수 거리 지점은 색 동일. 홀수 거리는 반대

- shell
  - shell idx 별 최대값
    - idx 0:  1 == 1^2
    - idx 1:  9 == 3^2
    - idx 2: 25 == 5^2
    - idx 3: 49 == 7^2
    - (idx*2 + 1)^2
      - 오른쪽 아래 모서리 값
  - idx r, c 중 절대값이 큰 수가 shell idx
  - (r,c)의 값 계산
    - shell 내 최대값부터의 상대 거리
    - dist == |shell idx - r/c| 의 합
    - 오른쪽, 윗면 (c > r 경우)
      - 이전 shell 최대값에서 거리만큼 증가
      - (2 * idx - 1) ** 2 + dist
    - 왼쪽, 아랫면 (c <= r 경우)
      - shell 내 최대값에서 거리만큼 차감
      - (2 * idx + 1) ** 2 - dist
  - 회전하며 중심에서부터 확장
    - 방향 전환 전까지의 연속 칸수(직선길이)는, 2개씩 묶어서 증가 계산
    - [i//2 for i in range(2, N*2)]
  - shell 방향과 다른 패턴 조합될 경우
    - 1D로 변환 구성 활용
  - shell + vertical/horizontal 교차점 계산
    - shell개수 = N//2. 4방 번걸아가며 계산
    - (북 -> 서), (서 -> 남) 전환시 증분 +1씩 복합 증분 

- 충돌 평가
  - vert/hori
    - 외곽 제한 관리용
    - 이미 그려진 선분(제한) 들을 veri, hori 리스트에 각각 저장
    - vert
      - [(bar_x_min, bar_x_max, bar_y)]
      - 초기값 [(0, N, -1), (0, N, N)]
    - hori
      - [(bar_y_min, bar_y_max, bar_x)]
      - 초기값 [(0, N, -1), (0, N, N), (L, L, L)]
      - (L, L, L) 은 시작점, 오른쪽으로 먼저 시작 & 검사범위 [:-1] 때문에 설정
    - 검사시 사용은 항상 [:-1] 범위만
      - 항상 +/- 90도 회전을 하기 때문에, 바로 전에 추가한 조건은 제외
    - 크로스 여부 확인
      - 서로의 길이가, 서로의 위치 지점을 포함하는지 확인 
      - bar_y_min <= y <= bar_y_max and minX <= bar_x <= maxX 

- padding
  - 외곽에 한겹 더 쌓기
  - ['.' + input() + '.' for _ in range(H)]
  - case
    - 외부를 자유롭게 이동 가능할 경우
    - 외부를 벽 처리하여, 방향 탐색시 범위 조건 제외 

- 아래로 전진하면 행에서의 최대값 누적
  - 위쪽 불가 -> 좌/우/아래로만 전진하는 방식
  - (max(좌 or 위)+현재) vs (max(위 or 우)+현재) 비교 후 저장

- 블록 쌓기
  - 한칸씩 이동 적용 x
  - 열별 탐색 후 가장 높은 행값 리턴 함수 구성
    - '리턴값 + 1' 에 블록 위치
  - 
- weight
  - 연료: 단가 계산, 적용
  - 거리
  - 비용


[while]
- 방향 * 속도 이동일 경우
  - 제한(충돌) 조건 전까지 적용


[arr]
- 중력 적용
  - for 탐색 역순
- 4방 끝단이 반대편과 이어지는 주기 회전 방식
  - (x % 총길이) 수식 적용
  - 행: (r + dis*dx[dir]) % n 
  - 열: (c + dis*dy[dir]) % n
- 조건 만족시 요소+1
  - [l + (l == 조건) for l in arr]
- 뺀 값이 음수일 경우 0처리
  - [i-B if i-B >=0 else 0 for i in arr]


[출력]
- 최대 자리수 맞춰 이쁘게 출력
  - print(f"%{print_len}d" % spiral(i, j), end = " ")