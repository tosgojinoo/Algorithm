def spiral(r, c):
    idx = max(abs(r), abs(c)) # x, y 각각의 절대값 중 큰 값이 껍질의 idx
    dist = abs(r - idx) + abs(c - idx)

    # 껍질의 오른쪽 아래 모서리의 값 = (2 * 껍질 index + 1)^2
    num1 = (2 * idx - 1) ** 2 + dist
    num2 = (2 * idx + 1) ** 2 - dist
    return num1 if c > r else num2


r1, c1, r2, c2 = map(int, input().split())
l = len(str(max(spiral(r1, c1), spiral(r1, c2), spiral(r2, c1), spiral(r2, c2)))) # 자리수 맞추기용
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(f"%{l}d" % spiral(i, j), end = " ")
    print()
