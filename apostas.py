import random
import time


def casa_de_apostas(perfil):
    print("\n" + "=" * 50)
    print("       BEM-VINDO À CASA DE APOSTAS!")
    print("      Aqui sua diversão é garantida!")
    print("=" * 50)
    print("         Jogue com responsabilidade!")
    print("       Proibido para menores de 18 anos")
    print("=" * 50)
    print(f"  Saldo disponível: R$ {perfil['saldo']:,.2f}")
    print("\n  Escolha o jogo:")
    print("  (1) Tigrinho")
    print("  (2) Roleta")
    print("  (3) Blackjack")
    print("  (4) Loteria")
    print("  (5) Aposta esportiva")
    print("  (6) Sair")

    while True:
        escolha = input("\n  Jogo escolhido: ").strip()
        if escolha in ["1", "2", "3", "4", "5", "6"]:
            break
        else:
            print("Opção inválida. Digite de 1 a 6.")

    if escolha == "1":
        tigrinho(perfil)
    elif escolha == "2":
        roleta(perfil)
    elif escolha == "3":
        blackjack(perfil)
    elif escolha == "4":
        loteria(perfil)
    elif escolha == "5":
        jogo_futebol(perfil)
    elif escolha == "6":
        print("\n  Até a próxima!")
        time.sleep(1.0)


def tigrinho(perfil):
    print("\n  🐯 TIGRINHO 🐯")
    print("  [ 🐯 | 🐼 | 🐷 | 🦁 | 🐭 | 🦊 ]")
    print("  Se você conseguir 3 bichinhos iguais, o valor da aposta é multiplicado por 10" )
    print("        Se você conseguir 2 bichinhos iguais, o valor da aposta é dobrado")

    while True:
        try:
            valor = float(input(f"\nSeu saldo é de R$ {perfil['saldo']:,.2f} \n Quanto você quer apostar parceiro? R$ "))
            if valor <= 0:
                print("  Valor deve ser maior que zero.")
            elif valor > perfil["saldo"]:
                print("  Saldo insuficiente!")
            else:
                break
        except ValueError:
            print("  Digite um número válido.")

    perfil["saldo"] -= valor

    simbolos = ["🐯", "🐼", "🐷", "🦁", "🐭", "🦊"]
    print("\n  Girando", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    s1 = random.choice(simbolos)
    print(f"\n  [ {s1} ]")
    time.sleep(1.5)

    s2 = random.choice(simbolos)
    print(f"  [ {s1} | {s2} ]")
    time.sleep(1.5)

    s3 = random.choice(simbolos)
    print(f"  [ {s1} | {s2} | {s3} ]")
    time.sleep(1.5)

    if s1 == s2 == s3:
        ganho = valor * 10
        perfil["saldo"] += ganho
        print(f"\n  QUEBROU A BANCA! +R$ {ganho:,.2f}")
        print("Acho que você está com a mão quente!")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        ganho = valor * 2
        perfil["saldo"] += ganho
        print(f"\n  DECOLANDO! Você conseguiu 2 iguais! +R$ {ganho:,.2f}")
        print("Você está entrando no ritmo da vitória")
    else:
        print(f"\n  Você perdeu! -R$ {valor:,.2f}")
        print("O tigre ainda está segurando seu prêmio!")

    print(f"  Saldo atual: R$ {perfil['saldo']:,.2f}")
    print("Vamos continuar? Sinto que você está perto de algo grande.")
    time.sleep(1.0)

    print("\n  (1) Jogar novamente")
    print("  (2) Sair")

    while True:
        opcao = input("\n  Opção: ").strip()
        if opcao == "1":
            tigrinho(perfil)
            break
        elif opcao == "2":
            print("\n  Te esperamos na próxima!")
            time.sleep(1.0)
            break
        else:
            print("  Opção inválida. Digite 1 ou 2.")



def roleta(perfil):
    print("\n                🎡 ROLETA 🎡")
    print("     Faça sua escolha entre vermelho ou preto!")
    print("  Você tem a chance de dobrar o valor da sua aposta!")

    while True:
        try:
            valor = float(input(f"\nSeu saldo é de R$ {perfil['saldo']:,.2f} \n Quanto você quer apostar parceiro? R$ "))
            if valor <= 0:
                print("  O valor deve ser maior que zero.")
            elif valor > perfil["saldo"]:
                print("  Saldo insuficiente!")
            else:
                break
        except ValueError:
            print("  Digite um número válido.")

    while True:
        cor = input("\n  Vermelho ou preto?: ").strip().lower()
        if cor in ["vermelho", "preto"]:
            break
        else:
            print("  Digite vermelho ou preto.")

    print("\n  A roleta está girando", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    resultado = random.choice(["vermelho", "preto"])
    perfil["saldo"] -= valor

    if cor == resultado:
        ganho = valor * 2
        perfil["saldo"] += ganho
        print(f"\n  VOCÊ GANHOU! Saiu a cor {resultado}! +R$ {ganho:,.2f}")
        print("Acho que você está com a mão quente!")
    else:
        print(f"\n Você perdeu! Saiu a cor {resultado}, -R$ {valor:,.2f}")
        print("A roleta ainda está segurando seu prêmio!")

    print(f"  Saldo atual: R$ {perfil['saldo']:,.2f}")
    print("Vamos continuar? Sinto que você está perto de algo grande.")
    time.sleep(1.0)

    print("\n  (1) Jogar novamente")
    print("  (2) Sair")
    while True:
        opcao = input("\n  Opção: ").strip()
        if opcao == "1":
            roleta(perfil)
            break
        elif opcao == "2":
            print("\n  Te esperamos na próxima!")
            time.sleep(1.0)
            break
        else:
            print("  Opção inválida. Digite 1 ou 2.")


def blackjack(perfil):
    print("\n                      🃏 BLACKJACK 🃏")
    print("           Chegue mais perto de 21 sem ultrapassar!")
    print("  Dealer para em 17, se empatar você recebe o dinheiro de volta.")

    while True:
        try:
            valor = float(input(f"\nSeu saldo é de R$ {perfil['saldo']:,.2f} \n Quanto você quer apostar parceiro? R$ "))
            if valor <= 0:
                print("  O valor deve ser maior que zero.")
            elif valor > perfil["saldo"]:
                print("  Saldo insuficiente!")
            else:
                break
        except ValueError:
            print("  Digite um número válido.")

    print("\n  O dealer está tirando a carta", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    def sortear_carta():
        return random.randint(1, 10)

    jogador = sortear_carta() + sortear_carta()
    dealer  = sortear_carta() + sortear_carta()

    print(f"\n  Sua mão: {jogador}")
    print(f"  Carta visível do dealer: {dealer // 2}")

    while jogador < 21:
        acao = input("\n  Pedir carta (1) ou parar (0)? ").strip().lower()
        if acao == "1":
            print("\n  Tirando a carta", end="")
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            carta = sortear_carta()
            jogador += carta
            print(f"\n  Você recebeu {carta}. Total: {jogador}")
            if jogador > 21:
                print("  Passou de 21! Você perdeu!")
                break
        elif acao == "0":
            break
        else:
            print("  Digite (1) para pedir ou (0) para parar.")

    perfil["saldo"] -= valor

    print(f"\n  Mão do dealer: {dealer}")
    while dealer < 17:
        dealer += sortear_carta()
        print(f"  Dealer pediu carta. Total: {dealer}")
        time.sleep(0.5)

    if jogador > 21:
        print(f"  -R$ {valor:,.2f}")
        print("O baralho ainda está segurando seu prêmio!")
    elif dealer > 21:
        ganho = valor * 2
        perfil["saldo"] += ganho
        print(f"  Dealer passou de 21! VOCÊ GANHOU! +R$ {ganho:,.2f}")
        print("Acho que você está com a mão quente!")
    elif jogador > dealer:
        ganho = valor * 2
        perfil["saldo"] += ganho
        print(f"  VOCÊ GANHOU! +R$ {ganho:,.2f}")
        print("Acho que você está com a mão quente!")
    elif jogador == dealer:
        perfil["saldo"] += valor
        print(f"  Empate! Aposta devolvida.")
        print("Você está entrando no ritmo da vitória")
    else:
        print(f"  O Dealer venceu! -R$ {valor:,.2f}")
        print("O baralho ainda está segurando seu prêmio!")

    print(f"  Saldo atual: R$ {perfil['saldo']:,.2f}")
    print("Vamos continuar? Sinto que você está perto de algo grande.")
    time.sleep(1.0)

    print("\n  (1) Jogar novamente")
    print("  (2) Sair")
    while True:
        opcao = input("\n  Opção: ").strip()
        if opcao == "1":
            blackjack(perfil)
            break
        elif opcao == "2":
            print("\n  Te esperamos na próxima!")
            time.sleep(1.0)
            break
        else:
            print("  Opção inválida. Digite 1 ou 2.")


def loteria(perfil):
    print("\n                      🎟️ LOTERIA 🎟️")
    print("                 Escolha 3 números de 1 a 30.")
    print(" Se acertar os 3 números, o valor da aposta é multiplicado por 10")
    print(".       Se acertar 2 números, o valor da aposta é dobrado")
    print(".       Se acertar 1 número, a casa devolve seu dinheiro")

    while True:
        try:
            valor = float(input(f"\nSeu saldo é de R$ {perfil['saldo']:,.2f} \n Quanto você quer apostar parceiro? R$ "))
            if valor <= 0:
                print("  O valor deve ser maior que zero.")
            elif valor > perfil["saldo"]:
                print("  Saldo insuficiente!")
            else:
                break
        except ValueError:
            print("  Digite um número válido.")

    numeros_jogador = []
    print("\n  Digite seus 3 números, devem estar entre 1 e 30):")
    while len(numeros_jogador) < 3:
        try:
            n = int(input(f"  Número {len(numeros_jogador) + 1}: "))
            if n < 1 or n > 30:
                print("  Digite um número entre 1 e 30.")
            elif n in numeros_jogador:
                print("  Número já escolhido!")
            else:
                numeros_jogador.append(n)
        except ValueError:
            print("  Digite um número válido.")

    print("\n  Sorteando os números", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    sorteados = random.sample(range(1, 31), 3)
    acertos = len(set(numeros_jogador) & set(sorteados))

    print(f"\n  Números sorteados:")
    time.sleep(1)
    for numero in sorteados:
        time.sleep(1)
        print(f"  {numero}", flush=True)
    time.sleep(1)
    print(f"  Seus números: {numeros_jogador}")
    print(f"  Você teve {acertos} acertos")

    perfil["saldo"] -= valor

    if acertos == 3:
        ganho = valor * 10
        perfil["saldo"] += ganho
        print(f"\n  VOCÊ GANHOU! Acertou os 3 números! +R$ {ganho:,.2f}")
        print("Acho que você está com a mão quente!")
    elif acertos == 2:
        ganho = valor * 2
        perfil["saldo"] += ganho
        print(f"\n  DECOLANDO! Acertou 2 números! +R$ {ganho:,.2f}")
        print("Você está entrando no ritmo da vitória")
    elif acertos == 1:
        perfil["saldo"] += valor
        print(f"\n  Você acertou 1 número! Aposta devolvida.")
        print("Você está entrando no ritmo da vitória")
    else:
        print(f"\n  Nenhum número acertado! -R$ {valor:,.2f}")
        print("O prêmio escapou por pouco.")


    print(f"  Saldo atual: R$ {perfil['saldo']:,.2f}")
    print("Vamos continuar? Sinto que você está perto de algo grande.")
    time.sleep(1.0)

    print("\n  (1) Jogar novamente")
    print("  (2) Sair")
    while True:
        opcao = input("\n  Opção: ").strip()
        if opcao == "1":
            loteria(perfil)
            break
        elif opcao == "2":
            print("\n  Te esperamos na próxima!")
            time.sleep(1.0)
            break
        else:
            print("  Opção inválida. Digite 1 ou 2.")


def jogo_futebol(perfil):
    print("\n  ⚽️ APOSTA ESPORTIVA ⚽️")
    print("  Escolha o time que você acha que vai ganhar o Brasileirão:")
    print("  (1) Flamengo      — favorito  [40% de chance]")
    print("  (2) Palmeiras     — bom       [25% de chance]")
    print("  (3) São Paulo     — médio     [15% de chance]")
    print("  (4) Corinthians   — azarão    [12% de chance]")
    print("  (5) Remo          — sortudo   [8% de chance]")

    while True:
        try:
            valor = float(input(f"\nSeu saldo é de R$ {perfil['saldo']:,.2f} \n Quanto você quer apostar parceiro? R$ "))
            if valor <= 0:
                print("  O valor deve ser maior que zero.")
            elif valor > perfil["saldo"]:
                print("  Saldo insuficiente!")
            else:
                break
        except ValueError:
            print("  Digite um número válido.")

    while True:
        escolha = input("\n  Qual time você escolhe: ").strip()
        if escolha in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("  Digite um número de 1 a 5.")

    times = {
        "1": {"nome": "Flamengo", "chance": 40, "multiplicador": 2},
        "2": {"nome": "Palmeiras",    "chance": 25, "multiplicador": 3},
        "3": {"nome": "São Paulo",  "chance": 15, "multiplicador": 5},
        "4": {"nome": "Corinthians",    "chance": 12, "multiplicador": 7},
        "5": {"nome": "Remo",  "chance": 8,  "multiplicador": 10}
    }

    escolhido = times[escolha]
    times_lista = [t["nome"] for t in times.values()]
    perfil["saldo"] -= valor

    print(f"\n  Seu time escolhido foi o {escolhido['nome']}")
    print("  Começou o campeonato...")
    time.sleep(0.5)
    inicio_campeonato = random.choice(times_lista)
    print(f"O {inicio_campeonato} saiu na frente.")
    time.sleep(1.5)
    print("  Fim da primeira fase...")
    meio_campeonato = random.choice(times_lista)
    print(f"O {meio_campeonato} assume a liderança.")
    time.sleep(1.5)
    print("  Estamos chegando no final do campeonato...")
    fim_campeonato = random.choice(times_lista)
    print(f"{fim_campeonato} está cada vez mais perto do título.")
    time.sleep(2)
    

    vencedor = random.choices(
        list(times.values()),
        weights=[c["chance"] for c in times.values()],
        k=1
    )[0]

    print(f"  O {vencedor['nome']} é o campeão do Brasileirão 2026!")

    if escolhido["nome"] == vencedor["nome"]:
        ganho = valor * escolhido["multiplicador"]
        perfil["saldo"] += ganho
        print(f"\n  VOCÊ GANHOU! +R$ {ganho:,.2f} ({escolhido['multiplicador']}x)")
        print("Acho que você está com a mão quente!")

    else:
        print(f"\n  Você perdeu! -R$ {valor:,.2f}")
        print("Seu próximo resultado pode mudar tudo!")


    print(f"  Saldo atual: R$ {perfil['saldo']:,.2f}")
    print("Vamos continuar? Sinto que você está perto de algo grande.")
    time.sleep(1.0)

    print("\n  (1) Jogar novamente")
    print("  (2) Sair")
    while True:
        opcao = input("\n  Opção: ").strip()
        if opcao == "1":
            jogo_futebol(perfil)
            break
        elif opcao == "2":
            print("\n  Te esperamos na próxima!")
            time.sleep(1.0)
            break
        else:
            print("  Opção inválida. Digite 1 ou 2.")
