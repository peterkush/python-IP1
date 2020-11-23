class User:
    def __init__(self,user_name,User_password):
        self.user_name = user_name
        self.User_password = User_password
    def save_user(self):
        User.user_list.append(self)
    def delete_user(self ):
        User.user_list.remove(self)

    