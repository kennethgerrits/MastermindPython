from models.DB import DB


class Player:

    def __init__(self, username):
        self.username = username
        print(username + ' has been created')

    def get_username(self):
        return self.username

    # def commit_to_db(self):
    #     db = DB()
    #     db.execute_and_return('INSERT OR IGNORE INTO Player (username) VALUES(?);'
    #                                       , (self.username,))
    #     db.close()
    #
    # def get_from_db(self):
    #     db = DB()
    #     player_id = db.query('SELECT id FROM Player WHERE username = ?', (self.username,))
    #     print(player_id)
    #     return player_id
