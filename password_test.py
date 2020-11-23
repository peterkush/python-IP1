import unittest
from password import User ,Credential

class TestUser(unittest.Testcase):
    def setUp(self):
        self.new_user =('peter', '1111')