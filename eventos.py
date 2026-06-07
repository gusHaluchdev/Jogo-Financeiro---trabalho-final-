import random
import time
from rich.console import Console
from rich.panel   import Panel

console = Console()


def gerar_evento_aleatorio(perfil):
    eventos_bons = [
        {"descricao": "Você recebeu um bônus no trabalho!", "valor": 500.0},
        {"descricao": "Você achou dinheiro na rua!",        "valor": 100.0},
        {"descricao": "Você ganhou um presente em dinheiro!", "valor": 300.0},
    ]
    eventos_ruins = [
        {"descricao": "Seu carro quebrou!",            "valor": 800.0},
        {"descricao": "Você recebeu uma multa!",        "valor": 200.0},
        {"descricao": "Problema de saúde inesperado!", "valor": 600.0},
    ]

    numero = random.randint(1, 100)

    if numero <= 40:
        evento = random.choice(eventos_bons)
        perfil["saldo"] += evento["valor"]
        console.print(Panel(
            f"[green bold]{evento['descricao']}[/]\n"          
            f"[green bold]+ R$ {evento['valor']:,.2f}[/]\n"
            f"Saldo atual: [green bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[bold green]🍀 EVENTO POSITIVO[/]",
            border_style="green"
        ))
    else:
        evento = random.choice(eventos_ruins)
        perfil["saldo"] -= evento["valor"]
        cor = "green" if perfil["saldo"] >= 0 else "red"
        console.print(Panel(
            f"[red bold]{evento['descricao']}[/]\n"            
            f"[red bold]- R$ {evento['valor']:,.2f}[/]\n"
            f"Saldo atual: [{cor} bold]R$ {perfil['saldo']:,.2f}[/]",
            title="[bold red]⚠️  EVENTO NEGATIVO[/]",
            border_style="red"
        ))

    time.sleep(1.5)
