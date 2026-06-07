import time
from constantes import SALDO_MINIMO, META_INDEPENDENCIA, MESES_MAXIMOS, TAXA_JUROS_DIVIDA
from relatorio  import exibir_relatorio_final, salvar_relatorio_txt
from rich.console import Console
from rich.panel   import Panel
from rich.table   import Table

console = Console()


def exibir_status_mes(perfil):
    pct    = min(perfil["saldo"] / META_INDEPENDENCIA * 100, 100)
    blocos = int(pct / 5)
    barra  = f"[green]{'█' * blocos}[/][dim]{'░' * (20 - blocos)}[/] {pct:.1f}%"

    if perfil["saldo"] >= META_INDEPENDENCIA:
        situacao = "[bold green]INDEPENDÊNCIA FINANCEIRA![/]"
    elif perfil["saldo"] >= 10000:
        situacao = "[green]Saudável[/]"
    elif perfil["saldo"] >= 0:
        situacao = "[yellow]Equilibrada[/]"
    elif perfil["saldo"] >= SALDO_MINIMO:
        situacao = "[red bold]Em risco![/]"
    else:
        situacao = "[red bold]FALÊNCIA![/]"

    stats = Table(show_header=False, box=None, padding=(0, 2))
    stats.add_column(style="dim")
    stats.add_column()
    stats.add_row("Jogador",  f"[bold]{perfil['nome']}[/] [dim]({perfil['classe']})[/]")
    stats.add_row("Saldo",    f"[green bold]R$ {perfil['saldo']:,.2f}[/]")
    stats.add_row("Salário",  f"[green]R$ {perfil['salario']:,.2f}[/]")
    stats.add_row("Dívida",   f"[red bold]R$ {perfil['divida_total']:,.2f}[/]")
    stats.add_row("Meta",     barra)
    stats.add_row("Situação", situacao)

    console.print(Panel(
        stats,
        title=f"[bold yellow]📅 MÊS {perfil['mes_atual']} DE {MESES_MAXIMOS}[/]",
        border_style="yellow"
    ))
    time.sleep(1.0)


def processar_fim_de_mes(perfil):
    console.print(Panel("[dim]Processando fim de mês...[/]", border_style="dim"))
    time.sleep(1.0)

    linhas = []

    # Salário
    perfil["saldo"] += perfil["salario"]
    linhas.append(
        f"[green]+ Salário recebido:[/]    [green bold]R$ {perfil['salario']:,.2f}[/]"
    )

    # Despesas fixas
    despesas_fixas = (
        perfil["aluguel"] +
        perfil["luz_agua_net"] +
        perfil["alimentacao"] +
        perfil["transporte"]
    )
    perfil["saldo"] -= despesas_fixas
    linhas.append(
        f"[red]- Despesas fixas:[/]      [red bold]R$ {despesas_fixas:,.2f}[/]"
    )

    # Rendimentos de investimentos
    total_rendimentos = 0.0
    for inv in perfil["investimentos_ativos"]:
        rendimento = inv["valor"] * inv["taxa"]
        inv["valor"] += rendimento
        total_rendimentos += rendimento
    perfil["saldo"] += total_rendimentos
    if total_rendimentos > 0:
        linhas.append(
            f"[green]+ Rendimentos:[/]         [green bold]R$ {total_rendimentos:,.2f}[/]"
        )

    # Contribuição das metas
    total_metas = 0.0
    for meta in perfil["metas"]:
        if meta["acumulado"] < meta["valor_alvo"]:
            perfil["saldo"] -= meta["contribuicao_mensal"]
            meta["acumulado"] += meta["contribuicao_mensal"]
            total_metas += meta["contribuicao_mensal"]
    if total_metas > 0:
        linhas.append(
            f"[red]- Contribuição metas:[/]  [red bold]R$ {total_metas:,.2f}[/]"
        )

    # Juros da dívida
    if perfil["divida_total"] > 0:
        juros = perfil["divida_total"] * TAXA_JUROS_DIVIDA
        perfil["divida_total"] += juros
        linhas.append(
            f"[red]- Juros da dívida:[/]     [red bold]R$ {juros:,.2f}[/]"
        )

    perfil["mes_atual"] += 1

    cor = "green" if perfil["saldo"] >= 0 else "red"
    linhas.append(f"\nSaldo final do mês: [{cor} bold]R$ {perfil['saldo']:,.2f}[/]")

    console.print(Panel("\n".join(linhas), title="[bold blue]📋 RESUMO DO MÊS[/]", border_style="blue"))
    time.sleep(1.5)


def verificar_condicoes_fim(perfil):
    if perfil["saldo"] < SALDO_MINIMO:
        console.print(Panel(
            f"[red bold]Seu saldo chegou a R$ {perfil['saldo']:,.2f}[/]\n"
            f"O limite era R$ {SALDO_MINIMO:,.2f}.\n"
            f"[dim]Você foi à falência.[/]",
            title="[bold red]💀 FALÊNCIA![/]",
            border_style="red"
        ))
        time.sleep(2.0)
        return False

    if perfil["saldo"] >= META_INDEPENDENCIA:
        console.print(Panel(
            f"[green bold]Você atingiu R$ {perfil['saldo']:,.2f}![/]\n"
            f"A meta era R$ {META_INDEPENDENCIA:,.2f}.\n"
            f"[dim]Parabéns, você conquistou sua independência financeira![/]",
            title="[bold green]🏆 INDEPENDÊNCIA FINANCEIRA![/]",
            border_style="green"
        ))
        time.sleep(2.0)
        return False

    if perfil["mes_atual"] > MESES_MAXIMOS:
        console.print(Panel(
            f"[yellow]Você chegou ao mês {MESES_MAXIMOS} sem atingir a meta.[/]\n"
            f"Saldo final: [bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[bold yellow]⏰ TEMPO ESGOTADO![/]",
            border_style="yellow"
        ))
        time.sleep(2.0)
        return False

    return True


def encerrar_jogo(perfil):
    console.print(Panel(
        f"[bold]Obrigado por jogar, [yellow]{perfil['nome']}[/]![/]",
        title="[bold]🎮 FIM DE JOGO[/]",
        border_style="dim"
    ))
    time.sleep(1.5)
    exibir_relatorio_final(perfil)
    salvar_relatorio_txt(perfil)
    console.print("[green]✅ Relatório salvo com sucesso![/]")
    console.print("[dim]Até a próxima![/]")
    time.sleep(1.0)
