from newsapi import NewsApiClient
from datetime import datetime, timedelta

# API 키 설정
api_key = '2d354d9f08384b26aafb95137606623c'
newsapi = NewsApiClient(api_key=api_key)

# 검색어 목록
search_terms = [
    "Korean bbq",
    "restaurant news",
]

# 48시간 이내 날짜 설정
date_from = datetime.now() - timedelta(days=7)
date_from = date_from.strftime('%Y-%m-%dT%H:%M:%SZ')

# 현재 날짜를 얻어서 파일 이름 형식에 맞게 포맷팅
current_date = datetime.now().strftime("%Y_%m_%d")
file_name = f"/home/doitandy/report/romeo_new_{current_date}.txt"

# 파일에 결과를 저장
with open(file_name, 'w') as file:
    seen_titles = set()  # 중복 제목 추적을 위한 집합

    for term in search_terms:
        all_articles = newsapi.get_everything(q=term, from_param=date_from, to=datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'), language='en', sort_by='publishedAt')

        # 화면에 결과 출력 및 파일에 저장
        file.write(f"Search results for '{term}' in the last 48 hours:\n")
        print(f"Search results for '{term}' in the last 48 hours:")
        
        for article in all_articles['articles']:
            if article['title'] not in seen_titles:
                seen_titles.add(article['title'])
                print(f"- {article['title']}")
                file.write(f"- {article['title']}\n")
        file.write("\n")

print(f"Report saved to {file_name}")

