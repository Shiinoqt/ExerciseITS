import json
import requests

# Removed trailing slash for cleaner concatenation
BASE_URL = "http://127.0.0.1:5000"

if __name__ == "__main__":
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # 1) GET / (Home)
    r = requests.get(f"{BASE_URL}/", headers=headers)
    print("GET /", r.status_code)

    # 2) GET /devices (List all)
    r = requests.get(f"{BASE_URL}/devices", headers=headers)
    print("GET /devices", r.status_code, len(r.json()), "devices found")

    # 3) POST /devices (Create)
    new_device = {
        "id" : "s2",
        "type": "smartphone",
        "model": "Galaxy S21",
        "customer_name": "Luca Bianchi",
        "purchase_year": 2021,
        "status": "in repair",
        "has_protective_case": True,
        "storage_gb": 128
    }
    # Using 'json=' parameter automatically sets headers and dumps to string
    r = requests.post(f"{BASE_URL}/devices", json=new_device)
    print("POST /devices", r.status_code, r.json())

    # 4) GET /devices/s2
    r = requests.get(f"{BASE_URL}/devices/s2", headers=headers)
    print("GET /devices/s2", r.status_code, r.json())

    # 5) PATCH /devices/s2/status
    patch_data = {
        "status": "repaired"
    }

    r = requests.patch(f"{BASE_URL}/devices/s2/status", headers=headers, data=json.dumps(patch_data))
    print("PATCH /devices/s2/status", r.status_code, r.json())

    # 6) PUT /devices/s3
    put_data = {
        "id" : "s3",
        "type": "smartphone",
        "model": "Galaxy S21 Ultra",
        "customer_name": "Luca Bianchi",
        "purchase_year": 2021,
        "status": "delivered",
        "has_protective_case": True,
        "storage_gb": 256
    }   

    r = requests.put(f"{BASE_URL}/devices/s2", headers=headers, data=json.dumps(put_data))
    print("PUT /devices/s2", r.status_code, r)

    # 7) DELETE /devices/s2
    r = requests.delete(f"{BASE_URL}/devices/s2", headers=headers)
    print("DELETE /devices/s2", r.status_code, r)

    # 8) GET /devices/s2json())
    r = requests.get(f"{BASE_URL}/devices/s2", headers=headers)
    print("GET /devices/s2", r.status_code, r)