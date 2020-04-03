class Player:

    def __init__(self, username):
        self.username = username
        print(username + ' has been created')

    def get_username(self):
        return self.username


