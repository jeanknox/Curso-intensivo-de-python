import json

lista = [i for i in range(100)]



with open("sequencia.json", "w") as arquivo:
    json.dump(lista,arquivo)
