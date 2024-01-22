import requests
from datetime import datetime, timedelta

def get_business_id(api_key, business_name, location):
    """Yelp API를 사용하여 비즈니스 ID를 가져오는 함수"""
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'term': business_name, 'location': location, 'limit': 1}
    response = requests.get('https://api.yelp.com/v3/businesses/search', headers=headers, params=params)

    # 응답 내용을 검사하여 비즈니스 ID를 찾습니다
    businesses = response.json().get('businesses')
    if not businesses:
        print(f"No businesses found for {business_name} in {location}")
        return None

    return businesses[0]['id']

def get_recent_reviews(api_key, business_id, days=7):
    """Yelp API를 사용하여 지정된 일수 동안의 최근 리뷰를 가져오는 함수"""
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(f'https://api.yelp.com/v3/businesses/{business_id}/reviews', headers=headers)
    reviews = response.json()['reviews']
    
    recent_reviews = []
    cut_off_date = datetime.now() - timedelta(days=days)
    for review in reviews:
        review_date = datetime.strptime(review['time_created'], '%Y-%m-%d %H:%M:%S')
        if review_date >= cut_off_date:
            recent_reviews.append(review)
    
    return recent_reviews

# Yelp API 키
api_key = 'nrpzbB1n0qhUotioapBr8VFGjN1p_IqrTUbgPcMev-yrG1S0GfaLnUDQL5ByjETUC6Es0Z3XZySpma1TBgN0Cvo8YRWXrL3ffP114LLFR941B82yfwh0ZM5ppjdyZXYx'

# 비즈니스 목록
businesses = [
    ('oo-kook Korean BBQ', 'Los Angeles'),
    ('oo-kook Korean BBQ', 'San Gabriel'),
    ('Shabuya', 'Los Angeles'),
    ('Shabuya', '820 E Valley Blvd Alhambra'),
    ('Shabuya', 'La Mirada')
]

# 각 비즈니스의 최근 리뷰를 가져옵니다
for name, location in businesses:
    business_id = get_business_id(api_key, name, location)
    reviews = get_recent_reviews(api_key, business_id)
    print(f"Reviews for {name} in {location}:")
    for review in reviews:
        print(f"- {review['text']}\n")

