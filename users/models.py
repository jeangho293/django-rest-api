from django.db import models
from bcrypt import checkpw
import jwt


class UserManager(models.Manager):
    def find_one(self, **filter_options):
        return self.get_queryset().filter(**filter_options).first()


# Create your models here.
class User(models.Model):
    account: str = models.CharField(max_length=255, unique=True)
    password: str = models.CharField(max_length=255)
    manager = UserManager()

    class Meta:
        db_table = "user"

    def compare_password(self, plain_password: str):
        if not checkpw(plain_password.encode("utf-8"), self.password.encode("utf-8")):
            raise ValueError("password is wrong.")

    def sign_token(self):
        return jwt.encode({"account": self.account}, "secret", algorithm="HS256")
