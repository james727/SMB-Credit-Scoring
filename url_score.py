# This file is a placeholder. It contains placeholder methods for evaluating
# a company's url's trustworthiness. Right now it just returns 1 if the company
# has a valid url. Ideally I'd use a paid service like seomoz or something to
# get a URL's trust score.

def get_url_score(company):
    # Returns 1 for valid url, else 0.
    if company.url is not None:
        return 1
    return 0
