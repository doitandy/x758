from newsapi import NewsApiClient
import pandas as pd

# News API 클라이언트 초기화
api_key = '2d354d9f08384b26aafb95137606623c'
newsapi = NewsApiClient(api_key=api_key)

# 주식 관련 최신 뉴스 가져오기
all_articles = newsapi.get_everything(q='stock market',
                                      language='en',
                                      sort_by='publishedAt',
                                      page_size=10)

# 데이터프레임으로 변환
articles_df = pd.DataFrame(all_articles['articles'])

# 중복 주제 제거 (예: 같은 제목의 기사)
articles_df = articles_df.drop_duplicates(subset=['title'])

# 보기 쉽게 출력
for index, row in articles_df.iterrows():
    print(f" {row['title']}\n {row['url']}\n")

# 필요에 따라 'description', 'publishedAt' 등의 다른 필드도 출력할 수 있습니다.

