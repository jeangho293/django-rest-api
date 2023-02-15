from users.models import User
import bcrypt


class UserService:
    _user = User

    def list(self):
        users = self._user.manager.get_user_list()
        return users

    def add(self, **request):
        account, password, confirm_password = request.values()
        user = self._user.manager.get_user(account=account)

        # NOTE: Need error handler by using raise
        if user:
            return f"{account} is already existed account."
        if password != confirm_password:
            return "Each password is different."

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")
        self._user.manager.create(account=account, password=hashed_password)
        return {"data": "create user"}
