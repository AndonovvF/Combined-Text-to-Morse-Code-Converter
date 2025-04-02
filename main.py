# Combined Morse Code Converter

# Encoding dictionary
TEXT_TO_MORSE = {'A': '.-', 'B': '-...',
                 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-',
                 'L': '.-..', 'M': '--', 'N': '-.',
                 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--',
                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.',
                 '0': '-----', ',': '--..--', '.': '.-.-.-',
                 '?': '..--..', '/': '-..-.', '-': '-....-',
                 '(': '-.--.', ')': '-.--.-', ' ': '/'}

# Decoding dictionary (reversed)
MORSE_TO_TEXT = {value: key for key, value in TEXT_TO_MORSE.items()}


def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in TEXT_TO_MORSE:
            morse_code.append(TEXT_TO_MORSE[char])
        else:
            morse_code.append(char)
    return ' '.join(morse_code)


def morse_to_text(morse_code):
    text = []
    for code in morse_code.split(' '):
        if code in MORSE_TO_TEXT:
            text.append(MORSE_TO_TEXT[code])
        else:
            text.append(code)
    return ''.join(text)


def main():
    print("Morse Code Converter")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            print(f"Morse Code: {text_to_morse(text)}")
        elif choice == '2':
            morse = input("Enter Morse code to convert to text (use '/' for spaces): ")
            print(f"Text: {morse_to_text(morse)}")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()