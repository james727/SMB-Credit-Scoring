# This file contains all methods that involve prompting the user for data
# regarding the company to be evaluated. Additionally, it includes a few
# functions that validate the user's input, re-prompting as necessary.

import company_info, company_yelp_score, sector_score, size_score, requests

def prompt_user():
    # This method executes the overall program flow; asking the user for data
    # about the company step by step.
    print_welcome_statement()

    name, city = prompt_company_name()
    yelp_object = validate_company_name(name, city)
    company = company_info.Company(name, city, yelp_object)

    industry = prompt_sector()
    company.industry = industry

    url = prompt_url()
    url = validate_url(url)
    company.url = url

    owner_name = prompt_owner_name()
    owner_name = validate_owner_name(owner_name)
    company.owner_name = owner_name

    size = prompt_size()
    company.size = size

    return company

def print_welcome_statement():
    # Startup print statements
    print "Welcome to Credit Score Inc.'s small business credit evaluation tool!\n"
    print "The program will take you through a series of prompts for information\nregarding the business you're considering loaning to. We'll gather as\nmuch information as we can and give you a P-Score estimate.\n"

def prompt_company_name():
    # Prompts user for company name and location
    print "Enter the name of the company:\n"
    name = raw_input()
    print "\nEnter the city the company is located in:\n"
    city =  raw_input()
    return name, city

def validate_company_name(name, city):
    # Searches yelp for companies matching the user's input, and asks the user
    # to select which one is correct.
    print "\nSearching for company data...\n"
    yelp_client = company_yelp_score.create_client()
    options = company_yelp_score.search_for_business(name, city, yelp_client)
    if len(options) == 0:
        print "No matching results found. Type 1 to try again, or anything else to proceed without Yelp data.\n"
        inp = raw_input()
        if inp == "1":
            new_company, new_city = prompt_company_name()
            return validate_company_name(new_company, new_city)
    print "Select which of the below options are the business in question. If none of them look right, type 0 to proceed without Yelp data:\n"
    for index, option in enumerate(options):
        print "\t" + str(index + 1) + ". " + option.name + ": " + ", ".join(option.location.display_address)
    print
    try:
        option_num = int(raw_input())
    except:
        print "Not a valid option. Proceeding without Yelp data."
        option_num = 0
    if option_num == 0: return None
    return options[option_num - 1]

def prompt_sector():
    # Prompts the user to select the company's sector from the list of sectors defined
    # in sector_score.py
    sectors = sector_score.get_sector_list()
    print "\nPlease enter the number of the sector listed below that best matches the company:\n"
    for index, sector in enumerate(sectors):
        print "\t" + str(index + 1) + ". " + sector
    print
    sector_number = raw_input()
    if sector_number not in [str(x + 1) for x in range(len(sectors))]:
        print "Invalid input, prompting again.\n"
        return prompt_sector()
    return sectors[int(sector_number)-1]

def prompt_url():
    # prompts the user for the company's URL
    print "\nEnter the url of the company's business website (must begin with http.)\n"
    return raw_input()

def validate_url(url):
    # Checks if url is reachable by sending an http request
    if not url.startswith("http"):
        print "\nInvalid URL, enter 1 to try again or anything else to skip this step (will result in a lower credit score).\n"
        inp = raw_input()
        if inp == "1":
            new_url = prompt_url()
            return validate_url(new_url)
        return None
    try:
        result = requests.get(url)
        return url
    except:
        print "\nCould not reach URL, enter 1 to try again or anything else to skip this step (will result in a lower credit score).\n"
        inp = raw_input()
        if inp == "1":
            new_url = prompt_url()
            return validate_url(new_url)
        return None

def prompt_owner_name():
    # This just prompt's the owner's name - would probably ask for SSN to run a credit check
    # if I was doing this for real.
    print "\nEnter the owner's name\n"
    return raw_input()

def validate_owner_name(owner_name):
    # Imagine that I'm using a credit report / background check service to validate that the
    # owner is actually a real person.
    return owner_name

def prompt_size():
    # Prompts company size based on the buckets specified in size_score.py
    sizes = size_score.get_revenue_sizes()
    print "\nSelect your best estimate of the company's annual revenue range from the below list:\n"
    for index, size in enumerate(sizes):
        print "\t" + str(index + 1) + ". " + size
    print
    size_num = raw_input()
    if size_num not in [str(x + 1) for x in range(len(sizes))]:
        print "\nInvalid input, prompting again.\n"
        return prompt_sector()
    return sizes[int(size_num)-1]
