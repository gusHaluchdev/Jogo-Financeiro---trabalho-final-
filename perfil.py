import time
from rich.console import Console
from rich.panel   import Panel
from rich.table   import Table
from rich.prompt  import Prompt

console = Console()

CLASSES = {
    "1": {
        "nome_classe": "Estagiário de TI",
        "salario": 1000.0,
        "divida": 5000.0,
        "saldo_inicial": 200.0,
        "dificuldade": "Difícil",
        "acoes_por_mes": 2,
        "freelance_min": 50.0,
        "freelance_max": 300.0,
        "aluguel": 600.0,
        "luz_agua_net": 200.0,
        "alimentacao": 400.0,
        "transporte": 150.0,
        "pagamento_minimo_divida": 350.0,
    },
    "2": {
        "nome_classe": "Repositor do Atacadão",
        "salario": 2000.0,
        "divida": 5000.0,
        "saldo_inicial": 800.0,
        "dificuldade": "Normal",
        "acoes_por_mes": 3,
        "freelance_min": 50.0,
        "freelance_max": 500.0,
        "aluguel": 800.0,
        "luz_agua_net": 250.0,
        "alimentacao": 500.0,
        "transporte": 200.0,
        "pagamento_minimo_divida": 550.0,
    },
    "3": {
        "nome_classe": "Médico",
        "salario": 7000.0,
        "divida": 10000.0,
        "saldo_inicial": 1500.0,
        "dificuldade": "Fácil",
        "acoes_por_mes": 4,
        "freelance_min": 200.0,
        "freelance_max": 1000.0,
        "aluguel": 2000.0,
        "luz_agua_net": 400.0,
        "alimentacao": 800.0,
        "transporte": 300.0,
        "pagamento_minimo_divida": 1200.0,
    },
}

_COR_DIF = {"Difícil": "red", "Normal": "yellow", "Fácil": "green"}


def exibir_introducao():
    console.print(Panel(
        "Nesse jogo você assume o papel de uma pessoa comum que precisa\n"
        "organizar sua vida financeira ao longo dos meses.\n\n"
        "[yellow bold]Objetivo:[/] atingir [green bold]R$ 50.000,00[/] em [blue bold]24 meses[/]\n"
        "sem entrar em falência (saldo abaixo de [red bold]R$ -5.000,00[/]).\n\n"
        "A cada mês você poderá:\n"
        "[green]·[/] Adicionar receitas        [green]·[/] Registrar despesas\n"
        "[green]·[/] Investir dinheiro         [green]·[/] Pagar dívidas\n"
        "[green]·[/] Criar e acompanhar metas\n\n"
        "[dim]Eventos aleatórios podem ocorrer ao longo da jogatina\n"
        "podendo ajudar ou prejudicar. Tome boas decisões![/]",
        title="[bold yellow]💰 BEM-VINDO AO SISTEMA FINANCEIRO[/]",
        border_style="yellow"
    ))
    console.input("[dim]Pressione Enter para continuar...[/]")
    time.sleep(0.5)


def configurar_perfil():
    console.print(Panel("", title="[bold yellow]⚙️  CONFIGURAR PERFIL[/]", border_style="yellow"))

    nome = Prompt.ask("[bold]Qual o seu nome, parceiro?[/]")
    while not nome.strip():
        console.print("[red]Nome não pode ser vazio![/]")
        nome = Prompt.ask("[bold]Qual o seu nome, parceiro?[/]")

    console.print(f"\n[bold]Olá, [yellow]{nome}[/]! Agora escolha sua classe:[/]\n")


    tabela = Table(title="Classes Disponíveis", show_lines=True)
    tabela.add_column("#",             style="bold", width=3)
    tabela.add_column("Classe",        style="bold")
    tabela.add_column("Dificuldade",   justify="center")
    tabela.add_column("Salário",       justify="right", style="green")
    tabela.add_column("Dívida",        justify="right", style="red")
    tabela.add_column("Saldo Inicial", justify="right", style="yellow")

    for id_, c in CLASSES.items():
        cor = _COR_DIF.get(c["dificuldade"], "white")
        tabela.add_row(
            id_,
            c["nome_classe"],
            f"[{cor}]{c['dificuldade']}[/]",
            f"R$ {c['salario']:,.2f}",
            f"R$ {c['divida']:,.2f}",
            f"R$ {c['saldo_inicial']:,.2f}",
        )
    console.print(tabela)

    escolha        = Prompt.ask("[bold]Classe escolhida[/]", choices=list(CLASSES.keys()))
    classe_escolhida = CLASSES[escolha]

    perfil = {
        "nome":                    nome,
        "classe":                  classe_escolhida["nome_classe"],
        "acoes_por_mes":           classe_escolhida["acoes_por_mes"],
        "saldo":                   classe_escolhida["saldo_inicial"],
        "salario":                 classe_escolhida["salario"],
        "divida_total":            classe_escolhida["divida"],
        "mes_atual":               1,
        "freelance_min":           classe_escolhida["freelance_min"],
        "freelance_max":           classe_escolhida["freelance_max"],
        "aluguel":                 classe_escolhida["aluguel"],
        "luz_agua_net":            classe_escolhida["luz_agua_net"],
        "alimentacao":             classe_escolhida["alimentacao"],
        "transporte":              classe_escolhida["transporte"],
        "investimentos_ativos":    [],
        "pagamento_minimo_divida": classe_escolhida["pagamento_minimo_divida"],
        "metas":                   [],
        "max_metas":               3,
        "historico":               [],
    }

    cor_dif = _COR_DIF.get(classe_escolhida["dificuldade"], "white")
    console.print(Panel(
        f"Nome:        [bold yellow]{nome}[/]\n"
        f"Classe:      [bold]{classe_escolhida['nome_classe']}[/]\n"
        f"Dificuldade: [{cor_dif} bold]{classe_escolhida['dificuldade']}[/]\n"
        f"Saldo:       [green bold]R$ {perfil['saldo']:,.2f}[/]\n"
        f"Salário:     [green bold]R$ {perfil['salario']:,.2f}[/]\n"
        f"Dívida:      [red bold]R$ {perfil['divida_total']:,.2f}[/]",
        title="[bold green]✅ Perfil Criado![/]",
        border_style="green"
    ))

    time.sleep(1.5)
    return perfil
