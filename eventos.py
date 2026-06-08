import random
import time


def gerar_evento_aleatorio(perfil):
    if perfil["mes_atual"] == 1:
        return
    eventos_bons = [
        {"descricao": "Você recebeu um bônus no trabalho!", "valor": 500.0},
        {"descricao": "Você achou dinheiro na rua!", "valor": 100.0},
        {"descricao": "Você ganhou um presente em dinheiro!", "valor": 300.0}
    ]

    eventos_ruins = [
        {"descricao": "Seu carro quebrou!", "valor": 800.0},
        {"descricao": "Você recebeu uma multa!", "valor": 200.0},
        {"descricao": "Problema de saúde inesperado!", "valor": 600.0}
    ]

    numero = random.randint(1, 100)
        
    if numero <= 40:
        evento = random.choice(eventos_bons)
        perfil["saldo"] += evento["valor"]
        print(f"\n {evento['descricao']}")    
        print(f" Ganhou R$ {evento['valor']:,.2f}") 
    else:
        evento = random.choice(eventos_ruins)
        perfil["saldo"] -= evento["valor"]
        print(f"\n {evento['descricao']}")
        print(f" Perdeu R$ {evento['valor']:,.2f}")


    print(f" Saldo atual: R$ {perfil['saldo']:,.2f}")
    time.sleep(1.5)
