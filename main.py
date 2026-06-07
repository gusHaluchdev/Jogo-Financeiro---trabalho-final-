import random
import datetime
import os
import time
import math
import json
from rich.console import Console
from perfil  import exibir_introducao, configurar_perfil
from utils   import exibir_status_mes, processar_fim_de_mes, verificar_condicoes_fim, encerrar_jogo
from eventos import gerar_evento_aleatorio
from acoes   import menu_acoes

console = Console()


def main():
    exibir_introducao()
    perfil  = configurar_perfil()
    rodando = True

    while rodando:
        exibir_status_mes(perfil)
        gerar_evento_aleatorio(perfil)
        menu_acoes(perfil)
        processar_fim_de_mes(perfil)
        rodando = verificar_condicoes_fim(perfil)

    encerrar_jogo(perfil)


if __name__ == "__main__":
    main()
