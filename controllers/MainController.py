from models.Player import Player


class MainController(object):

    def __init__(self):

        self.player = Player
    
    def test(self):
        pass

    def add_new_player(self, username):
        self.player = Player(username)
        print(self.player)
