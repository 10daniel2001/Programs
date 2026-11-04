import json

meu_dados = {
    "Nome": "Carlos daniel",
    "Idade": 25
}


texto = json.dumps(meu_dados)

print(texto)