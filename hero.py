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