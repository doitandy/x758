import requests
from datetime import datetime

# API 키 설정
api_key = '953bdbeff06e0f4775c212598669086b'

# 오늘 날짜 설정
today = datetime.now().strftime('%Y-%m-%d')

# API 요청을 위한 URL 구성
url = (f"http://api.mediastack.com/v1/news"
       f"?access_key={api_key}"
       f"&keywords=AI"
       f"&languages=en"
       f"&sort=published_desc"
       f"&countries=us"
       f"&date={today}")

# API 요청 실행
response = requests.get(url)

# 응답 확인
if response.status_code == 200:
    data = response.json()
    if data['data']:
        # 뉴스 데이터 출력
        for article in data['data']:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("------")
    else:
        print("오늘자 인공지능(AI) 관련 뉴스가 없습니다.")
else:
    # 오류 발생
    print(f"Error: {response.status_code}, Response: {response.text}")

