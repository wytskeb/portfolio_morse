from flask import Flask, request, jsonify
import os

from tokens import Tokens

from dotenv import load_dotenv

ww = load_dotenv("ww-api.env")
api_key = os.getenv("API_KEY")

print (f"we beginnen met het wachtwoord: {api_key}" )

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
    global my_tokens
    data = request.json
    if my_tokens.check_token(data.get('token')):
        user_input = data.get('input')
        if is_morsecode(user_input):
            text = decode_to_text(user_input)
            result = {"result": "Tekst", "output": text}
        else:
            morse_code = encode_to_morse(user_input)
            result = {"result": "Morsecode", "output": morse_code}
        return jsonify(result)
    else:
        return jsonify({"result": "ERROR", "output": "Token komt niet overeen"})

@app.route('/api/generate_token', methods=['GET'])
def generate_token():
    global my_tokens
    global api_key
    if request.args.get('sleutel') == api_key:
        # Verstuur het wachtwoord naar de frontend
        token = my_tokens.add_token()
        print(f"Nieuw token: {token}")
        print(f"Token lijst: {my_tokens.dict_tokens()}")
        return jsonify({"token": token}), 200
    else:
        return jsonify({"result": "ERROR", "output": "Sleutel komt niet overeen"}), 401


if __name__ == "__main__":
    my_tokens = Tokens()
    app.run(debug=True)