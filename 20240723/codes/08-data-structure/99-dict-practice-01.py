# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    blood={'A':0, 'B':0, 'O':0, 'AB':0 }
    for i in range(len(blood_types)):
        if blood_types[i] =='A':
            blood['A'] +=1
        elif blood_types[i] =='B':
            blood['B'] +=1
        elif blood_types[i] =='O':
            blood['O'] +=1
        elif blood_types[i] =='AB':
            blood['AB'] +=1
    return blood

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}

# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    blood = {'A':0,'B':0,'O':0,'AB':0}
    for i in range(len(blood_types)):
        if blood.get('A') != blood_types.count('A'):
            blood['A'] +=1
        elif blood.get('B') != blood_types.count('B'):
            blood['B'] +=1
        elif blood.get('O') != blood_types.count('O'):
            blood['O'] +=1
        elif blood.get('AB') != blood_types.count('AB'):
            blood['AB'] +=1
    return blood 
        

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
