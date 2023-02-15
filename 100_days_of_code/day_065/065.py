# Day 65: Video Game

class Character:
    name = None
    health = 100
    magic_points = 50

    def __int__(self, name: str) -> None:
        self.name = name

    def print(self) -> None:
        print(
            f'Name: {self.name}',
            f'Health: {self.health}',
            f'Magic Points: {self.magic_points}',
            sep='\n',
            end='\n\n'
        )

    def set_stats(self, health: int, magic_points: int) -> None:
        self.health = health
        self.magic_points = magic_points


class Player(Character):
    nickname = None
    lives = 3

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self.name = 'Player'

    def is_alive(self) -> bool:
        if self.lives > 0:
            return True
        else:
            return False

    def print(self) -> None:
        print(
            f'{self.name}',
            f'Name: {self.nickname}',
            f'Health: {self.health}',
            f'Magic Points: {self.magic_points}',
            f'Lives: {self.lives}',
            f'Alive?: {"Yes" if self.is_alive() else "No"}',
            sep='\n',
            end='\n\n'
        )


class Enemy(Character):
    type = None
    strength = 100

    def __init__(self, name: str, type: str, strength: int) -> None:
        self.name = name
        self.type = type
        self.strength = strength

    def print(self) -> None:
        print(
            f'Name: {self.name}',
            f'Health: {self.health}',
            f'Magic Points: {self.magic_points}',
            f'Type: {self.type}',
            f'Strength: {self.strength}',
            sep='\n',
            end='\n\n'
        )


class Orc(Enemy):
    speed = None

    def __init__(self, name: str, strength: int, speed: int) -> None:
        super().__init__(name, 'Orc', strength)
        self.speed = speed

    def print(self):
        print(
            f'Name: {self.name}',
            f'Health: {self.health}',
            f'Magic Points: {self.magic_points}',
            f'Type: {self.type}',
            f'Strength: {self.strength}',
            f'Speed: {self.speed}',
            sep='\n',
            end='\n\n'
        )


class Vampire(Enemy):
    day = True

    def __init__(self, name: str, strength: int, day: bool) -> None:
        super().__init__(name, 'Vampire', strength)
        self.day = day

    def print(self):
        print(
            f'Name: {self.name}',
            f'Health: {self.health}',
            f'Magic Points: {self.magic_points}',
            f'Type: {self.type}',
            f'Strength: {self.strength}',
            f'Day/Night: {"Day" if self.day else "Night"}',
            sep='\n',
            end='\n\n'
        )


def main() -> None:
    title = '🌟Generic RPG🌟\n'
    print(title)

    david = Player(nickname='David')
    david.print()

    boris = Vampire(name='Boris', strength=3, day=False)
    boris.set_stats(45, 70)
    boris.print()

    rishi = Vampire(name='Rishi', strength=75, day=True)
    rishi.set_stats(70, 10)
    rishi.print()

    bill = Orc(name='Bill', strength=75, speed=90)
    bill.set_stats(60, 5)
    bill.print()

    ted = Orc(name='Ted', strength=80, speed=45)
    ted.set_stats(75, 40)
    ted.print()

    station = Orc(name='Station', strength=49, speed=50)
    station.set_stats(35, 40)
    station.print()


if __name__ == '__main__':
    main()
