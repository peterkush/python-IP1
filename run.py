from password import User, Credential
import random
import string
import getpass

def create_user(name, user_password):
    new_user = User(name, user_password)
    return new_user
def generate_password(user):
    return user.generate_random_password()
