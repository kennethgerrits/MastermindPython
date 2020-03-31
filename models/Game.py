import random
import datetime

from models.DB import DB


class Game:

    def __init__(self, playerID, double, coloramount, positionamount):
        self.playerID = playerID
        self.double = bool(double)
        self.guessAmount = 0
        self.hasCheated = False
        self.colorAmount = int(coloramount)
        self.positionAmount = int(positionamount)
        self.correctOrder = []
        self.availableColors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple', 'pink', 'white', 'black', 'skyblue'][:coloramount]
        self.create_order()

    def create_order(self):
        colors = self.availableColors;
        for i in range(self.positionAmount):
            picked = random.choice(colors)
            self.correctOrder.append(random.choice(picked))
            if not self.double:
                colors.remove(picked)

    def insert_to_db(self):
        db = DB()
        db.execute('INSERT INTO Game (Player_id, guess_amount, has_cheated, start_time) VALUES ('
                   + self.playerID
                   + ',' + self.guessAmount
                   + ',' + self.hasCheated
                   + ',' + datetime.datetime.now() + ')')


    def test(self):
        pass
