import random
import datetime

from models.DB import DB


class Game:

    def __init__(self, player, double, coloramount, positionamount):
        self.player = player
        self.game_id = None
        self.double = bool(double)
        self.turnsTaken = 0
        self.colorAmount = int(coloramount)
        self.positionAmount = int(positionamount)
        self.correctOrder = []
        self.availableColors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple', 'pink', 'white', 'black',
                                'skyblue'][:self.colorAmount]
        self.history = [[], []]
        self.create_order()
        self.insert_to_db()

    def get_available_colors(self):
        return self.availableColors

    def get_is_configured(self):
        return self.is_configured

    def get_position_amount(self):
        return self.positionAmount

    def get_history(self):
        return self.history

    def create_order(self):
        colors = self.availableColors.copy()
        for i in range(self.positionAmount):
            picked = random.choice(colors)
            self.correctOrder.append(picked)
            if not self.double:
                colors.remove(picked)

    def guess(self, guessed):
        pinlist = []
        self.turnsTaken += 1
        self.update_to_db()
        correctOrder = self.correctOrder.copy()
        notGuessed = guessed.copy()
        for i in range(len(guessed)-1, -1, -1):
            if guessed[i] in correctOrder and correctOrder[i] == guessed[i]:
                pinlist.append('black')
                correctOrder.pop(i)
                notGuessed.pop(i)

        for color in notGuessed:
            if color in correctOrder:
                correctOrder.remove(color)
                pinlist.append('white')
            else:
                pinlist.append('grey')

        # random.shuffle(pinlist)
        self.history[0].append(guessed)
        self.history[1].append(pinlist)
        if self.correctOrder == guessed:
            return (True, pinlist,)
        else:
            return (False, pinlist,)

    def insert_to_db(self):
        db = DB()
        self.game_id = db.execute_and_return(
            'INSERT INTO Game (username, guess_amount, has_cheated, start_time) VALUES (?,?,?,?)'
            , (self.player.get_username(), self.turnsTaken, 0, datetime.datetime.now(),))
        db.close()

    def update_to_db(self):
        db = DB()
        db.execute('UPDATE Game SET guess_amount = ? WHERE id = ?', (self.turnsTaken, self.game_id,))
        db.close()

    def update_cheated_to_db(self):
        db = DB()
        db.execute('UPDATE Game SET has_cheated = 1 WHERE id = ?', (self.game_id,))
        db.close()


    def get_turns_taken(self):
        return self.turnsTaken

    def get_correct_order(self):
        return self.correctOrder
