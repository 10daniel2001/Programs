import requests

url = "https://jsonplaceholder.typicode.com/users/1"

resposta = requests.get(url, timeout=10)

print("Status:", resposta.status_code)

if resposta.ok:
    usuario = resposta.json()
    print("Nome:", usuario["name"])
    print("Email:", usuario["email"])