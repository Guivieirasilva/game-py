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
        return print(
            f"Nome: {self.__name}\nVida: {self.__life}\nNível: {self.__level}",
        )


class Hero(Character):
    def __init__(self, name, life, level, special):
        super().__init__(name, life, level)
        self.__special = special

    def get_special(self):
        return self.__special

    def show_details(self):
        print(f"{super().show_details()}\nHabilidade: {self.get_special()}\n")
        return


class Enemy(Character):
    def __init__(self, name, life, level, type):
        super().__init__(name, life, level)
        self.__type = type

    def get_type(self):
        return self.__type

    def show_details(self):
        print(f"{super().show_details()}\nTipo: {self.get_type()}\n")
        return


hero = Hero("Guilherm", 100, 5, "Kamehamera")
print(hero.show_details())

enemy = Enemy("Black", 100, 4, "SSR")
print(enemy.show_details())
