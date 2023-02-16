from users.serializers import UserSerializer


class UserService:
    _user_serializer = UserSerializer

    def add(self, **kwargs) -> None:
        account: str = kwargs["account"]
        password: str = kwargs["password"]
        confirm_password: str = kwargs["confirm_password"]

        user = self._user_serializer().find_one(account=account)
        if user:
            raise ValueError(f"{account} is already existed.")
        if password != confirm_password:
            raise ValueError("Each password is different.")

        serializer = self._user_serializer(
            data={"account": account, "password": password}
        )
        if serializer.is_valid():
            serializer.save()

    def login(self, **kwargs) -> str:
        account = kwargs.get("account")
        password = kwargs.get("password")

        user = self._user_serializer().find_one(account=account)
        if not user:
            raise ValueError("account or password is wrong.")
        user.compare_password(plain_password=password)

        return user.sign_token()
