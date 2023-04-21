import unittest
from emoji_skin_tone import Fitzpatrick, strip_skin_tone_modifiers, extract_human_emoji, apply_skin_tone

# Defines a test case class that inherits from unittest.TestCase
class TestEmojiSkinTone(unittest.TestCase):

    # Tests the strip_skin_tone_modifiers function
    def test_strip_skin_tone_modifiers(self):
        input_string = "Hello World! 👩🏻‍💼👨🏼‍💻"
        expected_output = "Hello World! 👩‍💼👨‍💻"
        self.assertEqual(strip_skin_tone_modifiers(input_string), expected_output)

    # Tests the extract_human_emoji function
    def test_extract_human_emoji(self):
        input_string = "Hello World! 👩🏻‍💼👨🏼‍💻"
        expected_output = ["👩🏻‍💼", "👨🏼‍💻"]
        self.assertEqual(extract_human_emoji(input_string), expected_output)

    # Tests the apply_skin_tone function
    def test_apply_skin_tone(self):
        input_string = "Hello World! 👩‍💼👨‍💻"
        expected_output = "Hello World! 👩🏽‍💼👨🏽‍💻"
        self.assertEqual(apply_skin_tone(input_string, Fitzpatrick.type_3), expected_output)


if __name__ == "__main__":
    unittest.main()
