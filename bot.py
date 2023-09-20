import requests
import json
import math
from validar_cpf import *
from banco_prata import*

def get_total_pages(headers):
    params = {'page': '1'}
    response = requests.get('https://backend.botconversa.com.br/api/v1/webhook/subscribers/', params=params, headers=headers)
    response.raise_for_status()
    data_dict = json.loads(response.text)
    total = math.ceil(data_dict["count"] / len(data_dict["results"]))
    return total

def get_subscribers(page, headers):
    params = {'page': page}
    response = requests.get('https://backend.botconversa.com.br/api/v1/webhook/subscribers/', params=params, headers=headers)
    response.raise_for_status()
    return json.loads(response.text)

def process_subscriber(subscriber):
    tags = subscriber['tags']
    if 'ura' in tags:
        nome = subscriber['full_name']
        telefone = subscriber['phone'][3:]
        cpf = subscriber['variables']['CPF']
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print(f'CPF: {cpf}')
        validar_cpf(telefone, nome, cpf)
        banco_prata(nome, cpf, telefone)

def main():
    headers = {'accept': 'application/json', 'API-KEY': '6f9d2125-3e30-49e0-b469-698f2b784231'}

    total_pages = get_total_pages(headers)

    for page in range(total_pages, 0, -1):
        subscribers = get_subscribers(page, headers)
        if not subscribers.get('results'):
            break  # Não há mais páginas

        for subscriber in subscribers['results']:
            process_subscriber(subscriber)

    print('Finalizado')

if __name__ == "__main__":
    main()