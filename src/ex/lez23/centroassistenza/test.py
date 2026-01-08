import json
import requests

BASE_URL = "http://127.0.0.1:5000/"

def print_response(title, response):
    print(f"=== {title} ===")
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("JSON response:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("Raw response:")
        print(response.text)
    print("=" * 40)

if __name__ == "__main__":
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # 1) GET /
    try:
        r = requests.get(f"{BASE_URL}/", headers=headers, timeout=5)
        print_response("GET /", r)
    except requests.exceptions.RequestException as e:
        print("Errore connessione su GET /:", e)

    # 2) GET /devices
    try:
        r = requests.get(f"{BASE_URL}/devices", headers=headers, timeout=5)
        print_response("GET /devices (lista iniziale)", r)
    except requests.exceptions.RequestException as e:
        print("Errore connessione su GET /devices:", e)

    # 3) GET /devices/s1
    try:
        r = requests.get(f"{BASE_URL}/devices/s1", headers=headers, timeout=5)
        print_response("GET /devices/s1", r)
    except requests.exceptions.RequestException as e:
        print("Errore connessione su GET /devices/s1:", e)