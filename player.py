from random import randint


class Player():
    """
        This is the general Player class. All other players (including the
        human) are subclasses of this one.
    """
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.memory = "paper"
        self.echo = False


class RandomPlayer(Player):
    """
        This class plays randomly.
    """
    def __init__(self):
        Player.__init__(self)

    def play(self):
        return self.moves[randint(0, 2)]


class RockEnthusiast(Player):
    """
        This class always plays "rock".
    """
    def __init__(self):
        Player.__init__(self)

    def play(self):
        return "rock"


class Reflect(Player):
    """
        Monkey see monkey do.
    """
    def __init__(self):
        Player.__init__(self)
        self.echo = True

    def play(self):
        return self.memory


class Cycle(Player):
    """
        Cycles through the options.
    """
    def __init__(self):
        Player.__init__(self)
        self.cycle_tracker = 0

    def play(self):
        if self.cycle_tracker == 2:
            self.cycle_tracker = 0
        else:
            self.cycle_tracker += 1
        return self.moves[self.cycle_tracker]


class Human(Player):
    """
        Generates no own moves, but instead prompts the human.
    """
    def __init__(self):
        Player.__init__(self)

    def play(self):
        move = ""
        prompt = """
Please select a move to play. Your options are:
1. rock
2. paper
3. scissors
        """
        while move not in self.moves:
            move = input(prompt)
        return move
