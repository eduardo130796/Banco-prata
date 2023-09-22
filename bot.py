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
    if ('simulacao_prata' in tags ) or ('cadastrado_prata' in tags):
        nome = subscriber['full_name']
        telefone = subscriber['phone'][3:]
        cpf = subscriber['variables']['CPF']
        print(f'Nome: {nome}')
        print(f'Telefone: {telefone}')
        print(f'CPF: {cpf}')
        try:
            if validar_cpf(telefone, nome, cpf):
                # Continue com o código normal
                banco_prata(nome, cpf, telefone)
                #pass
        except CPFFormatError as e:
            # Lidar com a exceção, por exemplo, exibir uma mensagem de erro
            print(f"Erro de CPF: {e}")
        #validar_cpf(telefone, nome, cpf)

def main():
    headers = {'accept': 'application/json', 'API-KEY': '6f9d2125-3e30-49e0-b469-698f2b784231'}

    total_pages = get_total_pages(headers)
    items_per_iteration = 2  # Especifique o número de páginas a serem processadas em cada iteração

    for start_page in range(1, total_pages + 1, items_per_iteration):
        end_page = min(start_page + items_per_iteration - 1, total_pages)
        for _ in range(2):  # Repita as páginas
            for page in range(start_page, end_page + 1):
                subscribers = get_subscribers(page, headers)
                print(f"Processando página {page}")
                if not subscribers.get('results'):
                    break  # Não há mais páginas

                for subscriber in subscribers['results']:
                    process_subscriber(subscriber)
                
    print('Finalizado')

if __name__ == "__main__":
    main()