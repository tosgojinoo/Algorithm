abs
chr
divmod
enumerate
filter
ord

# [변환 or 확인]
str.upper(): 문자열을 대문자로 변경
str.lower(): 문자열을 소문자로 변경
str.isupper(): 문자열이 대문자인지 확인
str.islower(): 문자열이 소문자인지 확인
str.swapcase()	대문자는 소문자로, 소문자는 대문자로 변환합니다	string.swapcase()
str.title() 각 단어의 앞글자만 대문자로 변환합니다. 만약 각 단어 중간에 대문자가 있다면 소문자로 변환됩니다.
string.isdigit() # only 숫자
string.isalpha() # only 문자
string.isalnum() # only 숫자, 문자
string.isspace() # only 공백

# [문자열 찾기]
string.find("찾을 문자열")
string.rfind("찾을 문자열")
string.index("찾을 문자열")
string.rindex("찾을 문자열")
string.startswith("찾을 문자열")
string.endswith("찾을 문자열")

# [공백 삭제]
string.strip()
string.rstrip()
string.lstrip()
string.replace("기존 문자열","새 문자열")

# [list 관련]
list.insert(index, value) # index 자리에 value 삽입
list.pop() # 가장 끝에 있는 요소 제거
list.pop(idx)
list.remove(value) # value == tuple() 도 가능
list.count(value)
list.index(value)

# [set 관련]
set1.add(set2)

# [입력 형태]
## 개별 입력
- map(int, input().split())
## 123456789
- [list(map(int, list(input()))) for _ in range(N)]
## 1 100 2 50 60 3 5 6 7 8
- [list(map(int, input().split())) for _ in range(N)]
## #..B#
- [list(input().strip()) for _ in range(N)]
## padding
- ['.' + input() + '.' for _ in range(H)]
## 뺀 값이 음수일 경우 0처리
- [i-B if i-B >=0 else 0 for i in arr]