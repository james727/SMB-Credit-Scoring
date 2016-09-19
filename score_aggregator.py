import company_yelp_score, sector_score, size_score, owner_score, url_score, time

COMPANY_WEIGHT = 1
INDUSTRY_WEIGHT = 1
SIZE_WEIGHT = 1
OWNER_WEIGHT = 1
URL_WEIGHT = 1

def aggregate_scores(company):
    # Takes a company object and tabulates all relevant scores. Then calls combine_scores
    # to aggregate and return.
    print "\nCalculating company p_score...\n"
    time.sleep(.5)
    company_score = company_yelp_score.get_company_score(company)
    company_industry_score = sector_score.get_industry_score(company)
    company_size_score = size_score.get_size_score(company)
    company_owner_score = owner_score.get_owner_score(company)
    company_url_score = url_score.get_url_score(company)
    return combine_scores(company_score, company_industry_score, company_size_score, company_owner_score, company_url_score)

def combine_scores(company_score, industry_score, size_score, owner_score, link_score):
    # Produces a weighted average score based on the weightings assigned up top.
    company_factor = COMPANY_WEIGHT * company_score
    industry_factor = INDUSTRY_WEIGHT * industry_score
    size_factor = SIZE_WEIGHT * size_score
    owner_factor = OWNER_WEIGHT * owner_score
    url_factor = URL_WEIGHT * link_score

    total_weight = COMPANY_WEIGHT + INDUSTRY_WEIGHT + SIZE_WEIGHT + OWNER_WEIGHT + URL_WEIGHT
    weighted_score = (company_factor + industry_factor + size_factor + owner_factor + url_factor + 0.0) / total_weight
    return weighted_score
