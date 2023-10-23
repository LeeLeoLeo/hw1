class Superhero:
    people = 'people'

    def __init__(self, name, nickname, superpower, healpoints, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.healpoints = healpoints
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def get_heal(self):
        return self.healpoints * 2

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.healpoints}'

    def __len__(self):
        return len(self.catchphrase)


guy = Superhero('Georg', 'Gora', 'earning money', 300, "im not your dad")
print(guy)
print(guy.get_name())
print(guy.get_heal())
print(guy.__len__())


class Puperhero(Superhero):

    def __init__(self, name, nickname, superpower, healpoints, catchphrase, damage):
        super().__init__(name, nickname, superpower, healpoints, catchphrase)
        self.damage = damage
        self.fly = False

    def get_heal(self):
        self.fly = True
        return self.healpoints ** 2

    def newphrase(self):
        return "True in the True_phrase"


class Juperhero(Superhero):
    def __init__(self, name, nickname, superpower, healpoints, catchphrase, damage):
        super().__init__(name, nickname, superpower, healpoints, catchphrase)
        self.damage = damage
        self.fly = False

    def get_heal(self):
        self.fly = True
        return self.healpoints ** 2

    def newphrase(self):
        return "True in the True_phrase"


new_guy = Puperhero("Valera", "Valya", "wasting money", 100, "im rich!!", 20)
print(new_guy.get_heal())
print(new_guy.newphrase())
newer_guy = Juperhero("Venya", "Ven", "giving some money", 500, "im just a guy!!", 5)
print(new_guy.get_heal())
print(new_guy.newphrase())


class Villian(Puperhero):
    def __init__(self, name, nickname, superpower, healpoints, catchphrase, damage):
        super().__init__(name, nickname, superpower, healpoints, catchphrase, damage)

    people = "monster"

    def gen_x(self):
        pass

    def crit(self, damage):
        return damage ** 2


newest_guy = Villian("Zluka", "Z", "steals money", 1000, "im poor!!", 450)

newest_guy.damage = newest_guy.crit(newest_guy.damage)
print(newest_guy.damage)
