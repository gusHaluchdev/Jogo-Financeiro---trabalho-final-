import random
import time
from rich.console import Console
from rich.panel   import Panel
from rich.prompt  import Prompt, FloatPrompt, IntPrompt

console = Console()



def _pedir_aposta(perfil):
    """Solicita e valida o valor da aposta."""
    while True:
        valor = FloatPrompt.ask(
            f"[bold]Quanto quer apostar?[/] "
            f"(saldo: [green]R$ {perfil['saldo']:,.2f}[/]) (R$)"
        )
        if valor <= 0:
            console.print("[red]O valor deve ser maior que zero.[/]")
        elif valor > perfil["saldo"]:
            console.print("[red]Saldo insuficiente![/]")
        else:
            return valor


def _menu_jogar_novamente(jogo_func, perfil):
    """Pergunta se o jogador quer jogar de novo."""
    console.print(Panel(
        "[gold1 bold](1)[/] Jogar novamente\n"
        "[dim](2)[/] Sair",
        border_style="dim"
    ))
    opcao = Prompt.ask("[bold]Opção[/]", choices=["1", "2"])
    if opcao == "1":
        jogo_func(perfil)
    else:
        console.print("[dim]Te esperamos na próxima![/]")
        time.sleep(1.0)



def casa_de_apostas(perfil):
    console.print(Panel(
        f"[bold]Jogue com responsabilidade![/]\n"
        f"[dim]Proibido para menores de 18 anos.[/]\n\n"
        f"Saldo disponível: [green bold]R$ {perfil['saldo']:,.2f}[/]\n\n"
        "[gold1 bold](1)[/] Tigrinho\n"
        "[gold1 bold](2)[/] Roleta\n"
        "[gold1 bold](3)[/] Blackjack\n"
        "[gold1 bold](4)[/] Loteria\n"
        "[gold1 bold](5)[/] Aposta Esportiva\n"
        "[dim](6)[/] Sair",
        title="[bold gold1]🎰 CASA DE APOSTAS[/]",
        border_style="gold1"
    ))

    escolha = Prompt.ask("[bold]Jogo escolhido[/]", choices=["1","2","3","4","5","6"])

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
        console.print("[dim]Até a próxima![/]")
        time.sleep(1.0)


def tigrinho(perfil):
    console.print(Panel(
        "[bold]🐯 | 🐼 | 🐷 | 🦁 | 🐭 | 🦊[/]\n\n"
        "3 iguais → [green bold]aposta × 10[/]\n"
        "2 iguais → [yellow bold]aposta × 2[/]",
        title="[bold gold1]🐯 TIGRINHO[/]",
        border_style="gold1"
    ))

    valor = _pedir_aposta(perfil)
    perfil["saldo"] -= valor

    simbolos = ["🐯", "🐼", "🐷", "🦁", "🐭", "🦊"]
    console.print("[dim]Girando[/]", end="")
    for _ in range(3):
        time.sleep(0.5)
        console.print(".", end="")

    s1, s2, s3 = (random.choice(simbolos) for _ in range(3))

    console.print(f"\n[bold]  [ {s1} ][/]")
    time.sleep(1.0)
    console.print(f"[bold]  [ {s1} | {s2} ][/]")
    time.sleep(1.0)
    console.print(f"[bold]  [ {s1} | {s2} | {s3} ][/]")
    time.sleep(1.5)

    if s1 == s2 == s3:
        ganho = valor * 10
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[green bold]JACKPOT! 3 iguais!\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[green]🏆 VOCÊ GANHOU![/]", border_style="green"
        ))
    elif s1 == s2 or s2 == s3 or s1 == s3:
        ganho = valor * 2
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[yellow bold]2 iguais! Dobrou!\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[yellow]✨ QUASE LÁ![/]", border_style="yellow"
        ))
    else:
        cor = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"[red bold]Sem combinação. - R$ {valor:,.2f}[/]\n"
            f"Saldo: [{cor} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[red]❌ PERDEU[/]", border_style="red"
        ))

    _menu_jogar_novamente(tigrinho, perfil)


def roleta(perfil):
    console.print(Panel(
        "Escolha [red bold]vermelho[/] ou [dim]preto[/].\n"
        "Acerte → [green bold]aposta × 2[/]",
        title="[bold gold1]🎡 ROLETA[/]",
        border_style="gold1"
    ))

    valor = _pedir_aposta(perfil)
    cor   = Prompt.ask("[bold]Vermelho ou preto?[/]", choices=["vermelho", "preto"])

    console.print("[dim]A roleta está girando[/]", end="")
    for _ in range(3):
        time.sleep(0.5)
        console.print(".", end="")

    resultado = random.choice(["vermelho", "preto"])
    perfil["saldo"] -= valor

    if cor == resultado:
        ganho = valor * 2
        perfil["saldo"] += ganho
        console.print(Panel(
            f"Saiu [bold]{resultado}[/]! Você acertou!\n"
            f"[green bold]+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[green]🏆 VOCÊ GANHOU![/]", border_style="green"
        ))
    else:
        cor_saldo = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"Saiu [bold]{resultado}[/]. Você apostou em {cor}.\n"
            f"[red bold]- R$ {valor:,.2f}[/]\n"
            f"Saldo: [{cor_saldo} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[red]❌ PERDEU[/]", border_style="red"
        ))

    _menu_jogar_novamente(roleta, perfil)


def blackjack(perfil):
    console.print(Panel(
        "Chegue mais perto de [bold]21[/] sem ultrapassar!\n"
        "Dealer para em 17. Empate → aposta devolvida.",
        title="[bold gold1]🃏 BLACKJACK[/]",
        border_style="gold1"
    ))

    valor = _pedir_aposta(perfil)

    console.print("[dim]Distribuindo as cartas[/]", end="")  
    for _ in range(3):
        time.sleep(0.5)
        console.print(".", end="")

    def sortear_carta():
        return random.randint(1, 10)

    jogador = sortear_carta() + sortear_carta()
    dealer  = sortear_carta() + sortear_carta()

    console.print(f"\n[bold]Sua mão:[/]                [yellow bold]{jogador}[/]")
    console.print(f"[bold]Carta visível do dealer:[/] [dim]{dealer // 2}[/]")

    while jogador < 21:
        acao = Prompt.ask(
            "[bold]Pedir carta[/] (1) ou [bold]parar[/] (0)?",
            choices=["1", "0"]
        )
        if acao == "1":
            console.print("[dim]Sorteando carta[/]", end="")
            for _ in range(3):
                time.sleep(0.3)
                console.print(".", end="")
            carta = sortear_carta()
            jogador += carta
            console.print(f"\n[bold]Você recebeu:[/] [yellow]{carta}[/]  Total: [yellow bold]{jogador}[/]")
            if jogador > 21:
                console.print("[red bold]Passou de 21![/]")
                break
        else:
            break

    perfil["saldo"] -= valor
    console.print(f"\n[bold]Mão do dealer:[/] [dim]{dealer}[/]")

    if jogador > 21:
        # Jogador estourou
        cor_saldo = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"[red bold]Você passou de 21! - R$ {valor:,.2f}[/]\n"
            f"Saldo: [{cor_saldo} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[red]❌ PERDEU[/]", border_style="red"
        ))
    elif dealer > 21:
        # ✅ BUG CORRIGIDO: dealer estourou → jogador ganha
        ganho = valor * 2
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[green bold]Dealer passou de 21! Você ganhou!\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[green]🏆 VOCÊ GANHOU![/]", border_style="green"
        ))
    elif jogador > dealer:
        ganho = valor * 2
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[green bold]Sua mão ({jogador}) > Dealer ({dealer})!\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[green]🏆 VOCÊ GANHOU![/]", border_style="green"
        ))
    elif jogador == dealer:
        perfil["saldo"] += valor
        console.print(Panel(
            f"[yellow]Empate! ({jogador} vs {dealer})\nAposta devolvida.[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[yellow]🤝 EMPATE[/]", border_style="yellow"
        ))
    else:
        cor_saldo = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"[red bold]Dealer ({dealer}) > Você ({jogador})! - R$ {valor:,.2f}[/]\n"
            f"Saldo: [{cor_saldo} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[red]❌ DEALER VENCEU[/]", border_style="red"
        ))

    _menu_jogar_novamente(blackjack, perfil)


def loteria(perfil):
    console.print(Panel(
        "Escolha [bold]3 números[/] de 1 a 30.\n\n"
        "3 acertos → [green bold]aposta × 10[/]\n"
        "2 acertos → [yellow bold]aposta × 2[/]\n"
        "1 acerto  → [dim]aposta devolvida[/]",
        title="[bold gold1]🎟️ LOTERIA[/]",
        border_style="gold1"
    ))

    valor = _pedir_aposta(perfil)

    numeros_jogador = []
    console.print("[bold]Digite seus 3 números (1–30):[/]")
    while len(numeros_jogador) < 3:
        try:
            n = IntPrompt.ask(f"  Número {len(numeros_jogador) + 1}")
            if n < 1 or n > 30:
                console.print("[red]Digite um número entre 1 e 30.[/]")
            elif n in numeros_jogador:
                console.print("[red]Número já escolhido![/]")
            else:
                numeros_jogador.append(n)
        except Exception:
            console.print("[red]Digite um número válido.[/]")

    console.print("[dim]Sorteando os números[/]", end="")
    for _ in range(3):
        time.sleep(0.5)
        console.print(".", end="")

    sorteados = random.sample(range(1, 31), 3)
    acertos   = len(set(numeros_jogador) & set(sorteados))

    console.print("\n[bold]Números sorteados:[/]")
    for numero in sorteados:
        time.sleep(0.8)
        console.print(f"  [yellow bold]{numero}[/]")

    console.print(f"\n[bold]Seus números:[/] {numeros_jogador}")
    console.print(f"[bold]Acertos:[/] [yellow bold]{acertos} acerto(s)[/]")  

    perfil["saldo"] -= valor

    if acertos == 3:
        ganho = valor * 10
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[green bold]3 acertos! Jackpot!\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[green]🏆 VOCÊ GANHOU![/]", border_style="green"
        ))
    elif acertos == 2:
        ganho = valor * 2
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[yellow bold]2 acertos! Dobrou!\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[yellow]✨ QUASE LÁ![/]", border_style="yellow"
        ))
    elif acertos == 1:
        perfil["saldo"] += valor
        console.print(Panel(
            f"[dim]1 acerto. Aposta devolvida.[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[yellow]↩️ DEVOLVIDO[/]", border_style="yellow"
        ))
    else:
        cor_saldo = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"[red bold]Nenhum acerto. - R$ {valor:,.2f}[/]\n"
            f"Saldo: [{cor_saldo} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[red]❌ PERDEU[/]", border_style="red"
        ))

    _menu_jogar_novamente(loteria, perfil)


def jogo_futebol(perfil):
    times = {
        "1": {"nome": "Flamengo",    "chance": 40, "multiplicador": 2},
        "2": {"nome": "Palmeiras",   "chance": 25, "multiplicador": 3},
        "3": {"nome": "São Paulo",   "chance": 15, "multiplicador": 5},
        "4": {"nome": "Corinthians", "chance": 12, "multiplicador": 7},
        "5": {"nome": "Remo",        "chance": 8,  "multiplicador": 10},
    }

    console.print(Panel(
        "[bold](1)[/] Flamengo    — favorito   [dim][40% | ×2][/]\n"
        "[bold](2)[/] Palmeiras   — bom        [dim][25% | ×3][/]\n"
        "[bold](3)[/] São Paulo   — médio      [dim][15% | ×5][/]\n"
        "[bold](4)[/] Corinthians — azarão     [dim][12% | ×7][/]\n"
        "[bold](5)[/] Remo        — sortudo    [dim][8%  | ×10][/]",
        title="[bold gold1]⚽ APOSTA ESPORTIVA — BRASILEIRÃO 2026[/]",
        border_style="gold1"
    ))

    valor      = _pedir_aposta(perfil)
    escolha    = Prompt.ask("[bold]Qual time você escolhe?[/]", choices=list(times.keys()))
    escolhido  = times[escolha]
    times_lista = [t["nome"] for t in times.values()]

    console.print(f"\n[bold]Seu time:[/] [yellow bold]{escolhido['nome']}[/]")
    console.print("[dim]Começou o campeonato...[/]")
    time.sleep(0.5)
    console.print(f"[dim]{random.choice(times_lista)} saiu na frente.[/]")
    time.sleep(1.5)
    console.print("[dim]Fim da primeira fase...[/]")
    console.print(f"[dim]{random.choice(times_lista)} assume a liderança.[/]")
    time.sleep(1.5)
    console.print("[dim]Chegando no final do campeonato...[/]")
    console.print(f"[dim]{random.choice(times_lista)} está cada vez mais perto do título.[/]")
    time.sleep(2.0)

    vencedor = random.choices(
        list(times.values()),
        weights=[c["chance"] for c in times.values()],
        k=1
    )[0]

    console.print(f"\n[bold yellow]🏆 {vencedor['nome']} é o CAMPEÃO DO BRASILEIRÃO 2026![/]")
    perfil["saldo"] -= valor

    if escolhido["nome"] == vencedor["nome"]:
        ganho = valor * escolhido["multiplicador"]
        perfil["saldo"] += ganho
        console.print(Panel(
            f"[green bold]Seu time ganhou! ×{escolhido['multiplicador']}\n+ R$ {ganho:,.2f}[/]\n"
            f"Saldo: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[green]🏆 VOCÊ GANHOU![/]", border_style="green"
        ))
    else:
        cor_saldo = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"[red bold]{escolhido['nome']} não ganhou. - R$ {valor:,.2f}[/]\n"
            f"Saldo: [{cor_saldo} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[red]❌ PERDEU[/]", border_style="red"
        ))

    _menu_jogar_novamente(jogo_futebol, perfil)
