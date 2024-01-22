from newsapi import NewsApiClient
from datetime import datetime, timedelta

# API 키 설정
api_key = '2d354d9f08384b26aafb95137606623c'
newsapi = NewsApiClient(api_key=api_key)

# 검색어 목록
search_terms = [
    "Korean bbq",
    "all you can eat korean bbq",
    "all you can eat shabu",
    "los angeles restaurant",
    "restaurant automation",
    "California labor law",
    "los angeles labor law",
    "california health inspection",

    ]

# 시작 날짜를 현재 날짜로부터 3일 전으로 설정
start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
# 현재 날짜 설정
current_date = datetime.now().strftime('%Y-%m-%d')

# 저장할 파일 이름 설정
file_name = 'news_search_results.txt'

# 중복된 기사 제목을 걸러내기 위한 세트
seen_titles = set()

# 파일에 결과를 저장하면서 화면에도 출력
with open(file_name, 'w') as file:
    for term in search_terms:
        # 지난 3일간의 기사 검색
        all_articles = newsapi.get_everything(q=term, from_param=start_date, to=current_date)
        search_results = f"Search results for '{term}' (from {start_date} to {current_date}):\n"
        file.write(search_results)
        print(search_results)
        for article in all_articles['articles']:
            if article['title'] not in seen_titles:  # 중복 제거 검사
                seen_titles.add(article['title'])
                article_info = f"- {article['title']} (Link: {article['url']})\n"
                file.write(article_info)
                print(article_info)
        file.write("\n")
        print("\n")
