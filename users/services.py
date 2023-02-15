from users.models import User


class UserService:
    _user = User

    def list(self):
        users = self._user.manager.get_user_list()
        return users
