from models.Game import Game
from models.Player import Player


class MainController(object):

    def __init__(self):
        self.player = None
        self.game = None

    def add_new_player(self, username):
        self.player = Player(username)

    def add_settings(self, doublecolors, coloramount, positionamount):
        self.player.commit_to_db()
        player_id = self.player.get_from_db()
        self.game = Game(player_id, doublecolors, coloramount, positionamount)

