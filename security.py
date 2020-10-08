from werkzeug.security import safe_str_cmp
from models.user import UserModel


# a table
# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# ]

# just created an object in another file and imported it from there
# so now it can be like below
# key - name
# username_mapping = { 'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }

# u.username : u = key : value pairs

# username_mapping['bob']
# usernae_mapping[1]
# mapping saves iteration every time

# key - id
# userid_mapping = { 1: {
#         'id': 1,
#         'username': 'bob',
#         'password': 'asdf'
#     }
# }

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
