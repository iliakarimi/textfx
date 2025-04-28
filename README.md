# Textfx

[![PyPI Downloads](https://static.pepy.tech/badge/textfx)](https://pepy.tech/project/textfx)


Textfx is a Python library for creating dynamic and visually engaging text effects. It offers multiple functions to display text with unique animations and styles, perfect for enhancing console-based projects.

## Features

- **Typing Effect**: Simulates the effect of typing text character by character.
- **Falling Text**: Coming Soon...
- **Scramble Effect**: Displays random characters that gradually transform into the actual text.
- **Wave Text**: Makes the text move in a wave-like pattern.
- **Untyping Effect**: Gradually erases text character by character.
- **Unfalling Text**: Coming Soon...
- **Unscramble Effect**: The text gradually scrambles into random characters until it disappears.
- **Unwave Text**: The text starts in a wave-like pattern and gradually stabilizes.

## Installation
You can install it With:

```bash
pip install textfx
```

or You can clone this repository and use the `textfx.py` file directly in your project:

```bash
git clone https://github.com/iliakarimi/textfx.git
```

Then, import the required functions in your Python script:

```python
from textfx import typeeffect, falltext, scrameffect, wavetext, untypeeffect, unfalltext, unscrameffect, unwavetext
```

## Usage

Below are examples of how to use each function:

### Typing Effect
```python
from textfx import typeeffect
typeeffect("Hello, world!", delay=0.1)
```


### Scramble Effect
```python
from textfx import scrameffect
scrameffect("Scrambled Text", delay=0.1)
```

### Wave Text
```python
from textfx import wavetext
wavetext("Wave Text", delay=0.1)
```

### Untyping Effect
```python
from textfx import untypeeffect
untypeeffect("Erasing Text", delay=0.1)
```


### Unscramble Effect
```python
from textfx import unscrameffect
unscrameffect("Glitching Away", delay=0.1)
```

### Unwave Text
```python
from textfx import unwavetext
unwavetext("Steadying Waves", delay=0.1)
```

## Dependencies

- Python 3.8

## Contributing

Feel free to fork this repository and submit pull requests. Suggestions for new effects and improvements are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy using Textfx! Let your text come to life!
