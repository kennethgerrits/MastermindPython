from models.Player import Player


class MainController(object):

    def __init__(self):
        self.player = Player

    def add_new_player(self, username):
        self.player = Player(username)
