def bfs(s, e):
	# q, v[] 생성, 필요 변수 선언
	q = []
	v = [0]*(V+1) # V: 노드 개수

	# q에 초기 데이터 삽입, v[] 표시
	q.append(s)
	v[s] = 1

	while q:
		c = q.pop(0)
		# 탈출 확인
		if c==e:
			# 정답 처리는 이곳에서..
			return v[e]-1 # 시작이 1이었으므로

		for n in adj[c]: # 연결된 노드
			if v[n]== 0:
				q.append(n)
				v[n]=v[c]+1
	# 목적지를 방문하지 못한 경우
	return 0