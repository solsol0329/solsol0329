dust = 305

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요!')
# dust가 150이하인 경우만 elif에서 평가
# dust > 80 and dust <= 150 의미
elif dust > 80: 
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')