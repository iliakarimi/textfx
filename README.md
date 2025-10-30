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

1. **Typing Effect**
2. **Scramble Effect**
3. **Wave Text**
4. **Untyping Effect**
5. **Unscramble Effect**
6. **Unwave Text**
7. **Loading Animations**
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
with ProgressBarLoading(message="Compiling Code", barline=".", animation="⚙", length=40, message_color="cyan", animation_color="yellow", barline_color="white", delay=0.07):
    time.sleep(5)
```

For detailed examples, see [`Documention`](docs/examples.md).


## 🎨 Color Options

All effects support an optional `color` parameter (via `termcolor`):


`black`
`red`
`green`
`yellow`
`blue`
`magenta`
`cyan`
`white`

`light_grey`
`dark_grey`
`light_red`
`light_green`
`light_yellow`
`light_blue`
`light_magenta`
`light_cyan`


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
