# Emoji Skin Tone

Emoji Skin Tone is a Python library that allows you to manipulate the skin tones of human emojis in a string. It provides functionality to strip skin tone modifiers from emojis, extract human emojis from a string, and apply a specific skin tone to human emojis.

## Features

- **Strip Skin Tone Modifiers**: Remove all skin tone modifiers from human emojis in a string.
- **Extract Human Emojis**: Extract all human emojis from a string, including any present skin tone modifiers.
- **Apply Skin Tone**: Apply a specific skin tone to all human emojis in a string.


## Installation

You can install this library locally by downloading this repository and using pip:

```bash
pip install emoji-skin-tone
```

## The Fitzpatrick Scale

The Fitzpatrick scale is a six-point classification system for human skin color. It's used in this library to represent a range of skin tones for human emojis.


In this library, we use the Fitzpatrick scale to apply skin tone modifiers to human emojis. The `Fitzpatrick` enum in the `emoji_skin_tone` module represents the six types of the Fitzpatrick scale:

- `Fitzpatrick.TYPE_1`: Light skin, often burns and rarely tans (e.g., 👩🏻‍💻)
- `Fitzpatrick.TYPE_2`: Fair skin, burns easily and tans minimally (e.g., 👩🏼‍💻)
- `Fitzpatrick.TYPE_3`: Medium skin, may burn but tans uniformly (e.g., 👩🏽‍💻)
- `Fitzpatrick.TYPE_4`: Olive skin, rarely burns and tans well (e.g., 👩🏾‍💻)
- `Fitzpatrick.TYPE_5`: Moderately pigmented brown skin, very rarely burns and tans very easily (e.g., 👩🏿‍💻)
- `Fitzpatrick.TYPE_6`: Heavily pigmented black skin, never burns and tans very easily (e.g., 👩🏿‍💻)

You can use these types with the `apply_skin_tone` function to apply skin tone modifiers to human emojis in a string.

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
