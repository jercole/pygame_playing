#########################################################
#  Author: Joseph Ercole
#  Description:
#  Just messing around with the pygame examples
#
#
#########################################################

from pprint import pprint


def main():
    import pkgutil

    # this is the package we are inspecting -- for example 'email' from stdlib
    import pygame.examples

    package = pygame.examples

    games = [game.name.split(".")[-1] for game in pkgutil.walk_packages(path=package.__path__
                                                                        , prefix=package.__name__ + '.'
                                                                        , onerror=lambda x: None)]
    game_selection_loop(games)

####################################
# Methods Below!
####################################

def game_selection_loop(games):
    """
    :param games:
    :return: Nothing
    """
    while True:
        list_games(games)
        game_name = ask_for_game_choice(games)
        if game_name != "EXIT_GAME":
            try:
                exec("import pygame.examples.%s as gen" % game_name)
                exec("gen.main()")
                print()
                print("**** Game: '%s' finished. Hit Enter to try Another Game *****" % game_name)
                print("Or type 'EXIT' to leave the game.")
                after_game = input().lower()
                if after_game == "exit":
                    print("As you wish. Exiting game!")
                    break

            except TypeError as e:
                print()
                print("WHOOPS! That game will not work without further input!")
                print("Error was:")
                print("\t%s" % e)
                print("Please try another game.")
                print()
                print("**** Hit Enter to Continue *****")
                input()
        else:
            print("As you wish. Exiting game!")
            break


def list_games(games):
    """
    :param games:
    :return: Nothing
    """
    for idx, game in enumerate(games, 1):
        print("%d: %s" % (idx, game))
    print()
    print("... Or type 'EXIT' to end program.")
    print()
    print()


def ask_for_game_choice(games):
    """
    :param games:
    :return: game_name
    """
    games_len = len(games)
    while locals().get("response", None) is None:
        response = input("Give me the number of a game you'd like to try (1 to %s):   " % games_len)
        if response.lower() == "exit":
            return "EXIT_GAME"
        elif isfloat(response):
            if response.isdigit():
                response = int(response)
                if not (1 <= response <= games_len):
                    print("Silly Monkey! You need to use a number between 1 and %s!!!" % games_len)
                    print()
                    response = None
            else:
                print("Whoa there, Mathematicus! How about we stick to only whole numbers.")
                print()
                response = None
        else:
            print("Gosh . . . I mean, come on. That's not even a number! Try again.")
            print()
            response = None

    game_name = games[response - 1]
    return game_name


# Press the green button in the gutter to run the script.


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
