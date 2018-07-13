
from player import *
from game import *

# code below is a work in progress to add the Spock version of the game.
# def get_game_type():
#     game_prompt_text = """What kind of game do you want to play?
#  Your options are RPS or spock. \n"""
#     print(game_prompt_text)
#     game_selection = ""
#     while game_selection not in ["RPS", "Spock"]:
#         game_selection = input("Select RPS or Spock. ")
#     if game_selection == "RPS":
#         return ["rock", "paper", "scissors"]
#     else:
#         return ["rock", "paper", "scissors", "spock", "lizard"]


def get_number_of_rounds():
    round_number_text = """Now let's establish how many rounds you want to playself.
Please enter a number."""
    while True:
        rounds = input("\nPlease select a number. ")
        if rounds.isnumeric():
            return rounds


def setup_game():
    intro = """Hello and welcome to the RPS game!
Let's get your game set up. Please answer a few
questions so we know your preferences."""
    print(intro)
    number_of_rounds = get_number_of_rounds()
    game = Game(int(number_of_rounds))
    return game


def run_game():
    game = setup_game()
    player0 = Human()
    player1 = [RockEnthusiast(), Reflect(), RandomPlayer(), Cycle()].pop(
              randint(0, 2))
    current_round = 1
    while current_round <= game.rounds:
        print("playing round {}!".format(str(current_round)))
        player_0_move = player0.play()
        player_1_move = player1.play()
        game.adjudicate_round(player_0_move, player_1_move)
        if player1.echo:
            player1.memory = player_0_move
        current_round += 1
    game.present_final_results()


run_game()
