from constantes import SALDO_MINIMO, META_INDEPENDENCIA, MESES_MAXIMOS, TAXA_JUROS_DIVIDA
from relatorio import exibir_relatorio_final, salvar_relatorio_json
import time

def validar_entrada_numerica(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"  Valor mínimo permitido: {minimo:,.2f}")
            elif maximo is not None and valor > maximo:
                print(f"  Valor máximo permitido: {maximo:,.2f}")
            else:
                return valor
        except ValueError:
            print("  Digite um número válido.")

def exibir_status_mes(perfil):
    print("\n" + "=" * 50)
    print(f"  MÊS {perfil['mes_atual']} DE {MESES_MAXIMOS}")
    print("=" * 50)
    print(f"  Jogador : {perfil['nome']} ({perfil['classe']})")
    print(f"  Saldo   : R$ {perfil['saldo']:,.2f}")
    print(f"  Salário : R$ {perfil['salario']:,.2f}")
    print(f"  Dívida  : R$ {perfil['divida_total']:,.2f}")

    progresso = min(perfil['saldo'] / META_INDEPENDENCIA * 100, 100)
    blocos = int(progresso / 5)
    barra = "█" * blocos + "░" * (20 - blocos)
    print(f"\n  Meta: [{barra}] {progresso:.1f}%")

    if perfil['saldo'] >= META_INDEPENDENCIA:
        print("Situação: INDEPENDÊNCIA FINANCEIRA!")
    elif perfil['saldo'] >= 10000:
        print("Situação: Saudável")
    elif perfil['saldo'] >= 0:
        print("Situação: Equilibrada!")
    elif perfil['saldo'] >= SALDO_MINIMO:
        print("Situação: Em risco!")
    else:
        print("Situação: FALÊNCIA!")

    print("=" * 50)
    time.sleep(1.0)

def processar_fim_de_mes(perfil):
    print("\n  Processando fim de mês...")
    time.sleep(1.0)

    perfil["saldo"] += perfil["salario"]
    print(f"  + Salário recebido:     R$ {perfil['salario']:,.2f}")

    despesas_fixas = (
        perfil["aluguel"] +
        perfil["luz_agua_net"] +
        perfil["alimentacao"] +
        perfil["transporte"]
    )
    perfil["saldo"] -= despesas_fixas
    print(f"  - Despesas fixas:       R$ {despesas_fixas:,.2f}")

    total_rendimentos = 0.0
    for investimento in perfil["investimentos_ativos"]:
        rendimento = investimento["valor"] * investimento["taxa"]
        investimento["valor"] += rendimento
        total_rendimentos += rendimento

    perfil["saldo"] += total_rendimentos
    print(f"  + Rendimentos: R$ {total_rendimentos:,.2f}")

    total_metas = 0.0
    for meta in perfil["metas"]:
        if meta["acumulado"] < meta["valor_alvo"]:
            perfil["saldo"] -= meta["contribuicao_mensal"]
            meta["acumulado"] += meta["contribuicao_mensal"]
            total_metas += meta["contribuicao_mensal"]

    if total_metas > 0:
        print(f"  - Contribuição metas:   R$ {total_metas:,.2f}")

    if perfil["divida_total"] > 0:
        juros = perfil["divida_total"] * TAXA_JUROS_DIVIDA
        perfil["divida_total"] += juros
        print(f"  - Juros da dívida:      R$ {juros:,.2f}")

    perfil["mes_atual"] += 1

    print(f"\n  Saldo final do mês: R$ {perfil['saldo']:,.2f}")
    print("=" * 50)
    time.sleep(1.5)

def verificar_condicoes_fim(perfil):
    if perfil["saldo"] < SALDO_MINIMO:
        print("\n" + "=" * 50)
        print("FALÊNCIA!")
        print("VOCÊ PERDEU!")
        print(f"  Seu saldo chegou a R$ {perfil['saldo']:,.2f}")
        print(f"  O limite era R$ {SALDO_MINIMO:,.2f}")
        print("=" * 50)
        time.sleep(2.0)
        return False

    if perfil["saldo"] >= META_INDEPENDENCIA:
        print("\n" + "=" * 50)
        print("PARABÉNS! VOCÊ GANHOU!")
        print("INDEPENDÊNCIA FINANCEIRA ATINGIDA!")
        print(f"  Você atingiu R$ {perfil['saldo']:,.2f}")
        print(f"  Meta era R$ {META_INDEPENDENCIA:,.2f}")
        print("=" * 50)
        time.sleep(2.0)
        return False

    if perfil["mes_atual"] > MESES_MAXIMOS:
        print("\n" + "=" * 50)
        print("TEMPO ESGOTADO!")
        print("VOCÊ PERDEU!")
        print(f"  Você chegou ao mês {MESES_MAXIMOS} sem atingir a meta.")
        print(f"  Saldo final: R$ {perfil['saldo']:,.2f}")
        print("=" * 50)
        time.sleep(2.0)
        return False

    return True

def encerrar_jogo(perfil):
    print("\n" + "=" * 50)
    print("  FIM DE JOGO")
    print(f"  Obrigado por jogar, {perfil['nome']}!")
    print("=" * 50)
    time.sleep(1.5)

    exibir_relatorio_final(perfil)
    salvar_relatorio_json(perfil)

    print("\n  Relatório salvo com sucesso!")
    print("  Até a próxima!")
    time.sleep(1.0)
