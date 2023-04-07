# Text Numbers

Text Numbers is a Python package that allows you to convert words representing numerical values (e.g., "three hundred forty-two") into actual numbers (e.g., 342). The package supports numbers up to 1 billion and can handle variations in word representation, including the use of "and" and hyphens. It also supports decimal numbers.

## Installation

You can install the Text Numbers package from the Python Package Index (PyPI) using the following command:

```bash
pip install text-numbers
```

# Usage

To use the Text Numbers package, you can import the word_to_number function and pass in a string representing a number in words. The function will return the corresponding numerical value.

Here's an example:

```python
from text_numbers import word_to_number

# Convert words to numbers
number = word_to_number("three hundred forty-two")
print(number)  # Output: 342

# Convert words with "and" to numbers
number = word_to_number("two hundred and sixty-five")
print(number)  # Output: 265

# Convert decimal numbers in words to numerical values
number = word_to_number("zero point zero nine")
print(number)  # Output: 0.09
```

# Contributing

Contributions to the Text Numbers package are welcome! If you encounter any issues or have feature requests, please open an issue on the GitHub repository. If you would like to contribute code, please submit a pull request.

# License

Text Numbers is released under the MIT License. See the LICENSE file for more information.
