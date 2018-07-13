# Paper beats rock; rock beats scissors; scissors beat paper.

# code below is for switching to Spock game. This is not finished.
# def populate_moves(type):
#     if type == "RPS":
#         return ["rock", "paper", "scissors"]
#     elif type == "Spock":
#         return ["rock", "paper", "scissors", "spock", "lizard"]


class Game:
    """
        The Game class stores all the games attributes, and determines the
        result of each round and the final score according to the game's rules.
    """
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 1
        self.rules = {"rock": ["lizard", "scissors"], "paper":
                      ["rock", "Spock"], "scissors": ["lizard", "paper"],
                      "Spock": ["rock", "scissors"], "lizard": ["Spock",
                      "paper"]}
        self.score = {"player0": 0, "player1": 0}

    def adjudicate_round(self, player0, player1):
        if player0 == player1:
            print("No one won this round. Moving on...")
        elif player0 not in self.rules[player1]:
            self.score["player0"] += 1
            print("This round was won by the human.")
        else:
            self.score["player1"] += 1
            print("This round was won by the computer.")
        print("Current results: human: {}, computer: {}".format(
            str(self.score["player0"]), str(self.score["player1"])))

    def present_final_results(self):
        print("The final results are {} for the human and {} for the computer."
              .format(str(self.score["player0"]), str(self.score["player1"])))
