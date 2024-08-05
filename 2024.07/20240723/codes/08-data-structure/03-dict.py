# clear
person = {'name': 'Alice', 'age': 25}
person.clear()
print(person)
# get
person = {'name': 'Alice', 'age': 25}
print(person.get('name'))
print(person.get('country'))
print(person.get('country','unknown'))
# print(person['country']) # KeyError: 'country'

# keys
person = {'name': 'Alice', 'age': 25}
print(person.keys()) # dict_keys(['name', 'age'])
for item in person.keys():
    print(item)


# values
person = {'name': 'Alice', 'age': 25}
print(person.values())
for item in person.values():
    print(item)


# items
person = {'name': 'Alice', 'age': 25}
print(person.items()) #dict_items([('name', 'Alice'), ('age', 25)])
for item in person.items():
    print(item)
for key, value in person.items():
    print(key)
    print(value)

# pop # 키 제거, pop은 제거하고 항상 무언가를 반환
person = {'name': 'Alice', 'age': 25}
print(person.pop('age'))
print(person)
print(person.pop('coutry', None)) # None
# print(person.pop('country')) # KeyError: 'country'

# setdefault #있으면 조회하고, 없으면 추가하고 반환
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA')) # KOREA
print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}

# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)
person.update(age=100, coutry='KOREA')
print(person)


