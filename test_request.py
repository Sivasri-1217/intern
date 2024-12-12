import requests

url = "http://127.0.0.1:5000/route_request"
payload = {
    "type": "Leave",
    "priority": "High",
    "department": "Finance"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())
