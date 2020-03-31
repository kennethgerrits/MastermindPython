from models.DB import DB


class Player:

    def __init__(self, username):
        self.username = username
        print(username + ' has been created')

    def commit_to_db(self):
        db = DB()
        db.query('INSERT INTO Player (username) SELECT(?) WHERE NOT EXISTS(SELECT 1 FROM Player WHERE username = ?)'
                 , (self.username, self.username))

    def get_from_db(self):
        db = DB()
        player_id = db.query('SELECT id FROM player WHERE username = ?', (self.username,))
        print(player_id[0])
        return player_id
