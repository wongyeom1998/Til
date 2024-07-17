# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요 {name}님! {age}살이시군요')

greet('harry', 20)
greet(20, 'harry')
# 특정한 값이 누락되면, 에러가 뜸

# 2. Default Argument Values
# 매개변수에 기본 값을 할당하는 것
# 함수 호출시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
def greet(name, age=20):
    print(f'안녕하세요 {name}님! {age}살이시군요')

greet('bob')
# 3. Keyword Arguments
# 함수를 호출할 때 사용법
# 단, 호출시 키워드 인자는 위치 인자 뒤에 위치해야 함

def greet(name, age):
    print(f'안녕하세요 {name}님! {age}살이시군요')


# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)

calculate_sum(1, 100, 5000, 30)
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)

print_info(name = 'eve')

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
