# Calculates company risk due to its industry. SECTOR_VOLATILITY data sourced
# from seekingalpha.com, numbers correspond to average one day % change on earnings
# within each sector which should serve as a decent approximation for sector volatility
# as a whole.

SECTOR_VOLATILITY = {"Utilities": 2.2,
                    "Financials": 3.2,
                    "Energy": 4.2,
                    "Materials": 4.8,
                    "Telecom": 5.0,
                    "Consumer Staples": 5.2,
                    "Industrials": 5.4,
                    "Health Care": 6.0,
                    "Consumer Discretionary": 6.1,
                    "Technology": 7.3}

def get_sector_list():
    # Returns the list of sectors for prompting the end-user
    return SECTOR_VOLATILITY.keys()

def get_industry_score(company):
    # Returns a value between 0 and 1, 1 corresponding to the least volatile
    company_industry_score = SECTOR_VOLATILITY[company.industry]
    max_industry_score = max(SECTOR_VOLATILITY.values())
    min_industry_score = min(SECTOR_VOLATILITY.values())
    company_delta = max_industry_score - company_industry_score
    normalized_company_score = company_delta / (max_industry_score - min_industry_score)
    return normalized_company_score
