import time
import apostas
from rich.console import Console
from rich.panel   import Panel
from rich.table   import Table
from rich.prompt  import Prompt, FloatPrompt

console = Console()


def menu_acoes(perfil):
    acoes_disponiveis = perfil["acoes_por_mes"]
    acoes_usadas = 0

    while acoes_usadas < acoes_disponiveis:
        restantes = acoes_disponiveis - acoes_usadas

        stats = Table(show_header=False, box=None, padding=(0, 3))
        stats.add_column(style="dim")
        stats.add_column(justify="right")
        stats.add_row("Mês",    f"[yellow bold]{perfil['mes_atual']}[/]")
        stats.add_row("Saldo",  f"[green bold]R$ {perfil['saldo']:,.2f}[/]")
        stats.add_row("Dívida", f"[red bold]R$ {perfil['divida_total']:,.2f}[/]")
        stats.add_row("Ações",  f"[blue bold]{restantes} restantes[/]")
        console.print(stats)

      
        menu = (
            "[green bold](1)[/] Adicionar receita\n"
            "[red bold](2)[/] Registrar despesa\n"
            "[blue bold](3)[/] Realizar investimento\n"
            "[yellow bold](4)[/] Pagar dívida\n"
            "[magenta bold](5)[/] Gerenciar metas\n"
            "[dim bold](6)[/] Ver histórico\n"
            "[gold1 bold](7)[/] Casa de apostas"
        )
        console.print(Panel(
            menu,
            title=f"[bold yellow]AÇÕES DO MÊS {perfil['mes_atual']}[/]",
            subtitle=f"[dim]{restantes} ação(ões) restante(s)[/]"
        ))

        escolha = Prompt.ask("[bold]Escolha uma ação[/]",
                             choices=["1","2","3","4","5","6","7"])

        if escolha == "1":
            adicionar_receita(perfil)
        elif escolha == "2":
            registrar_despesa(perfil)
        elif escolha == "3":
            realizar_investimento(perfil)
        elif escolha == "4":
            pagar_divida(perfil)
        elif escolha == "5":
            gerenciar_metas(perfil)
        elif escolha == "6":
            ver_historico(perfil)
        elif escolha == "7":
            apostas.casa_de_apostas(perfil)

        acoes_usadas += 1

    console.print(Panel("[bold yellow]Você usou todas as ações desse mês![/]",
                        border_style="yellow"))
    time.sleep(1.0)


def adicionar_receita(perfil):
    console.print(Panel(
        f"Faixa para [bold]{perfil['classe']}[/]: "
        f"[green]R$ {perfil['freelance_min']:,.2f}[/] até "
        f"[green]R$ {perfil['freelance_max']:,.2f}[/]",
        title="[bold green]💵 FREELANCE[/]"
    ))

    while True:
        valor = FloatPrompt.ask("[bold]Valor do freelance[/] (R$)")
        if valor < perfil["freelance_min"]:
            console.print(f"[red]Valor mínimo é R$ {perfil['freelance_min']:,.2f}[/]")
        elif valor > perfil["freelance_max"]:
            console.print(f"[red]Valor máximo é R$ {perfil['freelance_max']:,.2f}[/]")
        else:
            break

    perfil["saldo"] += valor
    console.print(Panel(
        f"[green bold]+ R$ {valor:,.2f}[/] adicionado!\n"
        f"Saldo atual: [green bold]R$ {perfil['saldo']:,.2f}[/]",
        title="[green]Freelance Registrado[/]",
        border_style="green"
    ))
    time.sleep(1.0)


def registrar_despesa(perfil):
    console.print(Panel(
        "[bold](1)[/] Lazer\n"
        "[bold](2)[/] Saúde\n"
        "[bold](3)[/] Outros",
        title="[bold red]💸 REGISTRAR DESPESA[/]"
    ))

    nomes     = {"1": "Lazer", "2": "Saúde", "3": "Outros"}
    categoria = Prompt.ask("[bold]Categoria[/]", choices=["1","2","3"])
    nome_cat  = nomes[categoria]

    while True:
        valor = FloatPrompt.ask(f"[bold]Valor gasto em {nome_cat}[/] (R$)")
        if valor <= 0:
            console.print("[red]O valor deve ser maior que zero[/]")
        else:
            break

    perfil["saldo"] -= valor
    cor = "green" if perfil["saldo"] >= 0 else "red"
    console.print(Panel(
        f"[red bold]- R$ {valor:,.2f}[/] em {nome_cat}\n"
        f"Saldo atual: [{cor} bold]R$ {perfil['saldo']:,.2f}[/]",
        title="[red]Despesa Registrada[/]",
        border_style="red"
    ))
    time.sleep(1.0)


def realizar_investimento(perfil):
    console.print(Panel(
        "[green bold](1)[/] Poupança  —  0.5%/mês  [dim][baixo risco][/]\n"
        "[green bold](2)[/] Tesouro   —  0.9%/mês  [dim][baixo risco][/]\n"
        "[yellow bold](3)[/] Ações     —  3.0%/mês  [dim][médio risco][/]\n"
        "[red bold](4)[/] Cripto    —  8.0%/mês  [dim][alto risco][/]\n"
        "[dim](5)[/] Voltar",
        title="[bold blue]📈 INVESTIMENTO[/]"
    ))

    escolha = Prompt.ask("[bold]Opção[/]", choices=["1","2","3","4","5"])

    if escolha == "5":
        console.print("[dim]Voltando para o menu...[/]")
        return

    tipos = {
        "1": {"tipo": "Poupança", "taxa": 0.005},
        "2": {"tipo": "Tesouro",  "taxa": 0.009},
        "3": {"tipo": "Ações",    "taxa": 0.030},
        "4": {"tipo": "Cripto",   "taxa": 0.080},
    }
    inv = tipos[escolha]

    while True:
        valor = FloatPrompt.ask(
            f"[bold]Quanto investir em {inv['tipo']}[/] "
            f"(saldo: [green]R$ {perfil['saldo']:,.2f}[/]) (R$)"
        )
        if valor <= 0:
            console.print("[red]O valor deve ser maior que zero[/]")
        elif valor > perfil["saldo"]:
            console.print(f"[red]Saldo insuficiente! Disponível: R$ {perfil['saldo']:,.2f}[/]")
        else:
            break

    perfil["saldo"] -= valor
    perfil["investimentos_ativos"].append({
        "tipo": inv["tipo"], "taxa": inv["taxa"], "valor": valor
    })

    console.print(Panel(
        f"Tipo: [blue bold]{inv['tipo']}[/]\n"
        f"Investido: [blue bold]R$ {valor:,.2f}[/]\n"
        f"Rendimento estimado: [green bold]R$ {valor * inv['taxa']:,.2f}[/]/mês\n"
        f"Saldo atual: [green bold]R$ {perfil['saldo']:,.2f}[/]",
        title="[blue]Investimento Registrado[/]",
        border_style="blue"
    ))
    time.sleep(1.0)


def pagar_divida(perfil):
    if perfil["divida_total"] <= 0:
        console.print(Panel("[bold green]Parabéns! Você não tem dívidas![/]",
                            border_style="green"))
        return

    info = Table(show_header=False, box=None, padding=(0, 3))
    info.add_column(style="dim")
    info.add_column(justify="right")
    info.add_row("Dívida total",  f"[red bold]R$ {perfil['divida_total']:,.2f}[/]")
    info.add_row("Pag. mínimo",   f"[yellow bold]R$ {perfil['pagamento_minimo_divida']:,.2f}[/]")
    info.add_row("Saldo atual",   f"[green bold]R$ {perfil['saldo']:,.2f}[/]")
    console.print(Panel(info, title="[bold yellow]💳 PAGAR DÍVIDA[/]"))

    while True:
        valor = FloatPrompt.ask("[bold]Quanto deseja pagar[/] (0 para voltar) (R$)")
        if valor == 0:
            console.print("[dim]Voltando para o menu...[/]")
            return
        elif valor < 0:
            console.print("[red]O valor deve ser maior que zero[/]")
        elif valor < perfil["pagamento_minimo_divida"]:
            console.print(f"[red]Mínimo: R$ {perfil['pagamento_minimo_divida']:,.2f}[/]")
        elif valor > perfil["saldo"]:
            console.print("[red]Saldo insuficiente![/]")
        else:
            break

    perfil["saldo"]        -= valor
    perfil["divida_total"]  = max(0.0, perfil["divida_total"] - valor)

    resultado = (
        f"Pagamento: [green bold]R$ {valor:,.2f}[/]\n"
        f"Dívida restante: [red bold]R$ {perfil['divida_total']:,.2f}[/]\n"
        f"Saldo atual: [green bold]R$ {perfil['saldo']:,.2f}[/]"
    )
    if perfil["divida_total"] <= 0:
        resultado += "\n[bold green]🎉 Parabéns! Todas as dívidas foram pagas![/]"

    console.print(Panel(resultado, title="[green]Pagamento Registrado[/]",
                        border_style="green"))
    time.sleep(1.0)


def gerenciar_metas(perfil):
    if not perfil["metas"]:
        console.print("[dim]Você não tem metas cadastradas[/]")
    else:
        tabela = Table(title="Suas Metas", show_lines=True)
        tabela.add_column("Meta",      style="magenta bold")
        tabela.add_column("Alvo",      justify="right")
        tabela.add_column("Acumulado", justify="right", style="green")
        tabela.add_column("Mensal",    justify="right")
        tabela.add_column("Progresso")

        for meta in perfil["metas"]:
            pct    = min(meta["acumulado"] / meta["valor_alvo"] * 100, 100)
            blocos = int(pct / 5)
            barra  = f"[green]{'█' * blocos}[/][dim]{'░' * (20 - blocos)}[/] {pct:.1f}%"
            tabela.add_row(
                meta["nome"],
                f"R$ {meta['valor_alvo']:,.2f}",
                f"R$ {meta['acumulado']:,.2f}",
                f"R$ {meta['contribuicao_mensal']:,.2f}",
                barra
            )
        console.print(tabela)

    console.print(Panel(
        "[green bold](1)[/] Criar nova meta\n"
        "[red bold](2)[/] Excluir meta\n"
        "[dim bold](3)[/] Voltar",
        title="[bold magenta]🎯 METAS[/]"
    ))

    opcao = Prompt.ask("[bold]Opção[/]", choices=["1","2","3"])

    if opcao == "3":
        return

    if opcao == "1":
        if len(perfil["metas"]) >= perfil["max_metas"]:
            console.print(f"[red]Limite de {perfil['max_metas']} metas atingido.[/]")
            time.sleep(1.0)
            return

        nome = Prompt.ask("[bold]Nome da meta[/]")
        while not nome.strip():
            console.print("[red]Nome não pode ser vazio[/]")
            nome = Prompt.ask("[bold]Nome da meta[/]")

        while True:
            valor_alvo = FloatPrompt.ask("[bold]Valor alvo[/] (R$)")
            if valor_alvo <= 0:
                console.print("[red]O valor deve ser maior que zero[/]")
            else:
                break

        while True:
            contribuicao = FloatPrompt.ask("[bold]Contribuição mensal[/] (R$)")
            if contribuicao <= 0:
                console.print("[red]A contribuição deve ser maior que zero[/]")
            else:
                break

        perfil["metas"].append({
            "nome": nome, "valor_alvo": valor_alvo,
            "acumulado": 0.0, "contribuicao_mensal": contribuicao
        })
        console.print(Panel(
            f"[green bold]Meta '[magenta]{nome}[/]' cadastrada com sucesso![/]",
            border_style="green"
        ))
        time.sleep(1.0)

    elif opcao == "2":
        if not perfil["metas"]:
            console.print("[dim]Você não tem metas cadastradas[/]")
            return

        for i, meta in enumerate(perfil["metas"], 1):
            console.print(f"[magenta bold]({i})[/] {meta['nome']}  "
                          f"[dim]alvo: R$ {meta['valor_alvo']:,.2f}[/]")

        while True:
            try:
                idx = int(Prompt.ask("[bold]Número da meta para excluir[/]"))
                if 1 <= idx <= len(perfil["metas"]):
                    break
                console.print(f"[red]Digite entre 1 e {len(perfil['metas'])}[/]")
            except ValueError:
                console.print("[red]Digite um número válido[/]")

        nome_exc = perfil["metas"][idx - 1]["nome"]
        perfil["metas"].pop(idx - 1)
        console.print(Panel(
            f"[green]Meta '[magenta]{nome_exc}[/]' excluída com sucesso![/]",
            border_style="green"
        ))
        time.sleep(1.0)


def ver_historico(perfil):
    if not perfil["historico"]:
        console.print(Panel("[dim]Nenhuma transação registrada[/]",
                            title="[bold]📋 HISTÓRICO[/]"))
        time.sleep(1.0)
        return

    tabela = Table(title="Histórico de Transações", show_lines=True)
    tabela.add_column("#",         style="dim",      width=4)
    tabela.add_column("Mês",       justify="center", style="yellow bold")
    tabela.add_column("Tipo",      style="bold")
    tabela.add_column("Descrição", style="dim")
    tabela.add_column("Valor",     justify="right")

    for i, t in enumerate(perfil["historico"], 1):
        tabela.add_row(
            str(i),
            str(t["mes"]),
            t["tipo"],
            t["descricao"],
            f"[green]R$ {t['valor']:,.2f}[/]"
        )

    console.print(tabela)
    time.sleep(1.0)
