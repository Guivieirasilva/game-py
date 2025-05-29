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

    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def attack(self, target):
        damage = self.__level * 2
        target.receive_attack(damage)
        print(
            f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!"
        )


class Hero(Character):
    def __init__(self, name, life, level, special):
        super().__init__(name, life, level)
        self.__special = special

    def get_special(self):
        return self.__special

    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_special()}\n"

    def attack_special(self, target):
        damage = self.get_level() * 5
        target.receive_attack(damage)
        print(
            f"{self.get_name()} usou a habilidade especial: {self.get_special()}",
            f"no {target.get_name()} e causou {damage} de dano!",
        )


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
        self.hero = Hero(name="Goku", life=100, level=5, special="Kamehamera")
        self.enemy = Enemy(name="Black", life=100, level=4, type="SSR")

    def initBatle(self):
        """Fazer a gestão da batalha"""
        print("Iniciando a batalha")

        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhe dos personagens: ")
            print(f"{self.hero.show_details()}")
            print(f"{self.enemy.show_details()}")

            input("Pressione ENTER para atacar...")
            select = int(input("1 - Ataque normal | 2 - Especial: "))

            if select == 1:
                self.hero.attack(self.enemy)

            elif select == 2:
                self.hero.attack_special(self.enemy)

            else:
                print("Escolha inválida. Escolha novamente!")

            if self.enemy.get_life() > 0:
                """Inimigo ataca o heroi"""
                self.enemy.attack(self.hero)

        if self.hero.get_life() > 0:
            print("Parabéns você foi o vencedor!")

        else:
            print("Você foi derrotado")


game = Game()
game.initBatle()
