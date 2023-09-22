import requests
import time
from mensagens import *

class Whatsapp:
    BASE_URL = 'https://backend.botconversa.com.br/api/v1/webhook/subscriber'
    API_KEY = '6f9d2125-3e30-49e0-b469-698f2b784231'
    HEADERS = {
        'accept': 'application/json',
        'API-KEY': API_KEY,
    }

    #busca o id do cliente
    @staticmethod
    def get_subscriber_id(tel):
        response = requests.get(f'{Whatsapp.BASE_URL}/get_by_phone/%2B55{tel}/', headers=Whatsapp.HEADERS)
        resposta = response.json()
        return resposta['id']
    
    #deleta a etiqueta
    @staticmethod
    def delete_etiqueta(id, etiqueta):
        json_data = {}
        response = requests.delete(f'{Whatsapp.BASE_URL}/{id}/tags/{etiqueta}/', headers=Whatsapp.HEADERS, json=json_data)


    #envia fluxo
    def send_flow(id, fluxo):
        json_data = {'flow': fluxo}
        response = requests.post(f'{Whatsapp.BASE_URL}/{id}/send_flow/', headers=Whatsapp.HEADERS, json=json_data)

    #adiciona etiqueta
    def add_etiqueta(id, etiqueta):
        json_data = {}
        response = requests.post(f'{Whatsapp.BASE_URL}/{id}/tags/{etiqueta}/', headers=Whatsapp.HEADERS, json=json_data)

    #envia a mensagem
    @staticmethod
    def send_message(id, texto, fluxo=None, etiqueta=None):
        json_data = {
            'type': 'text',
            'value': f'{texto}',
        }
        response = requests.post(f'{Whatsapp.BASE_URL}/{id}/send_message/', headers=Whatsapp.HEADERS, json=json_data)
        time.sleep(3)

        if fluxo:
            json_data = {'flow': fluxo}
            response = requests.post(f'{Whatsapp.BASE_URL}/{id}/send_flow/', headers=Whatsapp.HEADERS, json=json_data)

        if etiqueta:
            json_data = {}
            response = requests.post(f'{Whatsapp.BASE_URL}/{id}/tags/{etiqueta}/', headers=Whatsapp.HEADERS, json=json_data)
    #insere um valor no campo personalizado
    @staticmethod
    def send_custom_field(id, value,campo_personalizado):
        json_data = {'value': f'{value}'}
        response = requests.post(f'{Whatsapp.BASE_URL}/{id}/custom_fields/{campo_personalizado}/', headers=Whatsapp.HEADERS, json=json_data)
        response.raise_for_status()

    #envia mensagem com o valor liberado
    @staticmethod
    def whats_saldo_liberado(tel, nome,valor):
        id = Whatsapp.get_subscriber_id(tel)
        #usa o valor para envio da mensagem
        Whatsapp.add_etiqueta(id,'4640428')
        Whatsapp.send_custom_field(id,valor,'1239332')
        Whatsapp.delete_etiqueta(id, '4640702')

    def whats_negado(tel):
        id = Whatsapp.get_subscriber_id(tel)
        Whatsapp.delete_etiqueta(id, '4640702')
    
    def cadastrado(tel, nome):
        id = Whatsapp.get_subscriber_id(tel)
        #usa o valor para envio da mensagem
        Whatsapp.add_etiqueta(id,'4640702')
        Whatsapp.delete_etiqueta(id, '4613936')

    def cpf_errado(tel):
        id = Whatsapp.get_subscriber_id(tel)
        Whatsapp.delete_etiqueta(id, '4613936')
    
#Whatsapp.whats_negado('6193526884', 'Eduardo', 'não_autorizado','30,00')
#banco_prata('Eduardo', '03015468197','6193526884')