import json

with open("sequencia.json","r") as arquivo:
    numbers = json.load(arquivo)
print(numbers)
