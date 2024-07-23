# 빈 세트를 만들려면
# a = {}
# b = set()

# add
my_set = {'a', 'b', 'c', 1, 2, 3}
# 얘들은 나열되어 있을 뿐, 순서가 없다.
my_set.add(4)
print(my_set)

# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)
# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove(2)
# print(my_set)
# my_set.remove(10) # 오류

# pop
my_set = {'a', 'b', 'c', 1, 2, 3}

element = my_set.pop()
print(element)

# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)
my_set.discard(10)
print(my_set.discard(10))


# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1,4,5])
print(my_set) # {'b', 2, 3, 1, 4, 5, 'a', 'c'}



# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1. issubset(set2))
print(set3.issubset(set1))
print(set1.issuperset(set2))
print(set1.union(set2))