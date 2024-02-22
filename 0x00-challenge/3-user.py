import hashlib
import uuid

class User:
    __password = None

    def __init__(self):
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pwd):
        if pwd and isinstance(pwd, str):
            self.__password = hashlib.md5(pwd.encode()).hexdigest().lower()
        else:
            self.__password = None

    def is_valid_password(self, pwd):
        if pwd and isinstance(pwd, str) and self.__password:
            return hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password
        return False

if __name__ == '__main__':
    # Test cases
    user_1 = User()
    assert user_1.id is not None, "New User should have an id"

    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password != u_pwd, "User.password should be hashed"

    assert user_2.password is None, "User.password should be None by default"

    user_2.password = None
    assert user_2.password is None, "User.password should be None if set to None"

    user_2.password = 89
    assert user_2.password is None, "User.password should be None if set to an integer"

    assert user_1.is_valid_password(u_pwd), "is_valid_password should return True if it's the right pa
