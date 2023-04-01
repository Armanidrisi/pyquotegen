# pyquotegen
A Random Quote Generator Python Package

### This Is A Python Package Which Can Be Used For Generate Random Quotes In Python

### installation 
```bash
pip install pyquotegen
```


### Example Code Snippet To Get Quote

```python 
import pyquotegen

quote = pyquotegen.get_quote()#get_quote is a function for get a random quote 
print(quote)

# get a quote by specific category
quotebycategory=pyquotegen.get_quote("inspirational") #it will give the quote in INSPIRATIONAL category Note: Default Category Is Motivation if you don't provide any category 
print(quotebycategory)
```

### List Of Some Basic Categories 

- motivational
- friendship
- technology
- inspirational
- funny
- nature
- success
- attitude
- coding

Check Out On PyPi: [click here](https://pypi.org/project/pyquotegen/)

Try It Once
