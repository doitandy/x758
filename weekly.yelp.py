import requests
from datetime import datetime, timedelta

def get_reviews(api_key, businesses_info):
    headers = {'Authorization': f'Bearer {api_key}'}
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    results = {}

    for business_name, location in businesses_info.items():
        search_params = {'term': business_name, 'location': location}
        
        response = requests.get(search_api_url, headers=headers, params=search_params)
        
        businesses = response.json().get('businesses', [])
        if not businesses:
            results[business_name] = "No businesses found"
            continue
        
        business_id = businesses[0]['id']
        reviews_api_url = f'https://api.yelp.com/v3/businesses/{business_id}/reviews'
        reviews_response = requests.get(reviews_api_url, headers=headers)
        all_reviews = reviews_response.json().get('reviews', [])
        
        one_week_ago = datetime.now() - timedelta(days=7)
        recent_reviews = [review for review in all_reviews if datetime.strptime(review['time_created'], '%Y-%m-%d %H:%M:%S') > one_week_ago]

        results[business_name] = recent_reviews

    return results

# Your Yelp API Key
api_key = 'nrpzbB1n0qhUotioapBr8VFGjN1p_IqrTUbgPcMev-yrG1S0GfaLnUDQL5ByjETUC6Es0Z3XZySpma1TBgN0Cvo8YRWXrL3ffP114LLFR941B82yfwh0ZM5ppjdyZXYx'

# Business names and their locations
businesses_info = {
    'OoKook Korean BBQ': 'Los Angeles, CA',
    'OO-KOOK Korean BBQ - San Gabriel': 'San Gabriel, CA',
    'Shabuya': 'Los Angeles, CA',
    'Shabuya Alhambra': 'Alhambra, CA',
    'Shabuya La Mirada': 'La Mirada, CA'
}

# Get reviews for each business
reviews_dict = get_reviews(api_key, businesses_info)

# Display reviews for each business
for business_name, reviews in reviews_dict.items():
    print(f"\nReviews for {business_name} ({businesses_info[business_name]}):\n")
    if isinstance(reviews, list):
        for review in reviews:
            if isinstance(review, dict):
                print(f"Rating: {review.get('rating')}\nUser: {review.get('user', {}).get('name')}\nText: {review.get('text')}\n")
            else:
                print("Review format is not valid")
    else:
        print(reviews)  # No businesses found or error message

