import argparse
from emoji_skin_tone import Fitzpatrick, strip_skin_tone_modifiers, extract_human_emoji, apply_skin_tone

# Function that creates and configures the argument parser
def create_parser():
    parser = argparse.ArgumentParser(description="Manipulate emoji skin tones in strings")  # Create a new argumentparser instance with a description
    subparsers = parser.add_subparsers(dest="command")  # Add subparsers for different commands (strip, extract, apply)

    # Strip subparser
    strip_parser = subparsers.add_parser("strip", help="Remove skin-tone modifiers from a string")
    strip_parser.add_argument("input", type=str, help="The input string")

    # Extract subparser
    extract_parser = subparsers.add_parser("extract", help="Extract human emoji from a string")
    extract_parser.add_argument("input", type=str, help="The input string")

    # Apply subparser
    apply_parser = subparsers.add_parser("apply", help="Apply skin-tone modifiers to human emoji in a string")
    apply_parser.add_argument("input", type=str, help="The input string")
    apply_parser.add_argument("skin_tone", type=int, choices=range(1, 7), help="The Fitzpatrick skin-tone scale value (1-6)")

    return parser  # Returns configured parser

# Main function which handles the command line interface
def main():
    parser = create_parser()  # Creates the arg parser
    args = parser.parse_args()  # Parses the command line args

    # Executes the chosen function
    
    if args.command == "strip":
        print(strip_skin_tone_modifiers(args.input))
    elif args.command == "extract":
        print(extract_human_emoji(args.input))
    elif args.command == "apply":
        skin_tone = Fitzpatrick[f"TYPE_{args.skin_tone}"]
        print(apply_skin_tone(args.input, skin_tone))

if __name__ == "__main__":
    main()
