import requests

def convert_morse_text(text):
    try:
        api_url = "http://localhost:5000/api/convert"
        data = {"input": text}
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Raises an error for bad response status (4xx or 5xx)
        result = response.json()
        return result["output"]
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "ERROR"

def main():
    while True:
        text = input("Voer de tekst in die je naar Morsecode wilt omzetten: ")
        output = convert_morse_text(text)
        print("Output:", output)
        if input("Wil je nog een vertaling doen? (ja/nee) ").lower() != "ja":
            break

if __name__ == "__main__":
    main()
