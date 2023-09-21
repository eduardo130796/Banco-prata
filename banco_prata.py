from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import time
from mensagem_bot import *

def consultar_cpf(navegador, nome,cpf,tel):
        time.sleep(10)
        # Localizar todas as linhas da tabela
        rows = navegador.find_elements(By.XPATH, "//tbody/tr")
        print(len(rows))
    # Iterar sobre as linhas
        for index, row in enumerate(rows, start=1):
                # Localizar o elemento de CPF na linha atual
                cpf_element = row.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div/table/tbody/tr[{index}]/td[1]/span')
                cpf_numerico = ''.join(filter(str.isdigit, cpf_element.text))
                cpf = ''.join(filter(str.isdigit, cpf))
                print(cpf_numerico)
                # Localizar o elemento de status na mesma linha
                status_element = row.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div/table/tbody/tr[{index}]/td[3]/span')
                # Verificar se o texto do status é "FALHA NA CONSULTA" ou "CONSULTA CONCLUÍDA" e se o CPF corresponde
                if (status_element.text == "FALHA NA CONSULTA" or status_element.text == "CONSULTA CONCLUÍDA" or status_element.text =="AGUARDANDO RETORNO DA CEF") and cpf_numerico == cpf:
                        result_element = row.find_element(By.XPATH, f'//*[@id="content"]/div[2]/div/div/table/tbody/tr[{index}]')
                        
                        result_element.click()
                        try:
                                # Espera até que o elemento de resultado seja carregado
                                result_element = WebDriverWait(navegador, 30).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, '.column.taxes p.is-size-1')))
                                # Obter o texto do elemento
                                print('valor')
                                resultado = result_element.text
                                Whatsapp.whats_saldo_liberado(tel, nome,resultado)
                                print(resultado)
                        except:
                                # Se não for possível encontrar o valor disponível
                                result_element = WebDriverWait(navegador, 30).until(
                                EC.presence_of_element_located((By.CLASS_NAME, "message-body")))
                                # Obter o texto do elemento"
                                resultado = result_element.text
                                if resultado == 'Ainda não recebemos o retorno da CEF, por gentileza aguarde mais um pouco.':
                                        erro = 'aguardando'
                                        print('aguardando')
                                        Whatsapp.whats_negado(tel, nome, erro,'')
                                        return True
                                elif (resultado.split("."))[0] == 'Cliente sem saldo mínimo para antecipação (R$ 75,00)':
                                        erro = 'sem_saldo'
                                        saldo= (resultado.split("."))[1]
                                        saldo_baixo = saldo.split(":")[1].strip()
                                        print(saldo_baixo)
                                        print('semsaldo')
                                        Whatsapp.whats_negado(tel, nome, erro,saldo_baixo)
                                        return True
                                elif resultado == 'Instituição Fiduciária não possui autorização do Trabalhador para Operação Fiduciária.':
                                        erro = 'não_autorizado'
                                        print('não_autorizado')
                                        Whatsapp.whats_negado(tel, nome, erro,'')
                                        return True
                                elif resultado == 'Ação não permitida até o próximo mês.':
                                        erro = 'aniversario'
                                        print('aniversario')
                                        Whatsapp.whats_negado(tel, nome, erro,'')
                                        return True
                                Whatsapp.whats_negado(tel, nome, 'erro','sem')
                                print(resultado)
                        return True  # CPF já foi consultado
        return False  # CPF não foi consultado

def cadastrar_cpf(navegador, nome,cpf,tel):
        # Localize o campo de CPF e insira o valor
        elemento = navegador.find_element(By.XPATH,'//*[@id="content"]/div[1]/div/span/form/span[1]/div/input')

        # Usar a função execute_script para rolar até o elemento
        navegador.execute_script("arguments[0].scrollIntoView(true);", elemento)

        # Aguardar um momento para a rolagem ser concluída (opcional)
        time.sleep(2)
        
        cpf_element = navegador.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/span/form/span[1]/div/input')
        cpf_element.send_keys(cpf)

        # Localize o elemento select
        elemento_select = navegador.find_element(By.CSS_SELECTOR, 'select[data-v-15643325]')

        # Clique no elemento para abrir as opções
        elemento_select.click()
        time.sleep(2)  # Aguarde um momento para que as opções sejam exibidas

        # Clique na opção desejada 
        elemento_select.send_keys(Keys.ARROW_DOWN)
        elemento_select.send_keys(Keys.ENTER)
        time.sleep(5)

        # Clique em "Cadastrar" ou no botão relevante para finalizar o cadastro (Adapte conforme necessário)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[1]/div/span/form/button'))).click()
        time.sleep(5)
        try:
                # Espera até que o elemento de resultado seja carregado
                result_element = WebDriverWait(navegador, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.column.taxes p.is-size-1')))
                # Obter o texto do elemento
                print('valor')
                resultado = result_element.text
                Whatsapp.whats_saldo_liberado(tel, nome,resultado)
                print(resultado)
        except:
                Whatsapp.cadastrado(tel, nome)
        navegador.refresh()


def obter_cpf_outra_pagina(nome,cpf,telefone):
        # Lógica para obter o CPF de outra página
        cpf_obtido = cpf  # Substitua pelo CPF obtido

        return cpf_obtido,nome,telefone

def banco_prata(nome,cpf,telefone):
        usuario = "vandeir.professor@gmail.com"
        senha = "228KCX>YDc3Mn.KJ"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico, options=chrome_options)
        navegador.get('https://admin-cb.pratadigital.com.br')
        navegador.implicitly_wait(10)
        username = navegador.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/form/div[1]/p/input').send_keys(usuario)
        password = navegador.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/form/div[2]/p/input').send_keys(senha)
        time.sleep(2)
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[3]/p/button'))).click()
        WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navigation-container"]/div/div[3]/a[1]'))).click()
        navegador.implicitly_wait(15)

        #cpf_desejado = obter_cpf_outra_pagina()

        if consultar_cpf(navegador, nome,cpf,telefone):
                print(f"O CPF {cpf} já foi consultado.")
        else:
                cadastrar_cpf(navegador, nome,cpf,telefone)
                print(f"O CPF {cpf} foi cadastrado com sucesso.")

#banco_prata('Eduardo', '231.476.148-08','6193526884')