from all_quotes import allquotes
import random

# a class for throw error
class CategoryNotFoundError(Exception):
    pass

"""Function For Get All Qoutes"""
def get_quotes(category="motivational"):
  
  # check if category Exists or not
  
  if category.lower() not in allquotes:
    
    # raise new error
    
        raise CategoryNotFoundError('No such category %s' % (category))
        
  # return all quotes
  
  return allquotes[category.lower()]

#Function For Get Single Quote

def get_quote(category="motivational"):
  
  #get all quotes from `get_quotes` Function
  
  quotes = get_quotes(category.lower())

  #return random single quote 
  
  return random.choice(quotes)