# Company class. The program constructs an instance of the company class,
# fills in as much data as possible, and then calls various scoring functions
# which take a company instance as their arguments.

class Company(object):
    def __init__(self, name, city, yelp_object):
        self.name = name
        self.city = city
        self.industry = None
        self.url = None
        self.owner_name = None
        self.size = None
        self.yelp_object = yelp_object
        if yelp_object is not None:
            self.name = yelp_object.name
            self.city = yelp_object.location.city
            self.zip_code = yelp_object.location.postal_code
            self.review_count = yelp_object.review_count
            self.rating = yelp_object.rating
