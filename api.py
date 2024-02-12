from flask import Flask, request, jsonify

SLOT = "abc123"

app = Flask(__name__)

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

def is_morsecode(input_str):
    return all(char in '-. /' for char in input_str)

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    if data.get('sleutel') != SLOT:
        return jsonify({"result": "ERROR", "output": "Sleutel komt niet overeen"})
    user_input = data.get('input')
    if is_morsecode(user_input):
        text = decode_to_text(user_input)
        result = {"result": "Tekst", "output": text}
    else:
        morse_code = encode_to_morse(user_input)
        result = {"result": "Morsecode", "output": morse_code}
    #print(result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)