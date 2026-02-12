from typing import TYPE_CHECKING
from time import sleep
import os
import sys

import random
if TYPE_CHECKING:
    from personagem import Personagem

def limpar_console(tempo_ate_limpar : int):
    sleep(tempo_ate_limpar)
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

class Luta():
    def __init__(
        self,
        jogador : 'Personagem',
        bot : 'Personagem'
        ):

        self._jogador = jogador
        self._bot = bot

    def round(self) -> None:
        print("Agora é a sua vez. O que deseja fazer? ")
        self._jogador.mostrar_golpes()
        escolha_jogador = input("Digite a sua escolha: ")
        limpar_console(2)
        print("Muito bem, agora é a vez do adversario.")
        print("Aguarde a sua vez.")
        
        limpar_console(2)
        
        