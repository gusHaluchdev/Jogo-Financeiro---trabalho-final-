import time 


CLASSES =  { 
        "1":{
        "nome_classe": "Estagiário de ti",
        "salario": 1000.0,
        "divida": 5000.0,
        "saldo_inicial": 200.0, 
        "dificuldade":"Difícil",
        "acoes_por_mes": 2,
        "freelance_min": 50.0,
        "freelance_max": 300.0,
        "aluguel": 600.0,
        "luz_agua_net": 200.0,
        "alimentacao": 400.0,
        "transporte": 150.0,
        "pagamento_minimo_divida": 350.0
        },
        "2":{
        "nome_classe": "Repositor do atacadão",
        "salario": 2000.0,
        "divida": 5000.0,
        "saldo_inicial": 800.0,
        "dificuldade":"Normal",
        "acoes_por_mes": 3,
        "freelance_min": 50.0,
        "freelance_max": 500.0,
        "aluguel": 800.0,
        "luz_agua_net": 250.0,
        "alimentacao": 500.0,
        "transporte": 200.0,
        "pagamento_minimo_divida": 550.0

        },
        "3":{
        "nome_classe": "Médico",
        "salario": 7000.0,
        "divida": 10000.0,
        "saldo_inicial": 1500.0,
        "dificuldade":"Fácil",
        "acoes_por_mes": 4,
        "freelance_min": 200.0,
        "freelance_max": 1000.0,
        "aluguel": 2000.0,
        "luz_agua_net": 400.0,
        "alimentacao": 800.0,
        "transporte": 300.0,
        "pagamento_minimo_divida": 1200.0
    }
}


def exibir_introducao():
    print("\n" + "=" * 50 )
    print(" BEM-VINDO AO SISTEMA FINANCEIRO")
    print("="* 50)
    print(""" Nesse jogo você assume o papel de uma pessoa comum que precisa organizar sua vida financeira ao longo dos meses.
          Seu objetivo é atingir RS50.000,00 ao longo de 24 meses antes de entrar em falência (saldo abaixo de RS - 5.000,00).
          A cada mês você poderá:
          - Adicionar receitas 
          - Registrar despesas
          - Investir dinheiro
          - Pagar dívidas
          - Criar e acompanhar metas 
          - Verificar saldo e dívida
          Eventos aleatórios podem ocorrer ao longo da jogatina podendo ajudar ou prejudicar. Tome boas decisões e conquiste sua independência""")
    input ("Pressione enter para continuar")
    time.sleep(0.5)

 
def configurar_perfil():
    print("\n" + "=" * 50 )
    print(" VAMOS CONFIGURAR SEU PERFIL")
    print("="* 50)
    
    nome = input("\n Qual seu nome parceiro? ").strip()
    while not nome:
        print("Nome não pode ser vazio")
        nome = input("\n Qual seu nome parceiro? ").strip()
 
 
    print(f"\n Olá {nome}! Agora vamos definir a sua classe/dificuldade do jogo")
    for id, classe in CLASSES.items():
        print(f"({id}) {classe['nome_classe']} {classe['dificuldade']}")
        print(f"Salário mensal: R${classe['salario']:,.2f}" )
        print( f"Divida: R${classe['divida']:,.2f}")
        print(f"Saldo inicial: R${classe['saldo_inicial']:,.2f}")

    while True:
        escolha = input("\nclasse escolhida: ").strip()
        if escolha in CLASSES:
            classe_escolhida = CLASSES[escolha]
            break
        else:
            print("Opção inválida, Digite 1, 2 ou ,3")

    perfil= {
    "nome":     nome,
    "classe":   classe_escolhida["nome_classe"],
    "acoes_por_mes": classe_escolhida["acoes_por_mes"],
    "saldo":    classe_escolhida["saldo_inicial"],
    "salario":    classe_escolhida["salario"],
    "divida_total":classe_escolhida["divida"],
    "mes_atual":    1,
    "freelance_min": classe_escolhida["freelance_min"],
    "freelance_max": classe_escolhida["freelance_max"],
    "aluguel":     classe_escolhida["aluguel"],
    "luz_agua_net": classe_escolhida["luz_agua_net"],
    "alimentacao": classe_escolhida["alimentacao"],
    "transporte":  classe_escolhida["transporte"],
    "investimentos_ativos": [],
    "pagamento_minimo_divida": classe_escolhida["pagamento_minimo_divida"],
    "metas": [],
    "max_metas": 3,
    "historico": [],
    }
    
    print(f"\n Perfil criado! Boa sorte,{nome}")
    print(f"\n Classe escolhida: {classe_escolhida['nome_classe']}")
    print(f"\n Dificuldade: {classe_escolhida['dificuldade']}")
    print(f"Seu saldo inicial é: R$ {perfil['saldo']:,.2f}")
    print(f"Salário mensal: R$ {perfil['salario']:,.2f}")
    print(f"Dívida Inicial: R$ {perfil['divida_total']:,.2f}")

    time.sleep(1.5)
    return perfil
