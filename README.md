# Textfx

[![PyPI Downloads](https://static.pepy.tech/badge/textfx)](https://pepy.tech/project/textfx)
![Python](https://img.shields.io/badge/python-3.9-blue)
[![License](https://img.shields.io/github/license/iliakarimi/textfx)](https://github.com/iliakarimi/textfx/blob/main/LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/iliakarimi/textfx)](https://github.com/iliakarimi/textfx)

Textfx is a Python library for creating dynamic and visually engaging text effects.
It offers multiple functions to display text with unique animations and styles — perfect for enhancing console-based projects.

## Features

* **Typing Effect**: Simulates the effect of typing text character by character.
* **Scramble Effect**: Displays random characters that gradually transform into the actual text.
* **Wave Text**: Makes the text move in a wave-like pattern.
* **Untyping Effect**: Gradually erases text character by character.
* **Unscramble Effect**: The text gradually scrambles into random characters until it disappears.
* **Unwave Text**: The text starts in a wave-like pattern and gradually stabilizes.
* **Loading**: Display a loading animation using a customizable animation. **New!**
* ✅ **Color Support**: All effects now support colored text using `termcolor`.

## Installation

You can install it with:

```bash
pip install textfx
```

Or clone this repository and use the `textfx.py` file directly in your project:

```bash
git clone https://github.com/iliakarimi/textfx.git
cd textfx
pip install -r requirements.txt
```

Then, import the required functions in your Python script:

```python
from textfx import typeeffect, scrameffect, wavetext, untypeeffect, unscrameffect, unwavetext, Loading
```

## Usage

### Typing Effect

```python
from textfx import typeeffect
typeeffect("Hello, world!", color="cyan", delay=0.1)
```

### Scramble Effect

```python
from textfx import scrameffect
scrameffect("Scrambled Text", color="green", delay=0.1)
```

### Wave Text

```python
from textfx import wavetext
wavetext("Wave Text", color="yellow", delay=0.1)
```

### Untyping Effect

```python
from textfx import untypeeffect
untypeeffect("Erasing Text", color="gray", delay=0.1)
```

### Unscramble Effect

```python
from textfx import unscrameffect
unscrameffect("Glitching Away", color="blue", delay=0.1)
```

### Unwave Text

```python
from textfx import unwavetext
unwavetext("Steadying Waves", color="red", delay=0.1)
```

### Loading

```python
from textfx import Loading

with Loading("Processing..."):
    # do something
    time.sleep(5)
```

You can customize the spinner animation:

```python
Loading(animation=".oO@* ")
```

Or change the text and delay:

```python
Loading(message="Waiting", animation="|/-\\", delay=0.2, end_message="Finished!")
```

## 🎨 Color Options

All effects support **colored text** using the `color` parameter.

You can choose from the following colors:

```
grey, red, green, yellow, blue, magenta, cyan, white
```

Example:

```python
typeeffect("This is red text!", color="red", delay=0.1)
```

> 💡 *Color support may depend on your terminal. Most modern terminals support `termcolor` outputs.*

For more details, see [termcolor documentation](https://pypi.org/project/termcolor/).

## Dependencies

* Python **3.9** or above
* [`termcolor`](https://pypi.org/project/termcolor/)

You can install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Contributing

Feel free to fork this repository and submit pull requests.
Suggestions for new effects and improvements are always welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

🎉 **Enjoy using Textfx!**

