'''
itertools를 제외하고, 단순 반복문이 가장 빠름
'''
# 1
def r_combination(num):
    if len(num) == R:
        return
    for nxt in can_touch:
        touch_list.append(list(map(int, num+str(nxt))))
        if num+str(nxt) != '0': # 추가 조건: 맨 처음이 '0'인 경우 재귀 제외
            r_combination(num+str(nxt))

can_touch = [0, 1, 2, 3, 4, 7]
touch_list = []
R = 3 # 3번 선택
r_combination('') # init
print(touch_list)
print(len(touch_list))

# 2
def permutation_repetition(now):
  global picked
  if now == R:
    tmp = ''.join(picked)
    if tmp != '':
      tmp = str(int(tmp)) # 추가 조건: '0' 만 연속으로 앞에 있을 경우 자동 처리
      if tmp not in touch_list:
        touch_list.append(tmp)
    return
  else:
    for i in range(len(can_touch)):
      picked[now] = str(can_touch[i])
      permutation_repetition(now+1)

can_touch = [0, 1, 2, 3, 4, 7]
picked = ['']*3
touch_list = []
can_touch.append('')
# 계산범위 0~999, 숫자 조합은 최대 3자리
R = 3 # 3번 선택
permutation_repetition(0) # init
print(touch_list)
print(len(touch_list))