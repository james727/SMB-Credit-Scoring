# This file contains methods to evaluate the impact of a company's size on its
# creditworthiness. The assumption is that bigger companies will be less likely
# to default.

ANNUAL_REVENUE_SIZES = ["Less than $1 million",
                        "Between $1 and $5 million",
                        "Between $5 and $25 million",
                        "Between $25 and $100 million",
                        "Between $100 and $500 million",
                        "More than $500 million"]

def get_revenue_sizes():
    # Returns list of sizes for prompting end-user.
    return ANNUAL_REVENUE_SIZES

def get_size_score(company):
    # Returns a company's size score, a number between 0 and 1 based on
    # which of the ANNUAL_REVENUE_SIZES the company fits into.
    size_index = ANNUAL_REVENUE_SIZES.index(company.size)
    return (size_index + 0.0) / (len(ANNUAL_REVENUE_SIZES) - 1)
