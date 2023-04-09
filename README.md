# pyquotegen :speech_balloon:

[![PyPI version](https://badge.fury.io/py/pyquotegen.svg)](https://badge.fury.io/py/pyquotegen)
[![Downloads](https://pepy.tech/badge/pyquotegen)](https://pepy.tech/project/pyquotegen)
[![GitHub license](https://img.shields.io/github/license/Armanidrisi/pyquotegen)](https://github.com/Armanidrisi/pyquotegen/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Armanidrisi/pyquotegen)](https://github.com/Armanidrisi/pyquotegen/issues)


`pyquotegen` is a Python package that provides a simple way to generate random quotes. :thought_balloon:

## Installation :rocket:

To install `pyquotegen`, simply run: :arrow_down:

```bash
pip install pyquotegen
```

## Usage :computer:
To use `pyquotegen`, import the package and call the `get_quote` function: :sparkles:

```python
import pyquotegen

# get a random quote
quote = pyquotegen.get_quote()
print(quote)

# get a quote by specific category
quote_by_category = pyquotegen.get_quote("inspirational")
print(quote_by_category)
```

Note: The default category is "motivation" if you don't provide any category. :memo:

## List Of Some Basic Categories
- :rocket: motivational
- :two_men_holding_hands: friendship
- :computer: technology
- :bulb: inspirational
- :joy: funny
- :leaves: nature
- :chart_with_upwards_trend: success
- :muscle: attitude
- :keyboard: coding

## Features :rocket:
- Generates random quotes :sparkles:
- Provides quotes by specific category :bookmark_tabs:
- Supports multiple categories :notebook_with_decorative_cover:
- Lightweight and easy to use :muscle:

## Contributing :raised_hands:
Contributions are welcome! To contribute, please fork the repository and submit a pull request. :pray:

## Credits :star:
This package was created by Arman Idrisi. :heart:

## License :page_with_curl:
This project is licensed under the MIT License. See the LICENSE file for details. :scroll:
