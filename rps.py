
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


def get_game_type():
    while True:
        game_type = ""
        print("Do you want to play a single or a tournament?")
        while game_type not in ["single", "tournament"]:
            game_type = input("\nPlease select a game type. ")
        return game_type


def setup_game():
    intro = """Hello and welcome to the RPS game!
Let's get your game set up. Please answer a few
questions so we know your preferences."""
    print(intro)
    game_type = get_game_type()
    if game_type == "single":
        game = SingleRound()
    else:
        game = Tournament()
    return game


def run_game():
    game = setup_game()
    player0 = Human()
    player1 = [RockEnthusiast(), Reflect(), RandomPlayer(), Cycle()].pop(
              randint(0, 2))
    current_round = 1
    while game.play_on is True:
        print("playing round {}!".format(str(current_round)))
        player_0_move = player0.play()
        player_1_move = player1.play()
        game.adjudicate_round(player_0_move, player_1_move)
        if player1.echo:
            player1.memory = player_0_move
        game.current_round += 1
        game.decide_continuation()
    game.present_final_results()


run_game()
