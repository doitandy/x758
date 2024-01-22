from newsapi import NewsApiClient
import datetime

# NewsAPI 클라이언트 초기화
newsapi = NewsApiClient(api_key='2d354d9f08384b26aafb95137606623c')

# 현재 시간을 기준으로 48시간 이전의 날짜 계산
date_from = datetime.datetime.now() - datetime.timedelta(days=2)

# 'artificial intelligence'에 대한 검색 수행
all_articles_en = newsapi.get_everything(q='artificial intelligence',
                                         from_param=date_from,
                                         language='en',
                                         sort_by='publishedAt',
                                         page_size=100)

# 중복 기사 제거를 위한 함수
def remove_duplicates(articles):
    unique_articles = []
    seen_titles = set()

    for article in articles['articles']:
        if article['title'] not in seen_titles:
            seen_titles.add(article['title'])
            unique_articles.append(article)

    return unique_articles

# 중복 제거된 기사 목록 가져오기
unique_articles_en = remove_duplicates(all_articles_en)

# 결과 출력 (예시로 몇 개의 기사 제목만 출력)
for article in unique_articles_en[:5]:
    print(article['title'])

