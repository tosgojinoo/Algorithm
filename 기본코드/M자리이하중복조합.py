# 1
def comb(num):
    if len(num) == 3:
        return
    for i in range(N):
        touch_list.append(num+str(can_touch[i]))
        if num+str(can_touch[i]) != '0':
            comb(num+str(can_touch[i]))

M = int(input())
can_touch = list(map(int, input().split()))
touch_list = []
comb('')

# 2
def permutation_repetition(now, end):
  global picked
  if now == end :
    tmp = ''.join(picked)
    if tmp != '':
      tmp = str(int(tmp))
      if tmp not in touch_list:
        touch_list.append(tmp)
    return
  else:
    for i in range(len(can_touch)):
      picked[now] = str(can_touch[i])
      permutation_repetition(now+1, end)

M = 3
can_touch = list(map(int, input().split()))
picked = ['']*3
touch_list = []
can_touch.append('')
# 계산범위 0~999, 숫자 조합은 최대 3자리
permutation_repetition(0, M)