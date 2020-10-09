from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    # .get: another way to access value by a key
    # also able to set a default value with this method
    user = UserModel.find_by_username(username)
    # safe_str_cmp compares strings even in older python versions
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):  # payload - content of the JWT Token
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
