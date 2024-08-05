# 데코레이터 : 함수를 꾸미는 함수 > 기능을 추가 잠깐
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    @classmethod
    def num_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')
# 하위 클래스 > 상속
# 클래스 메서드를 호출하는 클래스가 인자로 들어오게 됨
person1 = Person('iu')
person2 = Person('BTS')

Person.num_of_population() 