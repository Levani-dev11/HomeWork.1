class Player:
    players_count = 0

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        Player.players_count += 1


print(Player.players_count)

player1 = Player("ანა")
player2 = Player("დავითი", 5)
player3 = Player(name="მარიამი", level=3)

print(f"სულ მოთამაშე: {Player.players_count}")

print(player1.name, player1.level)
print(player2.name, player2.level)
print(player3.name, player3.level)