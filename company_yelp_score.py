# This file contains the methods necessary to grab company info from the Yelp api,
# and a method to derive a company yelp score from this information. The company
# yelp score is a weighted combination of the number of reviews and the average rating.

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

def create_client():
    # Creates Yelp api client using a set of temporary keys I obtained for
    # this exercise
    auth = Oauth1Authenticator(
        consumer_key="QbwJZmMMjlyIzRZZFQzGPw",
        consumer_secret="n34uOEDkj-58esi4lscxWjxrLOQ",
        token="YXFlXv9023NiHhoYL5BbBf-ZTPz5FbWq",
        token_secret="jnAS4LPnLqZPk27yk7wTnTpGoXQ"
        )

    client = Client(auth)
    return client

def search_for_business(business_name, city, api_client):
    # Searches for a business based on name and city, and returns top 10 results
    params = {'term': business_name,
              'limit': 10}
    response = api_client.search(city, **params)
    results = response.businesses
    return results

def get_company_score(company):
    # Takes in a company object and returns a score based on its Yelp ratings
    # under the assumption that more, better reviews means a more trustworthy
    # business.
    if company.yelp_object is None:
        return 0
    num_reviews = int(company.review_count)
    rating = float(company.rating)
    max_score = 500 * 5 # cap reviews at 500
    capped_num_reviews = min(num_reviews, 500)
    weighted_reviews = capped_num_reviews * rating
    return weighted_reviews / max_score
