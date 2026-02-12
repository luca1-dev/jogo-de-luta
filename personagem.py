class Personagem():
    def __init__(
        self,
        nome : str,
        ataque_1 : str = "",
        ataque_2 : str = "",
        ataque_especial : str = "",
        defesa : str = ""
            ):

        self._nome = nome
        self._hp = 20
        self._ataque_1 = ataque_1
        self._ataque_2 = ataque_2
        self._ataque_especial = ataque_especial
        self._defesa = defesa


    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None :
        self._nome = nome

    @property
    def ataque_1(self) -> str:
        return self._ataque_1

    @ataque_1.setter
    def ataque_1(self, ataque_1: str) -> None :
        self._ataque_1 = ataque_1 
    
    @property
    def ataque_2(self) -> str:
        return self._ataque_2

    @ataque_2.setter
    def ataque_2(self, ataque_2: str) -> None :
        self._ataque_2 = ataque_2

    @property
    def ataque_especial(self) -> str :
        return self._ataque_especial

    @ataque_especial.setter
    def ataque_especial(self, ataque_especial: str) -> None :
        self._ataque_especial = ataque_especial

    @property
    def defesa(self) -> str:
        return self._defesa

    @defesa.setter
    def defesa(self, defesa: str) -> None :
        self._defesa = defesa

    def recebendo_dano(self, dano : int) -> None:
        self._hp -= dano


    def mostrar_golpes(self) -> None:
        golpes = "      1) ATAQUE BASICO 1\n" \
        "2) ATAQUE BASICO 2\n      3) ATAQUE ESPECIAL\n"\
        "4) DEFESA\n"

        print(golpes)

    def escolher_golpe(self, golpe : str) -> None:
        lista_escolhas = {
            '1' : self.ataque_1,
            '2' : self.ataque_2,
            '3' : self.ataque_especial,
            '4' : self.defesa,
        }

if __name__== "__main__":
    teste = Personagem("Luffy", "Soco", "Chute", "Voadora", "Esquivar")
    teste.mostrar_golpes()