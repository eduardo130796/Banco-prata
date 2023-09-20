import requests
import json
import math
from validar_cpf import *
import schedule     
import re      
from banco_prata import *                                                                                                                                      


def apibot():

        headers = {
            'accept': 'application/json',
            'API-KEY': '6f9d2125-3e30-49e0-b469-698f2b784231',
        }
        params = {
            'page': '1',
        }
        # pega a quantidade de pessoas cadastradas
        response = requests.get('https://backend.botconversa.com.br/api/v1/webhook/subscribers/', params=params, headers=headers)
        data_dict = json.loads(response.text)
        paginas = data_dict["count"]
        separado = paginas/25
        
        total = math.ceil(separado)
        #passa por todas as paginas
        for x in range(total,0,-1):    
            params = {
            'page': f'{x}',
        }
            response = requests.get('https://backend.botconversa.com.br/api/v1/webhook/subscribers/', params=params, headers=headers)
            data_dict = json.loads(response.text)         
            #verifica cada usuario se possui a etiqueta
            k = len(data_dict["results"])
            
            for i in range(k):
                t=data_dict["results"][i]['tags']       
                if ('ura' in t):
                    nome = data_dict["results"][i]['full_name']
                    telefone = data_dict["results"][i]['phone']
                    cpf = data_dict["results"][i]['variables']['CPF']
                    print(f'Nome:{nome}')
                    print(f'Telefone:{telefone}')
                    print(f'CPF:{cpf}')
                    telefone = telefone[3:]
                    #validação do CPF
                    validar_cpf(telefone,nome,cpf)
                    obter_cpf_outra_pagina(nome,cpf,telefone)

        print('finalizado')

while True:
 
    schedule.every(10).seconds.do(apibot)
    try:
        schedule.run_pending()
    except:
        continue
