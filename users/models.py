from django.db import models


# Create your models here.
class UserManager(models.Manager):
    def get_user_list(self):
        return self.get_queryset().all()


class User(models.Model):
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    manager = UserManager()

    class Meta:
        db_table = "users"
