from models.Game import Game
from models.Player import Player


class MainController(object):

    def __init__(self):
        self.player = None
        self.game = None
        self.is_configured = False

    def add_new_player(self, username):
        self.player = Player(username)

    def add_settings(self, doublecolors, coloramount, positionamount):
        self.game = Game(self.player, doublecolors, coloramount, positionamount)
        self.is_configured = True

    def play_turn(self, guessedOrder):
        return self.game.guess(guessedOrder)


    def get_available_colors(self):
        return self.game.get_available_colors()

    def get_is_configured(self):
        return self.is_configured

    def get_position_amount(self):
        return self.game.get_position_amount()

    def get_history(self):
        return self.game.get_history()
