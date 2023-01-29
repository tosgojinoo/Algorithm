def DFS(packet_idx):
    # DFS level 제한
    if packet_idx == len(packets): return True # 전체 packet 길이와 현 packet index가 동일할 경우, 더이상 계산 x

    # 대상 선택
    packet = packets[packet_idx]

    # 갱신값: level별 delay값
    for i in range(len(cpu_height)): # cpu 종료시간을 일일히 비교
        if cpu_height[i] > packet[0]: # packet 입력 시간이 cpu 종료 시간 보다 늦을 경우 == 대기가 필요할 경우
            delay[i] = cpu_height[i] - packet[0] # 대기 시간 저장
    
    # 방문 flag
    rep = tuple([packet_idx] + sorted(delay))
    if rep in visited: return False
    visited[rep] = 1

    # 검색 조건
    for i in range(len(cpu_height)):
        # backtracking의 위한 초기값 저장
        old_cpu_height = cpu_height[i]
        # update
        if cpu_height[i] > packet[0]: # packet 입력 시간이 cpu 종료 시간 보다 늦을 경우 == 대기가 필요할 경우
            # 문제 제한 조건
            if cpu_height[i] - packet[0] + packet[1] <= 10: # 대기시간 + 신규 packet의 처리 종료 시간이 최종 종료 제한 시간 이하일 경우
                cpu_height[i] = cpu_height[i] + packet[1] # 대기 후 처리 완료한 시간을 cpu 종료 시간에 입력
            else: continue # 대기가 필요한데, 종료 제한 시간을 넘어갈 경우, 다음으로
        else: cpu_height[i] = packet[0] + packet[1] # 대기가 필요 없을 경우, 바로 cpu 종료 시간에 추가
        
        if DFS(packet_idx + 1): return True # 다음 패킷에 대해 dfs 결과가 True일 경우

        # backtracking 후 초기값 복원
        cpu_height[i] = old_cpu_height # 처리 못했을 경우 원복
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    packets = [list(map(int, input().split())) for _ in range(N)]
    # 제출답 == cpu 최소 개수
    answer = -1
    # 조건 증가하면 DFS
    for cpu_num in range(1, 5+1):
        # 초기값
        cpu_height = [0] * cpu_num
        delay = [0] * cpu_num
        visited = {}
        packet_idx = 0

        # DFS 시작
        if DFS(packet_idx): # dfs 전체 검색 후 True 라면 저장
            answer = cpu_num
            break

    print(f'# {tc} {answer}')

# 참고
def dfs(test_idx):
    if test_idx == len(tests): return True
 
    test = tests[test_idx]
    
    for i in range(len(cpu_height)):
        if cpu_height[i] > test[0]:
            lst_delay[i]= cpu_height[i]-test[0]
 
    rep=tuple([test_idx]+sorted(lst_delay))
    if rep in visit: return False
    visit[rep]=1
 
    # print(test_idx)
    for i in range(len(cpu_height)):
        old_cpu_height = cpu_height[i]
        if cpu_height[i] > test[0]:
            if cpu_height[i] - test[0] + test[1] <= 10:
                cpu_height[i] = cpu_height[i] + test[1]
            else:
                continue
        else:
            cpu_height[i] = test[0] + test[1]
 
        if dfs(test_idx + 1):
            return True
        cpu_height[i] = old_cpu_height
    return False
 
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    tests = [list(map(int, input().split())) for _ in range(N)]
 
    answer = -1
    for cpu_num in range(1, 5+1):
        cpu_height = [0] * cpu_num
        lst_delay = [0] * cpu_num
        visit = {}
        if dfs(0):
            answer = cpu_num
            break
 
    print(f'#{test_case} {answer}')