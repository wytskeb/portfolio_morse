import requests
import os
from dotenv import load_dotenv

ww = load_dotenv( "ww-main.env")
main_key = os.getenv("MAIN_KEY")

print (f"wachtwoord = {main_key}" )


def convert_morse_text(text):
    try:
        api_url = "http://localhost:5000/api/convert"
        data = {"input": text, "sleutel": main_key}
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
        result = response.json()
        return result["output"]
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "ERROR"

def check_api_key():
    try:
        api_url = "http://localhost:5000/api/convert"
        data = {"sleutel": main_key, "input": "HOI"}
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
        result = response.json()
        if result.get("output") == ".... --- .. ":
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return False

def main():
    while True:
        text = input(
            "Voer de tekst in die je naar Morsecode wilt omzetten of voer de Morsecode in: "
        )
        output = convert_morse_text(text)
        print("Output:", output)
        if input("Wil je nog een vertaling doen? (ja/nee) ").lower() != "ja":
            break


if __name__ == "__main__":
    if check_api_key():
        main()
    else:
        print("De API sleutel komt niet overeen of de API is ziek. Probeer het opnieuw.")