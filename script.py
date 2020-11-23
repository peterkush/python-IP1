from password import User, Credential
import random
import string
import getpass

def create_user(name, user_password):
    new_user = User(name, user_password)
    return new_user
def generate_password(user):
    return user.generate_random_password()
def save_user(user):
    user.save_user()
def delete_user(user):
    user.delete_user()
def create_credential(account, account_username, account_password):
    new_credential = Credential(account, account_username, account_password)
    return new_credential
def save_credential(credential):
    credential.save_credential()
def delete_credential(credential):
    credential.delete_credential()
def find_credential(account_username):
    return Credential.find_by_account_username(account_username)
def check_existing_credential(account_username):
    return Credential.find_by_account_username(account_username)
def display_credential():
    return Credential.display_all_credential()


def main():
    user_name = input("Enter your name..")
    print(f"Hello {user_name},welcome  to password locker")
    print("\n")
    ask = input(f"Hi..! { user_name} .Do you have an account ? YES?NO ..").lower()
    if ask == "no":
        print("Sign in to password locker")
        user_name = input("Enter your name..") 
        print(f"Hello {user_name} .Generated password ?YES/NO >"

        ) 
        if create_user == "no":
            print("_"*167)
            print("|Passwords may not be visible coz they are secured|")
            print(""*67)
            getpass.getpass()
            print("You are logged in")
            while True:

                      print("Use these short codes : cc - create a new credential, dc - display credential, fc - find credential, dl - delete credential, gp - generate random password, ex - exit the credential list")
                      short_code = input().lower()
                      if short_code == 'cc':
                           print("create account")
                           print("_"*10)
                           
                           print("Account.....")
                           account = input(">")

                           print("usename....")
                           account_username = input(">")

                           print("Enter password")
                           account_password = input(">")

                           save_credential(create_credential(account, account_username, account_password))

                           print("\n")
                           print(f"New Credential {account} {account_username} {account_password} has been created")
                           print("\n")
        elif short_code == "gp":
                        print("Please enter the account you want to generate password for > ")
                        social_media = input("Enter account type > ")

                        def random_password(string_length):
                            letters = string.ascii_letters
                            return "".join(random.choice(letters) for i in range(string_length))

                        print(f"Your random password for {social_media} is:", random_password(8))

        elif short_code == "dc":
                        if display_credential():
                            print("Here is a list of credentials and password")
                            print("\n")
                        else:
                            print("\n")
                            print("You do not have any saved credential, try saving one")
                            print("\n")
        elif short_code == "fc":
                        print("Enter the account username you are searching")
                        search_account_username = input()
                        if check_existing_credential(search_account_username):
                            search_credential = find_credential(search_account_username)
                            print(f"{search_credential.account} {search_credential.account_username}")
                            print('_'*20)
                            print(f"Account password...{search_credential.account_password}")
                        else:
                            print("The credential does not exist.Try to resign in")

        elif short_code == "dl":
                        print("Enter the account username your will like to delete.")
                        my_delete = input(">")
                        my_del = find_credential(my_delete)
                        Credential.credential_list.remove(my_del)
                        print(f"Credential with account username {my_delete} has been removed successfully")


        elif short_code == "ex":
                        print("logged out")
                         #exit

        else:
                        print("please check your entry")



if __name__ == '__main__':
    main()