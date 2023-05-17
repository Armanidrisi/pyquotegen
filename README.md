[![Total Downloads](https://pepy.tech/badge/pyquotegen)](https://pepy.tech/project/pyquotegen)
[![PyPI Version](https://img.shields.io/pypi/v/pyquotegen?color=blue&label=PyPI%20version&logo=python)](https://pypi.org/project/pyquotegen/)
[![GitHub stars](https://img.shields.io/github/stars/Armanidrisi/pyquotegen?style=flat-square&logo=github)](https://github.com/Armanidrisi/pyquotegen/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Armanidrisi/pyquotegen?style=flat-square&logo=github)](https://github.com/Armanidrisi/pyquotegen/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Armanidrisi/pyquotegen?style=flat-square&logo=github)](https://github.com/Armanidrisi/pyquotegen/issues)
[![GitHub license](https://img.shields.io/github/license/Armanidrisi/pyquotegen?style=flat-square&logo=github)](https://github.com/Armanidrisi/pyquotegen/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/Armanidrisi/pyquotegen?style=flat-square&logo=github)](https://github.com/Armanidrisi/pyquotegen/graphs/contributors)
[![pyquotegen](https://img.shields.io/badge/pyquotegen-awesome-blueviolet?style=flat-square&logo=github)](https://github.com/Armanidrisi/pyquotegen)

# pyquotegen - Simple Quote Generator Python Package ✨

`pyquotegen` is a Python package that allows you to generate random quotes or quotes from specific categories. It provides a simple and straightforward way to incorporate quotes into your Python applications. 📚

## Installation ⚙️

You can install `pyquotegen` using pip:

```shell
pip install pyquotegen
```

## Usage 🚀

Here's an example of how to use `pyquotegen`:

```python
import pyquotegen

# Get a random quote
quote = pyquotegen.get_quote()
print(quote)

# Get a quote by specific category
quote_by_category = pyquotegen.get_quote("inspirational")
print(quote_by_category)
```

The `pyquotegen` package provides the `get_quote()` function, which returns a random quote. You can optionally specify a category to get a quote from that specific category. If no category is provided, a quote from any category will be returned. 🔍

## Functions 📝

### `get_quote(category: Optional[str] = None) -> str`

This function returns a random quote. If a category is specified, it returns a random quote from that category. If no category is provided, a quote from any category will be returned. 🎉

#### Parameters 📋

- `category` (optional): A string specifying the category of the quote. Available categories include "inspirational", "funny","motivational". If no category is provided, the function will return a quote from any category. 🗂️

#### Returns 📤

A string containing the quote. 💬

## Categories 🗂️

`pyquotegen` provides quotes in the following categories:

- :rocket: motivational
- :two_men_holding_hands: friendship
- :computer: technology
- :bulb: inspirational
- :joy: funny
- :leaves: nature
- :chart_with_upwards_trend: success
- :muscle: attitude
- :keyboard: coding

You can pass any of these categories as an argument to the `get_quote()` function to get a quote from that specific category. If you don't specify a category, a random quote from any category will be returned. 🎯

## Features :rocket:

- Generates random quotes :sparkles:
- Provides quotes by specific category :bookmark_tabs:
- Supports multiple categories :notebook_with_decorative_cover:
- Lightweight and easy to use :muscle:

## Contributing 🤝

We welcome contributions to `pyquotegen`! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/Armanidrisi/pyquotegen). 🙌

To contribute to `pyquotegen`, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make the necessary changes and ensure that the tests pass.
4. Submit a pull request to the `main` branch of the original repository. 🛠️

We appreciate your contributions, whether it's bug fixes, feature enhancements, or documentation improvements. 👏

## License 📜

This package is distributed under the MIT License. See the [LICENSE](https://github.com/Armanidrisi/pyquotegen/blob/main/LICENSE) file for more information. 📄

## Acknowledgements 🙏

The quotes used in `pyquotegen` are sourced from various public domain collections and online resources. We acknowledge and appreciate the authors and contributors of these quotes. 🌟

If you have any questions or need further assistance, please don't hesitate to reach out. 💡
