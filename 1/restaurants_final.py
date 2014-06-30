__author__ = 'Administrator'

"""
A restaurant recommendation system.

Here are some example dictionaries. These correspond to the
information in restaurants_small.txt

Restaurant name to rating:
# dict of {str:int}
{'Georie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str:list of str}
{'$': ['Queen St. Cafe', 'Dumplings', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georie Porgie'],
 '$$$$': []}

Cuisine tolist restaurant names:
# dict of {str:list of str}
{'Canadian': ['Georie Porgie'],
 'Pub Food': ['Georie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With these data, for a price of '$' and cuisines of ['Chinese', 'Thai'],
we would produce this list:

[[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""

# The file containing the restaurant data.
FILENAME = 'restaurants_small.txt'

def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines list. Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.

    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cuisine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)

    # Look for price or cuisines first?(here you make a decision!!!)
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range
    # and serve the requested cuisine. Need to look at ratings and sort
    # this list.
    result = build_rating_list(name_to_rating, names_final)


    # We're done! Return that sorted list.
    return result


def build_rating_list(name_to_rating, names_final):
    """(dict of {str:int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}

     >>> names = ['Queen St. Cafe', 'Dumplings R Us']
     [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """

def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """(list of str, dict of {str:list of str}, list of str) -> list of str

    >>> names= ['Queen St. Cafe', 'Dumplings', 'Deep Fried Everything']
    >>> cuis = {'Canadian': ['Georie Porgie'],
     'Pub Food': ['Georie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names, cuis, cuisines)
    ['Queen St. Cafe', 'Dumplings R Us']
    """

def read_restaurant(file):
    """(file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information
    in the file:
    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}





