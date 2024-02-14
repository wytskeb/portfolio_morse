import requests
import os
from dotenv import load_dotenv

ww = load_dotenv( "ww-main.env")
main_key = os.getenv("MAIN_KEY")

print (f"We beginnen met hetwachtwoord = {main_key}" )


def convert_morse_text(text, token):
    try:
        api_url = "http://localhost:5000/api/convert"
        data = {"input": text, "token": token}
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
        result = response.json()
        return result["output"]
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "ERROR"

def check_api_key(main_key):
    try:
        response = requests.get("http://localhost:5000/api/generate_token?sleutel=" + main_key)
        response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
        result = response.json()
        
        if result.get("token") is not None:
            return result["token"]
        else:
            return "notoken"
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "notoken"


def generate_password():
    url = 'http://localhost:5000/api/generate_password'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        generated_password = data.get('password')
        print("Het gegenereerde wachtwoord is:", generated_password)
        return generated_password
    else:
        print("Er is een fout opgetreden bij het ophalen van het wachtwoord:", response.text)


if __name__ == "__main__":
    # token ophalen
    token = check_api_key(main_key)
    print(token)
    if token != "notoken":
        while True:
            text = input(
                "Voer de tekst in die je naar Morsecode wilt omzetten of voer de Morsecode in: "
            )
            output = convert_morse_text(text, token)
            print("Output:", output)
            if input("Wil je nog een vertaling doen? (ja/nee) ").lower() != "ja":
                break

    else:
        print("De API is ziek. Probeer het opnieuw.")
