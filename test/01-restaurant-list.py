kind = input ("한식, 중식, 양식 중 선택하세요.")

import random

korean_food = ["라온", "가연", "곳간", "정식당"]
chinese_food = ["화상손만두", "맛이차이나", "대가방", "하하"]
western_food = ["돈파스타", "닐리비스트로", "그란데", "다린"]

if kind == '한식':
    print(random.choice(korean_food))

if kind == '중식':
    print(random.choice(chinese_food))

if kind == '양식':
    print(random.choice(western_food))
