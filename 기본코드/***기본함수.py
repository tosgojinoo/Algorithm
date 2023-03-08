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
list.insert(index, data) # index 자리에 data 삽입
list.pop() # 가장 끝에 있는 요소 제거
list.pop(idx)

# [set 관련]
set1.add(set2)