# Textfx

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/textfx?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=Monthly+downloads)](https://pepy.tech/projects/textfx)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/textfx?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=BLUE&left_text=Total+downloads)](https://pepy.tech/projects/textfx)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
[![License](https://img.shields.io/github/license/iliakarimi/textfx)](https://github.com/iliakarimi/textfx/blob/main/LICENSE)
[![Repo Size](https://img.shields.io/github/repo-size/iliakarimi/textfx)](https://github.com/iliakarimi/textfx)

Textfx is a lightweight Python library for creating dynamic, visually engaging console text effects and Loading Animation.

## 📦 Installation

```bash
pip install textfx
```

Or clone & install dependencies:

```bash
git clone https://github.com/iliakarimi/textfx.git
cd textfx
pip install -r requirements.txt
```

## 🎨 Features

1. **Typing Effect** (`typeeffect`)
2. **Scramble Effect** (`scrameffect`)
3. **Wave Text** (`wavetext`)
4. **Untyping Effect** (`untypeeffect`)
5. **Unscramble Effect** (`unscrameffect`)
6. **Unwave Text** (`unwavetext`)
7. **Loading Animations** (more new loading in v2.2)
8. **Color Support** via `termcolor`

## 🚀 Usage

Import the desired effects and loaders:

```python
from textfx import (
    typeeffect, scrameffect, wavetext,
    untypeeffect, unscrameffect, unwavetext,
    SpinnerLoading, ProgressBarLoading, GlitchLoading
)
```

For detailed examples, see [`docs/examples.md`](docs/examples.md).

### Loading Animations

All loader classes share these parameters:

* `message` (str): Prefix text displayed before the animation.
* `end_message` (str): Text displayed after the loader stops.
* `delay` (float): Seconds between animation frames.

#### 1. SpinnerLoading

Classic spinner cursor:

```python
with SpinnerLoading(
    message="Processing...",
    animation="⠋⠙⠸⠴⠦⠇",
    delay=0.1
):
    do_work()
```

#### 2. ProgressBarLoading

Animated bar moving back and forth:

```python
with ProgressBarLoading(
    barline='-', animation='█', length=30,
    message="Loading", delay=0.05
):
    do_work()
```

#### 3. GlitchLoading

Random-character glitch effect:

```python
with GlitchLoading(
    text="Decrypting...",
    delay=0.1
):
    do_work()
```

## 🎨 Color Options

All effects support an optional `color` parameter (via `termcolor`):

```
grey, red, green, yellow, blue, magenta, cyan, white
```

> *Ensure your terminal supports ANSI colors for `termcolor` outputs.*

## 📋 Dependencies

* Python **3.9+**
* [`termcolor`](https://pypi.org/project/termcolor/)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🏗️ Contributing

Pull requests are welcome! For more examples and details, refer to `docs/examples.md`.

## 📄 License

MIT License — see [LICENSE](LICENSE).

---

Enjoy using Textfx!
