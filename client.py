"""
client.py

This module is responsible for the connection with the API
"""

import os
import requests
from dotenv import load_dotenv

WW = load_dotenv( "ww-main.env")
main_key = os.getenv("MAIN_KEY")

print (f"We beginnen met hetwachtwoord = {main_key}" )


def convert_morse_text(input_text, token_in_uze):
    """
    Convert morse text to plain text
    """
    #try:
    api_url = "http://localhost:5000/api/convert"
    data = {"input": input_text, "token": token_in_uze}
    response = requests.post(api_url, json=data, timeout=10)
    #response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
    if response.status_code == 200:
        result = response.json()
        return result["output"]
    if response.status_code == 401:
        return "AUTH_ERROR"
    return "ERROR"
    #except requests.exceptions.RequestException as e:
    #    print("Error:", e)
    #    return "ERROR"

def check_api_key(api_key):
    """
    Check if the API key is valid
    """
    try:
        response = requests.get("http://localhost:5000/api/generate_token?sleutel=" + api_key,
                                timeout=10)
        response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
        result = response.json()
        if result.get("token") is not None:
            return result["token"]
        return "notoken"
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "notoken"


def generate_password():
    """
    Generate a new password
    """
    url = 'http://localhost:5000/api/generate_password'

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        generated_password = data.get('password')
        print("Het gegenereerde wachtwoord is:", generated_password)
        return generated_password
    print("Er is een fout opgetreden bij het ophalen van het wachtwoord:", response.text)
    return None


if __name__ == "__main__":
    # token ophalen
    token = check_api_key(main_key)
    if token != "notoken":
        while True:
            text = input(
                "Voer de tekst in die je naar Morsecode wilt omzetten of voer de Morsecode in: "
            )
            output = convert_morse_text(text, token)
            if output == "AUTH_ERROR":
                print("> Ik haal even een nieuw token voor je op...")
                token = check_api_key(main_key)
                if token == "notoken":
                    print("ERROR: kan API token niet vernieuwen.")
                    os._exit()
                else:
                    output = convert_morse_text(text, token)
            print(f"Output: {output}")
            if input("Wil je nog een vertaling doen? (j/n) ").lower() == "n":
                break

    else:
        print("De API is ziek. Probeer het opnieuw.")
