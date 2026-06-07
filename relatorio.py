import datetime
import os
import time
from rich.console import Console
from rich.panel   import Panel
from rich.table   import Table

console = Console()


def exibir_relatorio_final(perfil):
   
    console.print(Panel(
        f"[bold]Jogador:[/]      [yellow]{perfil['nome']}[/]\n"
        f"[bold]Classe:[/]       {perfil['classe']}\n"
        f"[bold]Meses jogados:[/] {perfil['mes_atual']}",
        title="[bold yellow]📊 RELATÓRIO FINAL[/]",
        border_style="yellow"
    ))

    
    fin = Table(show_header=False, box=None, padding=(0, 2))
    fin.add_column(style="dim")
    fin.add_column(justify="right")
    cor_saldo = "green" if perfil["saldo"] >= 0 else "red"
    fin.add_row("Saldo final",  f"[{cor_saldo} bold]R$ {perfil['saldo']:,.2f}[/]")
    fin.add_row("Dívida final", f"[red]R$ {perfil['divida_total']:,.2f}[/]")
    fin.add_row("Salário",      f"[green]R$ {perfil['salario']:,.2f}[/]")
    console.print(Panel(fin, title="[bold green]💰 Financeiro[/]", border_style="green"))

   
    if not perfil["investimentos_ativos"]:
        inv_txt = "[dim]Nenhum investimento realizado.[/]"
    else:
        linhas = [
            f"[blue]{inv['tipo']}:[/]  R$ {inv['valor']:,.2f}  a  {inv['taxa']*100:.1f}%/mês"
            for inv in perfil["investimentos_ativos"]
        ]
        inv_txt = "\n".join(linhas)
    console.print(Panel(inv_txt, title="[bold blue]📈 Investimentos[/]", border_style="blue"))

    
    if not perfil["metas"]:
        metas_txt = "[dim]Nenhuma meta cadastrada.[/]"
    else:
        partes = []
        for meta in perfil["metas"]:
            pct    = min(meta["acumulado"] / meta["valor_alvo"] * 100, 100)
            blocos = int(pct / 5)
            barra  = f"[green]{'█' * blocos}[/][dim]{'░' * (20 - blocos)}[/]"
            partes.append(
                f"[magenta bold]{meta['nome']}[/]  {barra}  {pct:.1f}%\n"
                f"  [dim]R$ {meta['acumulado']:,.2f} / R$ {meta['valor_alvo']:,.2f}[/]"
            )
        metas_txt = "\n".join(partes)
    console.print(Panel(metas_txt, title="[bold magenta]🎯 Metas[/]", border_style="magenta"))

    if not perfil["historico"]:
        hist_txt = "[dim]Nenhuma transação registrada.[/]"
    else:
        hist_txt = "\n".join(
            f"[dim]{i}.[/] [yellow][Mês {t['mes']}][/] [bold]{t['tipo']}[/]  "
            f"[green]R$ {t['valor']:,.2f}[/]"
            for i, t in enumerate(perfil["historico"], 1)
        )
    console.print(Panel(hist_txt, title="[bold]📋 Histórico[/]", border_style="dim"))

    time.sleep(2.0)


def salvar_relatorio_txt(perfil):

    os.makedirs("relatorios", exist_ok=True)

    agora        = datetime.datetime.now()
    nome_arquivo = f"relatorio_{perfil['nome']}_{agora.strftime('%d-%m-%Y_%H-%M')}.txt"
    caminho      = os.path.join("relatorios", nome_arquivo)

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
                f.write(
                    f"{meta['nome']}: R$ {meta['acumulado']:,.2f} / "
                    f"R$ {meta['valor_alvo']:,.2f} ({pct:.1f}%)\n"
                )

        f.write("\n--- HISTÓRICO ---\n")
        if not perfil["historico"]:
            f.write("Nenhuma transação registrada.\n")
        else:
            for i, t in enumerate(perfil["historico"], 1):
                f.write(f"{i}. [Mês {t['mes']}] {t['tipo']} - R$ {t['valor']:,.2f}\n")

        f.write("=" * 50 + "\n")
        f.write(f"Gerado em: {agora.strftime('%d/%m/%Y %H:%M')}\n")

    console.print(f"[dim]Relatório salvo em: {caminho}[/]")
    time.sleep(1.0)
