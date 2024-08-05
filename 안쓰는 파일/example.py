import requests
from pprint import pprint
#서울의 위도 37.56 경도 126.97

lat = 37.56
lon = 126.97
api_key = '74a7b1ce51bd89a8b6d24bb3a8c45386'



url= f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'


response = requests.get(url).json()
pprint(response)

# 데이터 중 온도를 파싱하시오.
