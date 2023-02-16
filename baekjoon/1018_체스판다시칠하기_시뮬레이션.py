''' my idea
memory[2(B or W)][M][N] 구성 -> X => DP 방식 아니라, 계산 후 바로 결과에 반영 후 휘발
MxN 행렬을 전부 탐색 -> X => N-7, M-7 까지만 탐색
  - 시작 지점이 B일 때, W일 때
      - 그 자리에, 바꿔야 하는 색 memory에 기록
          - for 0~7, BW 번갈아 가며 각 열 확인
          - B로 시작할 경우, 0열 BWBWBWBW, 1열 WBWBWBWB, ... 7열까지
min(memory) 출력
'''
N, M = map(int, input().split())
arr = []
result = []

for _ in range(N):
    arr.append(input())

for y in range(N - 8 + 1):
    for x in range(M - 8 + 1):
        draw1, draw2 = 0, 0 # 'B' / 'W' 각각으로 시작했을 때 cnt

        for py in range(y, y + 7 + 1):
            for px in range(x, x + 7 + 1):
                if (py + px) % 2 == 0: # 좌표의 합으로 패턴 선정
                    if arr[py][px] != 'B':
                        draw1 += 1
                    if arr[py][px] != 'W':
                        draw2 += 1
                else:
                    if arr[py][px] != 'W':
                        draw1 += 1
                    if arr[py][px] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))