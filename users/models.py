from django.db import models


# Custom model Manager
class UserManager(models.Manager):
    def get_user_list(self):
        return self.get_queryset().all()

    def get_user(self, **kwargs):
        return self.get_queryset().filter(**kwargs).first()


# Create your models here.
class User(models.Model):
    account = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    manager = UserManager()

    class Meta:
        db_table = "users"
