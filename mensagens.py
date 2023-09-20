from datetime import datetime
import pytz


class mensagens:
    @staticmethod
    def saudacao_horario_brasil():
        tz_brasil = pytz.timezone('America/Sao_Paulo')  # Configuração do fuso horário brasileiro
        agora_brasil = datetime.now(tz_brasil)
        hora_brasil = agora_brasil.hour

        if hora_brasil < 12:
            saudacao = "Bom dia"
        elif hora_brasil < 18:
            saudacao = "Boa tarde"
        else:
            saudacao = "Boa noite"

        return saudacao
    
    @staticmethod
    def mensagem_1(nome,valor_liquido):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
            f"{saudacao}, {nome}!\n\n"
            "Obrigado por aguardar,\n\n"
            f"Você possui *{valor_liquido}*, disponíveis para saque do seu FGTS."
        )

        return texto

    @staticmethod
    def mensagem_2(nome_1,valor):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
        f"{saudacao}, {nome_1}'!\n\n"
        "Obrigado por aguardar,\n\n"
        "Autoriza no seu aplicativo do FGTS os Bancos:\n"
        "(1) *QI SOCIEDADE DE CRÉDITO*;\n"
        "(2) MERCANTIL;\n"
        "_(obs.: após a liberação, favor nos comunicar para darmos andamento na consulta de saque)._"
        )
        return texto
    
    @staticmethod
    def mensagem_3(nome_1,valor):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
        f"{saudacao}, {nome_1}!\n\n"
        "Obrigado por aguardar,\n\n"
        f"Sua margem (R$ {valor}) para liberação de saque está abaixo do mínimo aceita pelos Bancos. Monitoraremos todos os dias sua conta e quando ocorrer novo aporte entraremos em contato, pode ser?"
        )
        return texto
    
    @staticmethod
    def mensagem_4(nome_1,valor_liquido):
        texto = (
                f'Ainda não obtivemos o retorno do Banco, pedimos que aguarde mais alguns minutos.'
        )
        return texto
    
    @staticmethod
    def mensagem_5(nome_1,valor_liquido):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
            f"{saudacao}, {nome_1}!\n\n"
            f"Poderia confirmar o seu CPF:{valor_liquido}, está constando como inválido."
        )
        return texto
    
    @staticmethod
    def mensagem_6(nome_1,valor_liquido):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
            f"{saudacao}, {nome_1}!\n\n"
            f"Conforme retorno do banco, a liberação para o saque estará disponível somente no próximo mês, o que geralmente ocorre devido à proximidade do seu aniversário."
        )
        return texto
    
    @staticmethod
    def mensagem_7(nome_1):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
            f"{saudacao}, {nome_1}!\n\n"
            f"Foi feita a solicitação para o banco em instantes retornaremos com a resposta da simulação"
        )
        return texto

    @staticmethod
    def mensagem_erro_padrao(nome_1,valor_liquido):
        saudacao = mensagens.saudacao_horario_brasil()
        texto = (
            f"{saudacao}, {nome_1}!\n\n"
            'Não obtivemos resposta do banco, mas um de nossos atendentes irá auxiliá-lo.'
        )
        return texto

    