import datetime
import os
import time
import json

def exibir_relatorio_final(perfil):
    print("\n" + "=" * 50)
    print("         RELATÓRIO FINAL")
    print("=" * 50)
    print(f"  Jogador : {perfil['nome']}")
    print(f"  Classe  : {perfil['classe']}")
    print(f"  Meses jogados: {perfil['mes_atual']}")
    print("\n--- FINANCEIRO ---")
    print(f"  Saldo final  : R$ {perfil['saldo']:,.2f}")
    print(f"  Dívida final : R$ {perfil['divida_total']:,.2f}")
    print(f"  Salário      : R$ {perfil['salario']:,.2f}")

    print("\n--- INVESTIMENTOS ---")
    if not perfil["investimentos_ativos"]:
        print("  Nenhum investimento realizado.")
    else:
        for inv in perfil["investimentos_ativos"]:
            print(f"  {inv['tipo']}: R$ {inv['valor']:,.2f} a {inv['taxa']*100:.1f}% ao mês")

    print("\n--- METAS ---")
    if not perfil["metas"]:
        print("  Nenhuma meta cadastrada.")
    else:
        for meta in perfil["metas"]:
            progresso = min(meta["acumulado"] / meta["valor_alvo"] * 100, 100)
            print(f"  {meta['nome']}: R$ {meta['acumulado']:,.2f} / R$ {meta['valor_alvo']:,.2f} ({progresso:.1f}%)")

    print("\n--- HISTÓRICO ---")
    if not perfil["historico"]:
        print("  Nenhuma transação registrada.")
    else:
        for i, transacao in enumerate(perfil["historico"], 1):
            print(f"  {i}. [{transacao['mes']}] {transacao['tipo']} - R$ {transacao['valor']:,.2f}")

    print("=" * 50)
    time.sleep(2.0)


def salvar_relatorio_json(perfil):
    os.makedirs("relatorios", exist_ok=True)

    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%d-%m-%Y_%H-%M")
    nome_arquivo = f"relatorio_{perfil['nome']}_{data_formatada}.json"
    caminho = os.path.join("relatorios", nome_arquivo)

    dados_relatorio = {
        "data": {
            "gerado_em": agora.strftime('%d/%m/%Y %H:%M'),
            "versao_relatorio": "1.0"
        },
        "jogador": {
            "nome": perfil['nome'],
            "classe": perfil['classe'],
            "meses_jogados": perfil['mes_atual']
        },
        "financeiro": {
            "saldo_final": perfil['saldo'],
            "divida_final": perfil['divida_total'],
            "salario": perfil['salario']
        },
        "investimentos": perfil["investimentos_ativos"],
        "metas": perfil["metas"],
        "historico": perfil["historico"]
    }

    with open(caminho, "w", encoding="utf-8") as arquivo_json:
        json.dump(dados_relatorio, arquivo_json, ensure_ascii=False, indent=2)

    print(f"\n Relatório salvo em JSON: {caminho}")
    time.sleep(1.0)

