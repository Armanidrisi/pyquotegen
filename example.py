import pyquotegen

# get a random quote
quote = pyquotegen.get_quote()
print(quote)

# get a quote by specific category
quote_by_category = pyquotegen.get_quote("inspirational")
print(quote_by_category)
