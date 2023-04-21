from enum import Enum
import regex

# Define the Fitzpatrick scale using an Enum
class Fitzpatrick(Enum):

    type_1_2 = '\U0001F3FB'
    type_3 = '\U0001F3FC'
    type_4 = '\U0001F3FD'
    type_5 = '\U0001F3FE'
    type_6 = '\U0001F3FF'



# Function to remove skin tone modifiers from a given string
def strip_skin_tone_modifiers(s: str) -> str:
    '''
    Remove skin tone modifiers from the input string.

    :param s: The input string containing emojis with or without skin tone modifiers
    :return: A copy of the input string with skin tone modifiers removed
    '''
    
    #Using regex substitution to remove skin tone modifiers from the input
    return regex.sub(f"[{regex.escape(''.join([val.value for _,val in Fitzpatrick.__members__.items()]))}]", "", s)



#Function to extract human emoji from a given string
def extract_human_emoji(s: str) -> list[str]:
    '''
    Extract all human emojis from the input string.

    :param s: The input string containing emojis
    :return: A list of substrings containing human emojis with any present skin tone modifiers
    '''
    
    #Using a regex pattern to find all human emoji in the input string and return them in a list
    return regex.findall(r"[\u200D\uFE0F]?\p{Emoji_Presentation}\uFE0F?", s)



#Function to apply skin tone modifiers to human emojis in a given string
def apply_skin_tone(s: str, skin_tone : Fitzpatrick) -> str:
    '''
    Apply the specified skin tone modifier to all human emojis in the input string.

    :param s: The input string containing emojis with or without skin tone modifiers
    :param skin_tone: A value from the Fitzpatrick Enum representing the desired skin tone modifier
    :return: A copy of the input string with the specified skin tone modifier applied to all human emojis (string)
    '''
    
    #Removes existing skin tone modifiers from the input string
    stripped_string = strip_skin_tone_modifiers(s)

    #Defines a custom replacement function that adds the skin tone modifier
    def replace_emoji(match):
        #Gets the matched emoji and converts it to the skin tone modifier
        return match.group(0) + skin_tone.value
    
    # Uses a regex pattern to find all human emojis without skin tone modifiers and replaces them using our replacement function
    # This pattern is more efficient and general, as it captures all human emojis.
    return regex.sub(r"(\p{Emoji_Presentation})(?!\uFE0F)", replace_emoji, stripped_string)

    
