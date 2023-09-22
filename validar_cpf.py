from validate_docbr import CPF
from mensagem_bot import *

cpf_validator = CPF()

def validar_cpf(tel,nome,cpf):
    if cpf != None:
        cpf_numerico = ''.join(filter(str.isdigit, cpf))
        
        if cpf_numerico and cpf_validator.validate(cpf_numerico):
            print('CPF correto')
        else:
            aviso = 'erro_cpf'
            Whatsapp.cpf_errdo(tel)
            print('CPF errado')
            return True
    else: 
        Whatsapp.cpf_errdo(tel)
    