import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

resposta = requests.get(url)
print("Status code:", resposta.status_code)
resposta_get = resposta.json()
print(resposta_get.keys())

print(resposta_get["total_count"])

primeiro = resposta_get[0]
print("Primeiro{}".format(primeiro["owner"]["login"]))
