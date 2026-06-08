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

    print(f"\n Relatório Json salvo em: {caminho}")

def salvar_relatorio_txt(perfil):
    os.makedirs("relatorios", exist_ok=True)

    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%d-%m-%Y_%H-%M")
    nome_arquivo = f"relatorio_{perfil['nome']}_{data_formatada}.txt"
    caminho = os.path.join("relatorios", nome_arquivo)

    with open(caminho, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("         RELATÓRIO FINAL\n")
        f.write("=" * 50 + "\n")
        f.write(f"Jogador      : {perfil['nome']}\n")
        f.write(f"Classe       : {perfil['classe']}\n")
        f.write(f"Meses jogados: {perfil['mes_atual']}\n")

        f.write("\n--- FINANCEIRO ---\n")
        f.write(f"Saldo final  : R$ {perfil['saldo']:,.2f}\n")
        f.write(f"Dívida final : R$ {perfil['divida_total']:,.2f}\n")
        f.write(f"Salário      : R$ {perfil['salario']:,.2f}\n")

        f.write("\n--- INVESTIMENTOS ---\n")
        if not perfil["investimentos_ativos"]:
            f.write("Nenhum investimento realizado.\n")
        else:
            for inv in perfil["investimentos_ativos"]:
                f.write(f"{inv['tipo']}: R$ {inv['valor']:,.2f} a {inv['taxa']*100:.1f}% ao mês\n")

        f.write("\n--- METAS ---\n")
        if not perfil["metas"]:
            f.write("Nenhuma meta cadastrada.\n")
        else:
            for meta in perfil["metas"]:
                pct = min(meta["acumulado"] / meta["valor_alvo"] * 100, 100)
                f.write(f"{meta['nome']}: R$ {meta['acumulado']:,.2f} / R$ {meta['valor_alvo']:,.2f} ({pct:.1f}%)\n")

        f.write("\n--- HISTÓRICO ---\n")
        if not perfil["historico"]:
            f.write("Nenhuma transação registrada.\n")
        else:
            for i, t in enumerate(perfil["historico"], 1):
                f.write(f"{i}. [Mês {t['mes']}] {t['tipo']} - R$ {t['valor']:,.2f}\n")

        f.write("=" * 50 + "\n")
        f.write(f"Gerado em: {agora.strftime('%d/%m/%Y %H:%M')}\n")

    print(f"\n Relatório TXT salvo em: {caminho}")
    time.sleep(1.0)

