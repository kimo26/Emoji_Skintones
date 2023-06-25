# Emoji Skin Tone

A Python library for manipulating emoji skin tones.

## Features

- Stripping skin-tone modifiers from a string
- Extracting human emoji with or without skin-tone modifiers from a string
- Applying skin-tone modifiers to human emoji in a string

## Installation

Download this folder then you can simply pip install it locally:

```bash
pip install emoji-skin-tone
```

## Usage

This library provides a set of functions for manipulating emoji skin tones in a string. Here's how you can use them:

```python
from emoji_skin_tone import Fitzpatrick, strip_skin_tone_modifiers, extract_human_emoji, apply_skin_tone

# To strip skin-tone modifiers from a string:
stripped_string = strip_skin_tone_modifiers("Hello World! 👩🏽‍💻👨🏿‍💻")
# The output will be: "Hello World! 👩‍💻👨‍💻"

# To extract human emojis from a string:
emoji_list = extract_human_emoji("Hello World! 👩🏽‍💻👨🏿‍💻")
# The output will be: ['👩🏽‍💻', '👨🏿‍💻']

# To apply skin-tone modifiers to human emojis in a string:
colored_string = apply_skin_tone("Hello World! 👩‍💻👨‍💻", Fitzpatrick.TYPE_3)
# The output will be: "Hello World! 👩🏽‍💻👨🏽‍💻"
```


## CLI Usage

The library also provides a command-line interface for these functions:

- To strip skin-tone modifiers from a string:
    ```bash
    python cli.py strip "Hello World! 👩🏽‍💻👨🏿‍💻"
    ```
- To extract human emoji from a string:
    ```bash
    python cli.py extract "Hello World! 👩🏽‍💻👨🏿‍💻"
    ```
- To apply skin-tone modifiers to human emoji in a string:
    ```bash
    python cli.py apply "Hello World! 👩‍💻👨‍💻" 3
    ```
