from validate_docbr import CPF
from mensagem_bot import *
cpf_validator = CPF()

class CPFFormatError(Exception):
    pass

def validar_cpf(tel, nome, cpf):
    # Verifique se o CPF não é vazio
    if cpf:
        # Remova todos os caracteres não numéricos do CPF
        cpf_numerico = ''.join(filter(str.isdigit, cpf))

        if cpf_validator.validate(cpf_numerico):
            print('CPF correto')
            return True  # CPF válido
        else:
            aviso = 'erro_cpf'
            Whatsapp.cpf_errado(tel)
            print('CPF errado')
            raise CPFFormatError('CPF inválido')  # Lança uma exceção quando o CPF é inválido
    else:
        # CPF é nulo ou vazio
        Whatsapp.cpf_errado(tel)
        print('CPF nulo ou vazio')
        raise CPFFormatError('CPF nulo ou vazio')  # Lança uma e