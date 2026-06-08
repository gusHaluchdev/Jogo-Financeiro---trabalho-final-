import time 
import apostas
import math

def menu_acoes(perfil):
    acoes_disponiveis = perfil["acoes_por_mes"]
    acoes_usadas = 0
    while acoes_usadas< acoes_disponiveis:
        restantes = acoes_disponiveis - acoes_usadas
        print(f"\n---AÇÕES DO MÊS{perfil['mes_atual']}---({restantes}ações)")
        print("(1) Adicionar receita")
        print("(2) Registrar despesa")
        print("(3) Realizar investimento")
        print("(4) Pagar dívida")
        print("(5) Gerenciar metas")
        print("(6) Ver histórico")
        print("(7) Casa de apostas")

        escolha = input("\nEscolha uma ação: ").strip()
        if escolha == "1":
            adicionar_receita(perfil)
            acoes_usadas += 1
        elif escolha == "2":
            registrar_despesa(perfil)
            acoes_usadas += 1
        elif escolha == "3":
            realizar_investimento(perfil)
            acoes_usadas += 1
        elif escolha == "4":
            pagar_divida(perfil)
            acoes_usadas += 1
        elif escolha == "5":
            gerenciar_metas(perfil)
            acoes_usadas += 1
        elif escolha == "6":
            ver_historico(perfil)
            acoes_usadas += 1
        elif escolha == "7":
            apostas.casa_de_apostas(perfil)
            acoes_usadas += 1
        else:
            print("Opção inválida parceiro! Tente novamente, Digite um numero de 1 a 6!")
    print(f"\n Você usou todas as ações desse mês!")
    time.sleep(1.0)

def adicionar_receita(perfil):
    print("\n FREELANCE")
    print(f"Limite para {perfil['classe']}: "
        f"R${perfil['freelance_min']:,.2f} até R${perfil['freelance_max']:,.2f}")
    while True:
        try:
            valor = float(input("\n Valor do freelance: R$ "))
            if valor < perfil["freelance_min"]:
                print(f"Valor mínimo é R$ {perfil['freelance_min']:,.2f}")
            elif valor > perfil["freelance_max"]:
                print(f"Valor maximo é R$ {perfil['freelance_max']:,.2f}")
            else:
                break
        except ValueError:
            print("Digite um número válido parceiro")

    perfil["saldo"] += valor
    perfil["historico"].append({
    "mes":      perfil["mes_atual"],
    "tipo":     "Freelance",
    "descricao": f"Freelance de R$ {valor:,.2f}",
    "valor":    valor
})
    print(f"\n Freelance de R${valor:,.2f} adicionado!")
    print(f" Saldo atual: R$ {perfil['saldo']:,.2f}")
    time.sleep(1.0)

def registrar_despesa(perfil):
    print("\n Registrar Despesa")
    print(" Escolha a categoria ")
    print("(1) Lazer ")
    print("(2) Saúde ")
    print("(3) Outros ")

    while True:
        categoria = input("\n Categoria: ").strip()
        if categoria in ["1","2","3"]:
            break
        else:
            print("Opção inválida parceiro. Digite 1, 2 ou 3 ")

    nomes = {"1": "Lazer", "2": "Saúde", "3": "Outros"}
    nomes_categoria = nomes[categoria]

    while True:
        try:
            valor = float(input(f"\n Valor gasto em {nomes_categoria}: R$ "))
            if valor <= 0:
                print(" O valor deve ser maior que zero")
            else:
                break
        except ValueError:
            print("Digite um numero válido")

    perfil["saldo"] -= valor
    perfil["historico"].append({
    "mes":      perfil["mes_atual"],
    "tipo":     f"Despesa {nomes_categoria}",
    "descricao": f"Gasto em {nomes_categoria}",
    "valor":    valor
})
    print(f"\n Despesa de R$ {valor:,.2f} em {nomes_categoria} registrada!")
    print(f"\n Saldo atual: R$ {perfil['saldo']:,.2f}")
    time.sleep(1.0)

def realizar_investimento(perfil):
    print("\n MOMENTO DE INVESTIR ")
    print("\n Escolha uma opção ")
    print("\n (1) Poupança - 0.5% ao mês [baixo risco]")
    print("\n (2) Tesouro  - 0.9% ao mês [baixo risco]")   
    print("\n (3) Ações    - 3.0% ao mês [médio risco]")
    print("\n (4) Cripto   - 8.0% ao mês [alto risco]")
    print("\n (5) Sair")

    while True:
        escolha = input("\n Opção: ").strip()
        if escolha in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Opção inválida parceiro escolha algo entre 1 a 5 ")

    if escolha == "5":
        print("\n Volte sempre parceiro! ")
        return
    tipos = { 
        "1": {"tipo": "Poupança", "taxa": 0.005},
        "2": {"tipo": "Tesouro",  "taxa": 0.009},
        "3": {"tipo": "Ações",    "taxa": 0.03},
        "4": {"tipo": "Cripto",   "taxa": 0.08}

    }
    investimento = tipos[escolha]

    while True:
        try:
            valor = float(input(f"\n Quanto deseja investir em {investimento['tipo']}? R$ "))
            if valor <= 0:
                print("O valor deve ser maior que zero")
            elif valor > perfil["saldo"]:
                print(f"Voce nao tem saldo suficiente. Seu saldo é R$ {perfil['saldo']:,.2f}")
            else:
                break
        except ValueError:
            print("Digite um número valido parceiro")

    perfil["saldo"] -= valor
    perfil["historico"].append({
    "mes":      perfil["mes_atual"],
    "tipo":     f"Investimento {investimento['tipo']}",
    "descricao": f"Aplicado em {investimento['tipo']}",
    "valor":    valor
})
    perfil["investimentos_ativos"].append({
        "tipo":  investimento["tipo"],
        "taxa":  investimento["taxa"],
        "valor": valor
    })

    print(f"\n Investimento de R$ {valor:,.2f} em {investimento['tipo']} registrado!")   
    print(f"\n Rendimento mensal estimado: R$ {valor * investimento['taxa']:,.2f}")
    print(f"\n Saldo atual: R$ {perfil['saldo']:,.2f}")
    time.sleep(1.0)    

def pagar_divida(perfil):
    print("\n Bora pagar as contas que é bom")
    print(f"Dívida atual: R$ {perfil['divida_total']:,.2f}")
    print(f"\n Saldo atual: R$ {perfil['saldo']:,.2f}")
    print(f"Pagamento mínimo: R$ {perfil['pagamento_minimo_divida']:,.2f}")

    if perfil["divida_total"] <= 0: 
        print("\n Parabens, voce pagou todas as contas")
        return

    while True:
        
        print("voltando para o menu ")
        try:
            valor = float(input("\n Quanto deseja pagar?(0 para voltar ) R$ "))
            if valor == 0:
                print(" voltando para o menu")
                return
            elif valor <= 0:
                print("O valor deve ser maior que zero")
            elif valor < perfil["pagamento_minimo_divida"]:
                print(f"O valor deve ser maior que R$ {perfil['pagamento_minimo_divida']:,.2f}")
            elif valor > perfil["saldo"]:
                print(f"Voce nao tem saldo suficiente. Seu saldo é R$ {perfil['saldo']:,.2f}")
            else:
                break
        except ValueError:
            print("Digite um número válido parceiro")

    perfil["saldo"] -= valor    
    perfil["divida_total"] -= valor
    perfil["historico"].append({
    "mes":      perfil["mes_atual"],
    "tipo":     "Pagamento de dívida",
    "descricao": f"Pagamento de R$ {valor:,.2f}",
    "valor":    valor
})
    print(f"\n Pagamento de R$ {valor:,.2f} registrado!")
    print(f"\n Dívida restante: R$ {perfil['divida_total']:,.2f}")
    print(f"\n Saldo atual: R$ {perfil['saldo']:,.2f}")

    if perfil["divida_total"] == 0:
        print("\n Parabens, voce pagou todas as contas!")

    time.sleep(1.0)

def gerenciar_metas(perfil):
    print("\n Gerenciar metas")
    if not perfil["metas"]:
        print("Você não tem metas cadastradas")
    else:
        print("Suas metas cadastradas:")
        for i, meta in enumerate(perfil["metas"]):   
            progresso = min(meta["acumulado"] / meta["valor_alvo"] * 100, 100)   
            blocos = int(progresso / 5)
            barra = "█" * blocos + "░" * (20 - blocos)
            print(f"\n {i}. {meta['nome']}")
            print(f"   Valor alvo: R$ {meta['valor_alvo']:,.2f}")
            print(f"   Acumulado: R$ {meta['acumulado']:,.2f}")
            print(f"   Contribuição: R$ {meta['contribuicao_mensal']:,.2f}")
            print(f"   [{barra}] {progresso:.1f}%")

    print("\n (1) Criar nova meta ")
    print("\n (2) Excluir meta ")
    print("\n (3) Voltar ")

    while True:
        opcao = input("\n Opção: ").strip()
        if opcao in ["1", "2", "3"]:
            break
        else:
            print("Opção inválida parceiro. Digite 1, 2 ou 3")

    if opcao == "1":
        if len(perfil["metas"]) >= perfil["max_metas"]:
            print(f"\n Limite de {perfil['max_metas']} metas atingido.")
            time.sleep(1.0)
            return 
        
        nome = input("\n Nome da meta: ").strip()
        while not nome:
            print("Nome nao pode ser vazio")
            nome = input("\n Nome da meta: ").strip()

        while True:
            try:
                valor_alvo = float(input("\n Valor alvo: R$ "))
                if valor_alvo <= 0:
                    print("O valor alvo deve ser maior que zero")
                else:
                    break
            except ValueError:
                print("Digite um número valido parceiro")

        while True:
            try:
                contribuicao = float(input("\n Contribuição mensal: R$ "))
                if contribuicao <= 0:
                    print("A contribuição deve ser maior que zero")
                else:
                    break
            except ValueError:
                print("Digite um número valido parceiro")

        perfil["metas"].append({
            "nome":              nome,
            "valor_alvo":        valor_alvo,
            "acumulado":         0.0,
            "contribuicao_mensal": contribuicao
        })
        meses_restantes = math.ceil(valor_alvo / contribuicao)
        print(f"\n  Meta '{nome}' cadastrada com sucesso!")
        print(f"  Previsão: {meses_restantes} meses para concluir")
        time.sleep(1.0)

    elif opcao == "2":
        if not perfil["metas"]:
            print("\n Você nao tem metas cadastradas")
        else:
            while True:
                try:
                    idx = int(input("\n Número da meta para excluir: "))
                    if 1 <= idx <= len(perfil["metas"]):
                        break
                    else:
                        print("Opção inválida parceiro. Digite um número entre 1 e", len(perfil["metas"]))  
                except ValueError:
                    print("Digite um número valido parceiro")
            perfil["metas"].pop(idx - 1)
            print("\n Meta excluida com sucesso!")
            time.sleep(1.0)

def ver_historico(perfil):
    print("\n Historico de transações")
    if not perfil["historico"]:
        print("Nenhuma transação registrada")
        time.sleep(1.0)
        return 
    for i, transacao in enumerate(perfil["historico"], 1):
        print(f"\n {i}. [{transacao['mes']}] {transacao['tipo']}")
        print(f" Descrição: {transacao['descricao']}")
        print(f" Valor: R$ {transacao['valor']:,.2f}")
    time.sleep(1.0)
