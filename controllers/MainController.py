from models.DB import DB
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

    def get_total_turn_amount_all(self):
        db = DB()
        rows = db.query(
            'SELECT distinct(username), count(username)FROM Game where guess_amount != 0 group by username order by guess_amount')
        db.close()
        return rows

    def get_details_of_player(self, username):
        db = DB()
        rows = db.query('SELECT username, start_time, guess_amount from Game where username = ? and guess_amount != 0',
                        (username,))
        db.close()
        return rows

    def resetGame(self):
        self.player = None
        self.game = None
        self.is_configured = False

    def get_player(self):
        return self.player

    def get_turns_taken(self):
        return self.game.get_turns_taken()

    def get_correct_order(self):
        return self.game.get_correct_order()
