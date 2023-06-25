import unittest
from emoji_skin_tone import Fitzpatrick, strip_skin_tone_modifiers, extract_human_emoji, apply_skin_tone

# Defines a test case class that inherits from unittest.TestCase
class TestEmojiSkinToneFunctions(unittest.TestCase):

    def test_strip_skin_tone_modifiers(self):
        # Test with a string containing multiple emojis with different skin tones
        self.assertEqual(strip_skin_tone_modifiers("Hello World! 👩🏽‍💻👨🏿‍💻👦🏻👧🏾"), "Hello World! 👩‍💻👨‍💻👦👧")

        # Test with a string containing an emoji without a skin tone
        self.assertEqual(strip_skin_tone_modifiers("Hello World! 👩‍💻"), "Hello World! 👩‍💻")

        # Test with a string containing no emojis
        self.assertEqual(strip_skin_tone_modifiers("Hello World!"), "Hello World!")

    def test_extract_human_emoji(self):
        # Test with a string containing multiple emojis with different skin tones
        self.assertEqual(extract_human_emoji("Hello World! 👩🏽‍💻👨🏿‍💻👦🏻👧🏾"), ['👩🏽‍💻', '👨🏿‍💻', '👦🏻', '👧🏾'])

        # Test with a string containing an emoji without a skin tone
        self.assertEqual(extract_human_emoji("Hello World! 👩‍💻"), ['👩‍💻'])

        # Test with a string containing no emojis
        self.assertEqual(extract_human_emoji("Hello World!"), [])

    def test_apply_skin_tone(self):
        # Test with a string containing multiple emojis and apply a skin tone
        self.assertEqual(apply_skin_tone("Hello World! 👩‍💻👨‍💻👦👧", Fitzpatrick.type_4), "Hello World! 👩🏽‍💻👨🏽‍💻👦🏽👧🏽")

        # Test with a string containing an emoji without a skin tone and apply a skin tone
        self.assertEqual(apply_skin_tone("Hello World! 👩‍💻", Fitzpatrick.type_4), "Hello World! 👩🏽‍💻")

        # Test with a string containing no emojis and try to apply a skin tone
        self.assertEqual(apply_skin_tone("Hello World!", Fitzpatrick.type_3), "Hello World!")



if __name__ == "__main__":
    unittest.main()
