a = 3

if a > 3:
    print('3초과')
else:
    print('3이하')


dust = 480
if dust > 150:
    print('매우나쁨')
    if dust > 300:
        print('위험해요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')