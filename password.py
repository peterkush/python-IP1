class User:
    user_list = []
    def __init__(self,user_name,User_password):
        self.user_name = user_name
        self.User_password = User_password
    def save_user(self):
        User.user_list.append(self)
    def delete_user(self ):
        User.user_list.remove(self)

class Credential:
    credential_list = []
       
    def _init_(self,account,account_username,account_password):
        self.account = account
        self.account_username = account_username
        self.account_password = account_password
    def save_credential(self):
        Credential.credential_list.append(self)
    def delete_credential(self):
        Credential.credential_list.remove(self)

    

    