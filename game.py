class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Nome: {self.__name}\nVida: {self.__life}\nNível: {self.__level}"


class Hero(Character):
    def __init__(self, name, life, level, special):
        super().__init__(name, life, level)
        self.__special = special

    def get_special(self):
        return self.__special

    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_special()}\n"


class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        return f"{super().show_details()}\nTipo: {self.get_type()}\n"


class Game:
    """Classa Orquestadora do Jogo"""

    def __init__(self) -> None:
        self.hero = Hero(name="Guilherme", life=100, level=5, special="Kamehamera")
        self.enemy = Enemy(name="Black", life=100, level=4, type="SSR")

    def initBatle(self):
        """Fazer a gestão da batalha"""
        print("Iniciando a batalha")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhe dos personagens: ")
            print(f"{self.hero.show_details()}")
            print(f"{self.enemy.show_details()}")

        input("Pressione ENTER para atacar...")
        escolha = input("1 - Ataque normal | 2 - Especial: ")


game = Game()
game.initBatle()
