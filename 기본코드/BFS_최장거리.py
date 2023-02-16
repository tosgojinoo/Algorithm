def bfs():
	s = 0
	e = 100
	# q에 초기 데이터 삽입, v[] 표시
	queue = []
	queue.append(s)

	visited = [0]*(V+1) # V: 노드 개수
	visited[s] = 1

	while queue:
		node = queue.pop(0)
		# 탈출 확인
		if node == e:
			return visited[e] - 1 # 시작이 1이었으므로

		for nnode in arr[node]: # 연결된 노드
			if not visited[nnode]:
				queue.append(nnode)
				visited[nnode] = visited[node]+1
	# 목적지를 방문하지 못한 경우
	return 0