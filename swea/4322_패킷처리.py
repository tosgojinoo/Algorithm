def DFS(packet_idx):
    # DFS level 제한
    if packet_idx == len(arr): # 이미 packet 처리 완료 상태
        return True

    # 세팅1: 대상 선택. for 편리함.
    packet = arr[packet_idx]

    # 세팅2: delay 계산
    # 해당 packet 진입 당시, cpu 잔량과의 차이로 delay 계산
    for i in range(cpu_num): # cpu 종료시간을 일일히 비교
        if cpu_height[i] > packet[0]: # packet 입력 시간이 cpu 종료 시간 보다 빠를 경우 == 대기가 필요할 경우
            delay[i] = cpu_height[i] - packet[0] # 대기 시간 저장

    # 세팅3: visited 계산
    # packet_idx와 delay 상태 배열의 조합을 visited로 처리. list가 아닌 dict인 이유는, 시간복잡성 감소 위해.
    key = tuple([packet_idx] + sorted(delay))
    if key in visited:
        return False
    visited[key] = True

    # DFS
    # 몇번 cpu_num에서 처리할 지 루프 처리
    for i in range(cpu_num):
        # 초기값. 해당 cpu_num에서 처리 할수도, 안 할수도 있기 때문.
        tmp = cpu_height[i]
        # delay 처리 방식과 유사하게 다시 한번 확인
        if cpu_height[i] > packet[0]: # 대기. packet 입력 시간이 cpu 종료 시간 보다 늦을 경우.
            if cpu_height[i] - packet[0] + packet[1] <= 10: # 제한 조건: 대기시간 + 신규 packet의 처리 종료 시간이 최종 종료 제한 시간 이하일 경우
                cpu_height[i] += packet[1] # 대기 후 처리 완료한 시간을 cpu 종료 시간에 입력
            else:
                continue # 종료 제한 시간을 넘어갈 경우. 무시
        else:
            cpu_height[i] = packet[0] + packet[1]  # 대기 불필. 바로 cpu 종료 시간에 추가

        # 연달아 모든 packet 확인
        if DFS(packet_idx + 1): # 다음 패킷에 대해 DFS 결과가 True일 경우
            return True
        # 이번 cpu_num에서는 처리 못했기 때문에, 원복 후 다음 cpu_num 이동
        cpu_height[i] = tmp  # 처리 못했을 경우 원복
    return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # [[도착시간, 길이]]
    # 제출답 == cpu 최소 개수
    answer = -1
    # 조건 증가하며 DFS
    for cpu_num in range(1, 5 + 1):
        # 초기값
        cpu_height = [0] * cpu_num
        delay = [0] * cpu_num
        visited = {}
        # DFS 시작
        if DFS(0):  # DFS 전체 검색 후 True 라면 저장
            answer = cpu_num
            break # 자동으로 최소값 채택

    print(f'#{tc} {answer}')

'''
# 참고
def DFS(test_idx):
    if test_idx == len(arr):
        return True

    test = arr[test_idx]

    for i in range(len(cpu_height)):
        if cpu_height[i] > test[0]:
            lst_delay[i]= cpu_height[i]-test[0]

    rep=tuple([test_idx]+sorted(lst_delay))
    if rep in visit:
        return False

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

        if DFS(test_idx + 1):
            return True
        cpu_height[i] = old_cpu_height
    return False


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각 처리
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = -1
    for cpu_num in range(1, 5+1):
        cpu_height = [0] * cpu_num
        lst_delay = [0] * cpu_num
        visit = {}
        if DFS(0):
            answer = cpu_num
            break

    print(f'#{test_case} {answer}')
'''


'''
# 참고
def DFS(test_idx):
    if test_idx == len(arr):
        return True
 
    test = arr[test_idx]
    
    for i in range(len(cpu_height)):
        if cpu_height[i] > test[0]:
            lst_delay[i]= cpu_height[i]-test[0]
 
    rep=tuple([test_idx]+sorted(lst_delay))
    if rep in visit:
        return False

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
 
        if DFS(test_idx + 1):
            return True
        cpu_height[i] = old_cpu_height
    return False
 
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각 처리
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    answer = -1
    for cpu_num in range(1, 5+1):
        cpu_height = [0] * cpu_num
        lst_delay = [0] * cpu_num
        visit = {}
        if DFS(0):
            answer = cpu_num
            break
 
    print(f'#{test_case} {answer}')
'''