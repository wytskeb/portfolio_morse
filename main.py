MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Reverse the MORSE_CODE_DICT to create a dictionary for decoding
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encode_to_morse(text):
    morse_code = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            morse_code += char + ' '
    return morse_code

def decode_to_text(morse_code):
    text = ''
    for code in morse_code.split(' '):
        if code in REVERSE_MORSE_CODE_DICT:
            text += REVERSE_MORSE_CODE_DICT[code]
        else:
            text += code
    return text

def main():
    while True:
        choice = input("Wil je tekst naar morsecode omzetten (1) of morsecode naar tekst (2)? ")
        
        if choice == '1':
            text = input("Voer de tekst in die je naar morsecode wilt omzetten: ")
            morse_code = encode_to_morse(text)
            print("Morsecode:", morse_code)
        elif choice == '2':
            morse_code = input("Voer de morsecode in die je naar tekst wilt omzetten: ")
            text = decode_to_text(morse_code)
            print("Tekst:", text)
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

        cont = input("Wil je nog een vertaling doen? (ja/nee) ").lower()
        if cont != 'ja':
            break

if __name__ == "__main__":
    main()