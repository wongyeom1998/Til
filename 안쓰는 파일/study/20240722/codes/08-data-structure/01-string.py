# find

# index

# isupper
string1 = 'HELLO'
string2 = 'hello'
print(string1.isupper())
# islower

# isalpha

# 문자열은 불변 데이터 타입이기 때문에 새로운 문자열을 반환해서
# 설명서에 대괄호는 선택적이라는 뜻

# replace
text = 'Hello, world! world world'
new_text = text.replace('world','python',1)
print(new_text)
# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)
# split
text = 'Hello, world!'
words = text.split(',')
words2= text.split()
print(words)
print(words2)
# join (split의 반대)
words = ['Hello', 'world!']
new_text=' '.join(words)
print(new_text)
# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)
# title
new_text2 = text.title()
print(new_text2)
# upper
# lower
# swapcase 대소문자 변경
new_text5 = text.swapcase()
print(new_text5)

#메서드는 이어서 사용 가능 100%는 아님
# 앞쪽에 반환값이 있어야 하고 앞쪽의 데이터 타입이 맞아야 됨 
# 문자열의 메서드, 리스트의 메서드
# 참고
# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
print("isdecimal() 메서드 예시:")
print("'12345'.isdecimal():", '12345'.isdecimal())
print("'123.45'.isdecimal():", '123.45'.isdecimal())
print("'-123'.isdecimal():", '-123'.isdecimal())
print("'Ⅳ'.isdecimal():", 'Ⅳ'.isdecimal())
print("'½'.isdecimal():", '½'.isdecimal())
print("'²'.isdecimal():", '²'.isdecimal())
print()

# isdigit() : 일반 숫자뿐만 아니라 지수 표현(²)도 True로 인식
print("isdigit() 메서드 예시:")
print("'12345'.isdigit():", '12345'.isdigit())
print("'123.45'.isdigit():", '123.45'.isdigit())
print("'-123'.isdigit():", '-123'.isdigit())
print("'Ⅳ'.isdigit():", 'Ⅳ'.isdigit())
print("'½'.isdigit():", '½'.isdigit())
print("'²'.isdigit():", '²'.isdigit())
print()

# isnumeric() : 일반 숫자, 로마 숫자, 분수, 지수 등 다양한 형태의 숫자 표현을 True로 인식
print("isnumeric() 메서드 예시:")
print("'12345'.isnumeric():", '12345'.isnumeric())
print("'123.45'.isnumeric():", '123.45'.isnumeric())
print("'-123'.isnumeric():", '-123'.isnumeric())
print("'Ⅳ'.isnumeric():", 'Ⅳ'.isnumeric())
print("'½'.isnumeric():", '½'.isnumeric())
print("'²'.isnumeric():", '²'.isnumeric())
